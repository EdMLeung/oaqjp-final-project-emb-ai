# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from emotion_detection import emotion_detector

# Create an instance of the Flask class, passing in the name of the current module
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotionDetector():
    ''' This code receives the text from the HTML and 
        calls emotion detection(). The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Check if missing input
    #if not text_to_analyze:
    #    return "Input parameter missing"

    # Check if the label is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"

    response_text = f"For the given statement, the system response is 'anger': \
                    {response['anger']}, 'disgust': {response['disgust']}, \
                    'fear': {response['fear']}, 'joy': {response['joy']}, \
                    'sadness': {response['sadness']}. The dominant emotion is \
                    {response['dominant_emotion']}."

    return response_text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main html
        page over the Flask channel
    '''
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it 
        on localhost:5000
    '''
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)