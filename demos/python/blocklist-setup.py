import os
from dotenv import load_dotenv
from azure.ai.contentsafety import BlocklistClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import (
    TextBlocklist,
    AddOrUpdateTextBlocklistItemsOptions,
    TextBlocklistItem,
)
from azure.core.exceptions import HttpResponseError

load_dotenv()
key = os.getenv("CONTENT_SAFETY_KEY")
endpoint = os.getenv("CONTENT_SAFETY_ENDPOINT")

# Create a Blocklist client
client = BlocklistClient(endpoint, AzureKeyCredential(key))

# Provide Blocklist name and description
blocklist_name = "<name your list here>"
blocklist_description = "<description here>"

# Create Blocklist
try:
    blocklist = client.create_or_update_text_blocklist(
        blocklist_name=blocklist_name,
        options=TextBlocklist(
            blocklist_name=blocklist_name, description=blocklist_description
        ),
    )
    if blocklist:
        print("\nBlocklist created or updated: ")
        print(f"Name: {blocklist.blocklist_name}, Description: {blocklist.description}")
except HttpResponseError as e:
    print("\nCreate or update text blocklist failed: ")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    print(e)
    raise

# Add terms to Blocklist
blocklist_item_text_1 = "jeepers"
blocklist_item_text_2 = "creepers"

blocklist_items = [
    TextBlocklistItem(text=blocklist_item_text_1),
    TextBlocklistItem(text=blocklist_item_text_2),
]
try:
    result = client.add_or_update_blocklist_items(
        blocklist_name=blocklist_name,
        options=AddOrUpdateTextBlocklistItemsOptions(blocklist_items=blocklist_items),
    )
    for blocklist_item in result.blocklist_items:
        print(
            f"BlocklistItemId: {blocklist_item.blocklist_item_id}, Text: {blocklist_item.text}, Description: {blocklist_item.description}"
        )
except HttpResponseError as e:
    print("\nAdd blocklistItems failed: ")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    else:
        print(e)
        raise
