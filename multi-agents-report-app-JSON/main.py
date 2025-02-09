from agent import CustomerRelationOfficer, Author, Editor
import formatter as md
from typing import Dict, Any

ROLES = {
    "cro": """You are a Customer Relations Officer. Your role is to:
    1. Understand the user's report requirements
    2. Ask relevant questions to gather complete information
    3. Structure the gathered information
    4. Answer in the language spoken to you (IMPORTANT):
        1. EXAMPLE:
            Q: What's the main topic of your report?
            A: The topic is "Impact of Technology on Education".
            Then continue in English.

        2. EXAMPLE:
            Q: What's the main topic of your report?
            A: Yapay zeka ve siber güvenlik.
            Then continue in Turkish.

    Always respond in JSON format:
    {
        "action": "continue | done",
        "message": "your question or message when continuing",
        "summary": {
            "topic": "main report topic",
            "purpose": "report purpose",
            "target_audience": "intended audience",
            "key_points": ["point1", "point2", ...],
            "special_requirements": ["req1", "req2", ...],
            "tone": "formal/informal/technical/etc",
            "length_requirement": "expected length"
        }
    }""",

    "author": """You are a Report Author. Your role is to:
    1. Write reports based on user requirements
    2. Revise reports based on editor feedback
    3. Maintain consistent style and tone

    Always respond in JSON format:
    {
        "action": "done",
        "report": {
            "content": "full report content in markdown",
            "sections": ["section1", "section2", ...],
            "word_count": number,
            "metadata": {
                "tone": "used tone",
                "target_audience": "intended audience",
                "key_points_covered": ["point1", "point2", ...]
            }
        }
    }""",

    "editor": """You are a Report Editor. Your role is to:
    1. Review reports for quality and completeness
    2. Ensure alignment with user requirements
    3. Provide constructive feedback

    Always respond in JSON format:
    {
        "action": "revise | done",
        "feedback": {
            "general_comments": "overall assessment",
            "specific_issues": ["issue1", "issue2", ...],
            "improvement_suggestions": ["suggestion1", "suggestion2", ...],
            "strengths": ["strength1", "strength2", ...],
            "alignment_score": number (1-10),
            "quality_score": number (1-10)
        }
    }"""
}

def generate_report() -> None:
    """Main function to orchestrate the report generation process"""
    # Initialize agents
    cro = CustomerRelationOfficer("CRO", ROLES["cro"])
    author = Author("Author", ROLES["author"])
    editor = Editor("Editor", ROLES["editor"])

    print("\n------------------CRO------------------")
    # Get user requirements through conversation
    user_intent = cro.get_user_intent()
    
    print("\n------------------Author------------------")
    print("Writing initial report based on requirements...\n")
    
    # Get initial report from author
    report = author.write_report(user_intent)
    count_revisions = 1
    max_revisions = 5

    # Revision cycle
    while True:
        print("\n------------------Current Report------------------")
        md.print_formatted_md(f"Draft Report (Revision {count_revisions})")
        md.print_formatted_md(report["content"])
        
        print("\n------------------Editor Review------------------")
        review_result = editor.review_report(report, user_intent)
        
        # Check editor's decision
        if review_result["action"] == "done":
            print(f"\n✅ Report Approved! (Revision Count-{count_revisions})")
            md.print_formatted_md(review_result["feedback"]["general_comments"])
            print("\nStrengths:")
            for strength in review_result["feedback"]["strengths"]:
                print(f"- {strength}")
            break
            
        elif count_revisions > max_revisions:
            print(f"\n⚠️ Maximum revision limit ({max_revisions}) reached!")
            print("Delivering final version despite pending improvements.")
            break
            
        else:
            print(f"\n📝 Revision Required (Revision Count-{count_revisions}):")
            md.print_formatted_md(review_result["feedback"]["general_comments"])
            print("\nSpecific Issues:")
            for issue in review_result["feedback"]["specific_issues"]:
                print(f"- {issue}")
                
            print("\n------------------Revision in Progress------------------")
            report = author.revise_report(report, review_result["feedback"], user_intent)
            count_revisions += 1

    # Deliver final report
    print("\n------------------Final Delivery------------------")
    cro.deliver_report(report)

if __name__ == "__main__":
    try:
        generate_report()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user. Exiting...")
    except Exception as e:
        print(f"\n\nAn error occurred: {str(e)}")