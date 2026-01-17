import os
import chromadb
import pickle
import time
from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder, SentenceTransformer 
from dotenv import load_dotenv

load_dotenv()

class HybridIndexer:
    def __init__(self, persist_dir="chroma_db"):
        print(f"⚙️  Initializing Enterprise RAG Engine (Grok-Ready)...")
        
        #Vector Database
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(name="erpnext_hybrid")
        
        #Local Embedding Model
        print("   🧠 Loading Local Embedding Model (all-MiniLM-L6-v2)...")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        #Neural Re-Ranker
        print("   ⚖️  Loading Cross-Encoder (ms-marco-MiniLM-L-6-v2)...")
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        
        self.bm25 = None
        self.doc_map = {} 

    def get_embedding(self, text):
        """Generates Embeddings LOCALLY (Zero Latency, No Rate Limits)"""
        
        return self.embedder.encode(text).tolist()

    def build_index(self, folder_path):
        print(f"🚀 Scanning Dataset: {folder_path}")
        documents = []
        ids = []
        embeddings = []
        tokenized_corpus = []
        
        count = 0
        MAX_FILES = 20 

        for root, _, files in os.walk(folder_path):
            if count >= MAX_FILES: break
            for file in files:
                if count >= MAX_FILES: break
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                            code = f.read()
                            if len(code) > 50:
                                doc_text = f"FILE: {file}\nPATH: {full_path}\nCONTENT:\n{code[:3000]}"
                                
                                documents.append(doc_text)
                                ids.append(full_path)
                                # Local Embedding
                                embeddings.append(self.get_embedding(doc_text))
                                
                                tokens = doc_text.lower().split()
                                tokenized_corpus.append(tokens)
                                self.doc_map[len(tokenized_corpus)-1] = full_path
                                
                                count += 1
                                print(f"   🔹 Indexed {count}/{MAX_FILES}: {file}")
                    except: pass

        if documents:
            self.collection.upsert(documents=documents, ids=ids, embeddings=embeddings)
        
        print("   📊 Training BM25 Sparse Model...")
        self.bm25 = BM25Okapi(tokenized_corpus)
        
        os.makedirs("data", exist_ok=True)
        with open("data/bm25.pkl", "wb") as f: pickle.dump(self.bm25, f)
        with open("data/doc_map.pkl", "wb") as f: pickle.dump(self.doc_map, f)
            
        print(f"✅ Indexed {count} files using Local Intelligence.")

    def search(self, query, top_k=10):
        print(f"🔍 Hybrid Search: '{query}'")
        
        # 1. Vector Search (Local)
        query_emb = self.get_embedding(query)
        vector_results = self.collection.query(query_embeddings=[query_emb], n_results=top_k)
        vector_files = vector_results['ids'][0] if vector_results['ids'] else []

        # 2. BM25 Search
        if not self.bm25 and os.path.exists("data/bm25.pkl"):
            with open("data/bm25.pkl", "rb") as f: self.bm25 = pickle.load(f)
            with open("data/doc_map.pkl", "rb") as f: self.doc_map = pickle.load(f)

        tokenized_query = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)
        top_n = sorted(range(len(bm25_scores)), key=lambda i: bm25_scores[i], reverse=True)[:top_k]
        bm25_files = [self.doc_map[i] for i in top_n if i in self.doc_map]

        #Rerank
        candidates = list(set(vector_files + bm25_files))
        if not candidates: return None

        pred_input = [[query, c] for c in candidates]
        scores = self.reranker.predict(pred_input)
        ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)
        
        best_file = ranked[0][0]
        print(f"   🎯 Winner: {best_file} (Score: {ranked[0][1]:.4f})")
        return best_file