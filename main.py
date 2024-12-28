from markdown import *
from agent import *
ROLES = {
    "cro": """
    As a Customer Relation Officer, your aim is to gather information about the user's intent and expectation for generating a comprehensive report.

    Ask necessray questions to understand the user's needs and expectations.

    If you are not sure that you have enough information to generate a report, ask the user to provide more details.

    Answer the questions asked to you in question language.
    
    If you think that you have enough information about the intent and expectations for the report, stop asking questions and provide a summary by filling in the following format:
    SUMMARY: [User's main topic]
    Intent: [Summarized intent]
    Expectations: [List of expectations]

    -----------------------------------
    Current conversation:
    -----------------------------------
    """,
    "author": """
    As an Author, your aim is to write a report based on the user's intent and expectations and then imporve it based on the editor's feedback.
    
    First you will be given the user's intent and expectations. Prepare the report based on this information.
    
    Then, an Editor will check your report and provide feedback. You will need to revise the report based on the feedback and the original user intent.""",
    "editor": """
    As an Editor, your aim is to review the report written by the Author and provide feedback based on the given user intent and expectations.
    //////////////////////////////////////////
    GENERAL RUILES:
    //////////////////////////////////////////
    Each sections should have at least 3 paragraphs. Each paragraph should have at least 15 sentences.

    The report must be to the point and should not contain any irrelevant information.

    There should be no grammatical errors in the report.

    The conclusion of the report should meet the user's expectations.

    You can give as many revisions as you find reasonable to prepare the report. But your revision limit is 15. Your request must be clear, easy to follow, and concise. If possible, give simple instructions to revise the report step by step.

    //////////////////////////////////////////
    ACTION RULES:
    //////////////////////////////////////////
    First decide if the report needs any revisions according to the user's intent and expectations.

    Then, select one of the below actions:

    A. If some revisions are required, response with the following format:
    ***Revision Required:...***

    B. Else, if there is no need for revisions, response with the following format:
    ***Done! Report meets the user's expectations.***

    """

}
def generate_report():
    """"""
    cro = CustomerRelationOfficer("CRO", ROLES["cro"])
    author = Author("Author", ROLES["author"])
    editor = Editor("Editor", ROLES["editor"])

    users_intent = cro.get_user_intent()
    print("\n------------------CRO------------------")
    print("\nUser intent and expectations gathered.")
    print("\n------------------Author------------------")
    report = author.write_report(users_intent)
    
    count_revisions = 0

    while True:
        print_formatted_md(f"Draft Report (Revision {count_revisions + 1}): \n{report}\n")
        print(f"\n------------------Editor------------------")
        review = editor.review_report(report, users_intent)
        print_formatted_md(f"Editor's Review (Revision {count_revisions + 1}): \n{review}\n")

        if "meets the user's expectations" in review.lower():
            break
        elif count_revisions < 15:
            print("\n------------------Author------------------")
            print("Revising report based on editor's feedback...\n")
            report = author.revise_report(report, review, users_intent)
        else:
            print("\n------------------SYSTEM------------------")
            print(f"\nMaximum number of revisions reached. Report not finalized. Revisions: {count_revisions}")
            break
        print("\n------------------CRO------------------")
        cro.deliver_report(report)

if __name__ == "__main__":
    generate_report()