import google.generativeai as genai
from dotenv import load_dotenv
import os
import markdown as md
# Load .env file
load_dotenv()

# Initialize Gemini API
genai.configure(api_key=os.getenv("API_KEY"))

class Agent:
    def __init__(self, name: str, role:str):
        self.name = name
        self.role = role
        self.model = genai.GenerativeModel(model_name=os.getenv("MODEL_NAME"), system_instruction=role) # system_instruction is the role of the AI model

    def generate_response(self, prompt: str):
        response = self.model.generate_content(prompt) # generate_content method generates content based on the prompt
        return response.text
 

class CustomerRelationOfficer(Agent):
    def get_user_intent(self, max_interactions: int = 5) -> str:
        msg = """Hi! I'm a Customer Relation Officer. Let's discuss your report needs. What's the main topic of your report?"""
        converstaion = [f"{self.name}: {msg}"]
        report_topic = input(f"{self.name}: {msg} ")
        converstaion.append(f"User: {report_topic}")

        for i in range(max_interactions):
            prompt = f"""
            -----------------------------------
            Current conversation:
            -----------------------------------
            {''.join(converstaion)}"""
            response = self.generate_response(prompt)
            md.print_formatted_md(f"{self.name}: {response}")
            converstaion.append(f"{self.name}: {response}")

            if response.startswith("SUMMARY"):
                return response
            
            if i < max_interactions - 1:
                user_input = input("Your response: ")
                converstaion.append(f"User: {user_input}")
            
        # If we have reached the maximum number of interactions wihout a summary, generate one
        summary_prompt = f"""We have reached the maximum number of interactions. Now, summarize the user's intent and expectations based on the conversation so far: {''.join(converstaion)}
        Provide a summary in the format:
        SUMMARY: [User's main topic]
        Intent: [Summarized intent]
        Expectations: [List of expectations]"""

        response = self.generate_response(summary_prompt)
        md.print_formatted_md(response)
        return response

    def deliver_report(self, report: str):
        print("\nYour report is ready! Here is the summary:")
        md.print_formatted_md(report)

        # Convert report to a word document
        report_file = "report.docx"
        md.convert_md_to_docx(report, report_file)
        print(f"\nReport saved as {report_file}")
    
class Author(Agent):
    def write_report(self, user_intent: str):
        prompt = f"""Write a report based on the user's intent and expectations: {user_intent}"""
        return self.generate_response(prompt)

    def revise_report(self, original_report: str, editor_feedback: str, user_intent: str):
        prompt = f"""Revise the report based on the editor's feedback and the original user intent:
        Original report: {original_report}
        Editor feedback: {editor_feedback}
        User intent: {user_intent}
        Please provide a revised report."""
        return self.generate_response(prompt)

class Editor(Agent):
    def review_report(self, report: str, user_intent: str):
        prompt = f"""Review the report: {report} based on the user's intent and expectations: {user_intent}"""
        return self.generate_response(prompt)

