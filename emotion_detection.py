import requests

def emotion_detector(text_to_analyze):
    # URL of the Watson Emotion Prediction service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Header specifying the model ID
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Request payload
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request and return response text
    response = requests.post(url, json=myobj, headers=headers)
    return response.text