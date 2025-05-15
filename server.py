"""server.py - Flask server for the Emotion Detector web application. 
   Updated after Pylint code analysis
"""
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    ''' This function calls the application
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response, status_code = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None or status_code == 400:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                        {response['anger']}, 'disgust': {response['disgust']}, \
                        'fear': {response['fear']}, 'joy': {response['joy']}, \
                        'sadness': {response['sadness']}. The dominant emotion is \
                        {response['dominant_emotion']}."

    return response_text

@app.route("/")
def render_index_page():
    ''' This is the function to render the html interface
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
