import os
from dotenv import load_dotenv
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory

load_dotenv()
key = os.getenv("CONTENT_SAFETY_KEY")
endpoint = os.getenv("CONTENT_SAFETY_ENDPOINT")

# Create an Azure AI Content Safety client
client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

# Set Blocklist name variable
blocklist_name = "code-words"


def analyze_text():
    # After you edit your blocklist, it usually takes effect in 5 minutes, please wait some time before analyzing
    # with blocklist after editing.

    # Construct request
    request = AnalyzeTextOptions(
        text="Jeepers, creepers, I hate you and want to beat you up.",
        blocklist_names=[blocklist_name],
        halt_on_blocklist_hit=False,
    )

    # Analyze text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        print("\nAnalyze text failed: ")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
            raise
        print(e)
        raise

    hate_result = next(
        item
        for item in response.categories_analysis
        if item.category == TextCategory.HATE
    )
    self_harm_result = next(
        item
        for item in response.categories_analysis
        if item.category == TextCategory.SELF_HARM
    )
    sexual_result = next(
        item
        for item in response.categories_analysis
        if item.category == TextCategory.SEXUAL
    )
    violence_result = next(
        item
        for item in response.categories_analysis
        if item.category == TextCategory.VIOLENCE
    )

    if hate_result:
        print(f"Hate severity: {hate_result.severity}")
    if self_harm_result:
        print(f"SelfHarm severity: {self_harm_result.severity}")
    if sexual_result:
        print(f"Sexual severity: {sexual_result.severity}")
    if violence_result:
        print(f"Violence severity: {violence_result.severity}")
    if response and response.blocklists_match:
        print("\nBlocklist match results: ")
        for match_result in response.blocklists_match:
            print(
                f"BlocklistName: {match_result.blocklist_name}, BlocklistItemId: {match_result.blocklist_item_id}, "
                f"BlocklistItemText: {match_result.blocklist_item_text}"
            )


if __name__ == "__main__":
    analyze_text()
