import json
# Import the requests library to handle HTTP requests
import requests
def emotion_detector(text_to_analyse):
    """ Function to capture emotion and return label and score """   
    # URL of the sentiment analysis service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyse } }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=input_json, headers=header, timeout=10)
    return response.text
