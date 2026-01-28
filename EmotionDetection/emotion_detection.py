''' Module te capture user input and return label and score '''
import json
# Import the requests library to handle HTTP requests
import requests
def emotion_detector(text_to_analyze):
    """ Function to capture emotion and return label and score """   
    # URL of the sentiment analysis service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=input_json, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    
    emotion_predictions = formatted_response.get('emotionPredictions', [])
    if emotion_predictions:
        prediction = emotion_predictions[0]
    
        if response.status_code == 200:
            emotion_scores = {
                'anger': prediction['emotion']['anger'],
                'disgust': prediction['emotion']['disgust'],
                'fear': prediction['emotion']['fear'],
                'joy': prediction['emotion']['joy'],
                'sadness': prediction['emotion']['sadness']
            }

            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion

        elif response.status_code == 400 or response.status_code == 500:
            emotion_scores = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            
    else:
        emotion_scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotion_scores
