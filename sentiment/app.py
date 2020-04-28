from flask import Flask, jsonify, request
from summarizer import Summarizer
from textblob import TextBlob
from flask_cors import CORS



app = Flask(__name__)
CORS(app)


@app.route('/analyse/sentiment', methods=['POST'])
def analyse_sentiment():

    data = request.get_data()
    data = data.decode("utf-8").replace("'", '')
    # exit()

    value = list(TextBlob(data).sentiment)[0]
    value = int(value*100)
    sentiment = ''
    if value in range(-20, 30):
        sentiment = "Neutral"
    elif value in range(30, 80):
        sentiment = "Mediocre Positive"
    elif value > 70:
        sentiment = "Positive"
    elif value in range(-70, -20):
        sentiment = "Mediocre Negative"
    elif value < -70:
        sentiment = "Negative"

    return jsonify({'sentiment': sentiment})


@app.route('/analyse/summar', methods=['POST'])
def analyse_summary():

    data = request.get_data()
    data = data.decode("utf-8").replace("'", '')

    model = Summarizer()
    result = model(data, min_length=60)
    summary = ''.join(result)

    return jsonify({'summar': summary})


# driver function
if __name__ == '__main__':

    app.run(debug=True)
