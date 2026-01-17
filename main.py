import argparse
import sys
import os
import time
from src.indexer import HybridIndexer
from src.pipeline_manager import run_advanced_pipeline

# Colors for Professional Output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_step(message):
    print(f"\n{Colors.HEADER}🔹 {message}{Colors.ENDC}")

def print_success(message):
    print(f"{Colors.GREEN}✅ {message}{Colors.ENDC}")

def main():
    parser = argparse.ArgumentParser(description="ERPNext Architectural Refactoring Agent")
    subparsers = parser.add_subparsers(dest="command")

    #Initialize
    init_parser = subparsers.add_parser("init", help="Index the codebase with Hybrid Search")
    init_parser.add_argument("folder", help="Path to ERPNext source folder (e.g., data/)")

    #Ask 
    ask_parser = subparsers.add_parser("ask", help="Ask an Architectural Question")
    ask_parser.add_argument("question", help="The question to ask")

    args = parser.parse_args()

    if args.command == "init":
        print_step(f"Initializing Enterprise Knowledge Base from: {args.folder}")
        start_time = time.time()
        
        indexer = HybridIndexer()
        indexer.build_index(args.folder)
        
        elapsed = time.time() - start_time
        print_success(f"Indexing Complete in {elapsed:.2f} seconds.")

    elif args.command == "ask":
        print(f"\n{Colors.BOLD}🤖 ERPNext Architect Agent v2.0{Colors.ENDC}")
        print("-" * 50)
        print(f"❓ User Question: {Colors.BLUE}'{args.question}'{Colors.ENDC}")
        
        print_step("PHASE 1: Hybrid Retrieval (Dense + Sparse + Re-Rank)")
        indexer = HybridIndexer()
        
        try:
            target_file = indexer.search(args.question)
        except Exception as e:
            print(f"{Colors.FAIL}❌ Search Error: {e}{Colors.ENDC}")
            print(f"{Colors.WARNING}⚠️  Did you run 'python main.py init data/' first?{Colors.ENDC}")
            return

        if target_file:
            print_success(f"Target Identified: {target_file}")
            
            print_step("PHASE 2: AST Structural Analysis & Refactoring")
            print(f"{Colors.WARNING}   (Parsing Abstract Syntax Tree...){Colors.ENDC}")
            
            run_advanced_pipeline(args.question, target_file)
            
            print_success("Process Complete. Check 'generated/' folder for outputs.")
        else:
            print(f"{Colors.FAIL}❌ No relevant code found.{Colors.ENDC}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()