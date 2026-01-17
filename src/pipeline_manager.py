import os
from .parser import CodeParser
from .visualizer import MermaidVisualizer
from .refactoring_engine import RefactoringEngine
from dotenv import load_dotenv

load_dotenv()

def run_advanced_pipeline(user_question, file_path):
    api_key = os.getenv("OPENROUTER_API_KEY") 
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY missing in .env")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f: source = f.read()
    except:
        print(f"❌ File not found: {file_path}")
        return

    parser = CodeParser(source)
    chunks = parser.extract_chunks()

    MermaidVisualizer.generate(chunks)

    engine = RefactoringEngine(api_key)
    
    context = "\n".join([f"Func: {c['name']} | Calls: {c['calls']}" for c in chunks[:5]])
    
    print("   🤖 Grok is refactoring...")
    ai_response = engine.propose_refactoring(user_question, context)
    
    print("\n" + "="*40)
    print("GROK RESPONSE:")
    print(ai_response[:300] + "...") 
    print("="*40 + "\n")

 
    engine.extract_and_save_code(ai_response)
    
    return ai_response