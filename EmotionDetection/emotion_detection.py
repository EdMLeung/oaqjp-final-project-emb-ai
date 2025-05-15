import requests, json # Import the requests library to handle HTTP requests

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    status_code = response.status_code
    
    # Check if error and dictionary as empty
    if status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Parse the JSON response from the API
        formatted_response = response.json()

        # Extract emotion label from the response
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Find the max emotion rating from the set of emotions
        dominant_emotion = max(emotions, key = emotions.get)

        # Return the response text from the API
        return {'anger': emotions ["anger"],'disgust': emotions ["disgust"],'fear': emotions ["fear"],
        'joy': emotions ["joy"],'sadness': emotions ["sadness"],'dominant_emotion': dominant_emotion}