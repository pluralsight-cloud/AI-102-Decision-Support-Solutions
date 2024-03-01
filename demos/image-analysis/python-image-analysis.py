import os
from dotenv import load_dotenv
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData, ImageCategory
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError

# Pass in endpoint/key values
load_dotenv()
key = os.getenv("CONTENT_SAFETY_KEY")
endpoint = os.getenv("CONTENT_SAFETY_ENDPOINT")

# Create an Azure AI Content Safety client
client = ContentSafetyClient(endpoint, AzureKeyCredential(key))


def analyze_image(image_path):

    # Build request
    with open(image_path, "rb") as file:
        request = AnalyzeImageOptions(image=ImageData(content=file.read()))

    # Analyze image
    try:
        response = client.analyze_image(request)
    except HttpResponseError as e:
        print(f"Analyze image failed for {image_path}.")
        if e.error:
            print(f"Error code: {e.error.code}")
            print(f"Error message: {e.error.message}")
        return

    # Process analysis results
    for result in response.categories_analysis:
        print(f"Category: {result.category}, Severity: {result.severity}")


def process_images(directory):
    for file_name in os.listdir(directory):
        if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            print(f"\nProcessing {file_name}")
            analyze_image(os.path.join(directory, file_name))


if __name__ == "__main__":
    images_folder = "sample_data"
    process_images(images_folder)
