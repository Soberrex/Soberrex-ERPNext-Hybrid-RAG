import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class RefactoringEngine:
    def __init__(self, api_key):
       
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        self.model = "meta-llama/llama-3.2-3b-instruct"

    def propose_refactoring(self, user_question, context):
        prompt = f"""
        You are a Senior ERPNext Architect.
        
        CONTEXT:
        {context}
        
        USER REQUEST: {user_question}
        
        TASK:
        1. Analyze the dependencies.
        2. Write a refactored 'Service Class' in Python.
        3. Write a Pytest unit test.
        """
        
        try:
            print(f"   🚀 Sending request to OpenRouter ({self.model})...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert Python Refactoring Agent."},
                    {"role": "user", "content": prompt}
                ],
                # OpenRouter specific headers for rankings (optional but good practice)
                extra_headers={
                    "HTTP-Referer": "https://github.com/erpnext-analyzer", 
                    "X-Title": "ERPNext Analyzer"
                }
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ OpenRouter Error: {str(e)}"

    @staticmethod
    def extract_and_save_code(ai_text, output_dir="generated/"):
        os.makedirs(output_dir, exist_ok=True)
        
        # Regex to capture code blocks
        code_blocks = re.findall(r'```python(.*?)```', ai_text, re.DOTALL)
        
        if code_blocks:
            with open(f"{output_dir}new_service.py", "w") as f:
                f.write(code_blocks[0].strip())
            print(f"   ✅ Saved Refactored Code to {output_dir}new_service.py")
            
            if len(code_blocks) > 1:
                with open(f"{output_dir}test_service.py", "w") as f:
                    f.write(code_blocks[1].strip())
                print(f"   ✅ Saved Unit Tests to {output_dir}test_service.py")
        else:
            print("   ⚠️ No code blocks found in response.")