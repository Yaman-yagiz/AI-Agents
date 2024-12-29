import google.generativeai as genai
from dotenv import load_dotenv
import os
import formatter as md
import json
from typing import Dict, Any

# Load .env file
load_dotenv()

# Initialize Gemini API
genai.configure(api_key=os.getenv("API_KEY"))

class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.model = genai.GenerativeModel(
            model_name=os.getenv("MODEL_NAME"), 
            system_instruction=role
        )

    def generate_response(self, prompt: str) -> Dict[str, Any]:
        """Generate a response and parse it as JSON"""
        try:
            response = self.model.generate_content(prompt)
            # Response içeriğindeki JSON string'i çıkartıyoruz
            text_content = response.text
            # JSON string'i temizleme
            if text_content.startswith("```json"):
                text_content = text_content.replace("```json", "").replace("```", "").strip()
            return json.loads(text_content)
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return {
                "action": "error",
                "message": "Failed to parse response as JSON"
            }
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {
                "action": "error",
                "message": f"An error occurred: {str(e)}"
            }

class CustomerRelationOfficer(Agent):
    def get_user_intent(self, max_interactions: int = 5) -> Dict[str, Any]:
        """
        Gather user intent through conversation and return structured data
        Returns a dictionary containing user intent and expectations
        """
        initial_msg = "Hi! I'm a Customer Relation Officer. Let's discuss your report needs. What's the main topic of your report?"
        conversation = [f"{self.name}: {initial_msg}"]
        report_topic = input(f"{self.name}: {initial_msg} ")
        conversation.append(f"User: {report_topic}")

        for i in range(max_interactions):
            prompt = f"""
            Based on the following conversation, either:
            1. Ask another question to gather more information
            2. If you have enough information, provide a summary

            Current conversation:
            -----------------------------------
            {''.join(conversation)}
            -----------------------------------
            
            Respond in JSON format only.
            """
            
            response = self.generate_response(prompt)
            
            if response["action"] == "done":
                return response["summary"]
            
            # Continue conversation
            print(f"\n{self.name}: {response['message']}")
            conversation.append(f"{self.name}: {response['message']}")
            
            if i < max_interactions - 1:
                user_input = input("Your response: ")
                conversation.append(f"User: {user_input}")
            
        # Force summary if max interactions reached
        force_summary_prompt = f"""
        Maximum interactions reached. Provide a final summary of the conversation:
        {''.join(conversation)}
        
        Respond in JSON format with action: "done" and include the summary.
        """
        
        final_response = self.generate_response(force_summary_prompt)
        return final_response["summary"]

    def deliver_report(self, report: Dict[str, Any]) -> None:
        """Deliver the final report to the user"""
        print("\nYour report is ready! Here is the summary:")
        md.print_formatted_md(report["content"])

        # Convert report to a word document
        report_file = "report.docx"
        md.convert_md_to_docx(report["content"], report_file)
        print(f"\nReport saved as {report_file}")

class Author(Agent):
    def write_report(self, user_intent: Dict[str, Any]) -> Dict[str, Any]:
        """Write initial report based on user intent"""
        prompt = f"""
        Write a report based on the following user intent and expectations:
        {json.dumps(user_intent, indent=2)}
        
        Respond in JSON format with:
        {{
            "action": "done",
            "report": {{
                "content": "your report content",
                "sections": ["list of sections"],
                "word_count": number
            }}
        }}
        """
        response = self.generate_response(prompt)
        return response["report"]

    def revise_report(self, 
                     original_report: Dict[str, Any], 
                     editor_feedback: Dict[str, Any], 
                     user_intent: Dict[str, Any]) -> Dict[str, Any]:
        """Revise report based on editor feedback"""
        prompt = f"""
        Revise the report based on the following:
        
        Original Report:
        {json.dumps(original_report, indent=2)}
        
        Editor Feedback:
        {json.dumps(editor_feedback, indent=2)}
        
        User Intent:
        {json.dumps(user_intent, indent=2)}
        
        Respond in JSON format with the revised report.
        """
        response = self.generate_response(prompt)
        return response["report"]

class Editor(Agent):
    def review_report(self, 
                     report: Dict[str, Any], 
                     user_intent: Dict[str, Any]) -> Dict[str, Any]:
        """Review report and provide structured feedback"""
        prompt = f"""
        Review the following report based on the user's intent and expectations:
        
        Report:
        {json.dumps(report, indent=2)}
        
        User Intent:
        {json.dumps(user_intent, indent=2)}
        
        Respond in JSON format with either:
        
        For revisions needed:
        {{
            "action": "revise",
            "feedback": {{
                "general_comments": "overall feedback",
                "specific_issues": ["list of issues"],
                "improvement_suggestions": ["list of suggestions"]
            }}
        }}
        
        For approved report:
        {{
            "action": "done",
            "feedback": {{
                "message": "Report meets expectations",
                "strengths": ["list of strong points"]
            }}
        }}
        """
        return self.generate_response(prompt)