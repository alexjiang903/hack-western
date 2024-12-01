from flask import Flask, jsonify, request
from flask_cors import CORS

import requests

import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

app = Flask(__name__)
CORS(app)


def vfFunction(reply, definition, context):
    name = " "
    interact(name, { 'type': 'launch' })

    # reply = input("def(Yes) or summary(No)\n")
    if (reply == "Yes"):
        interact(name, { 'type': 'text', 'payload': "Yes" })
        # definition = input("input def\n")
        interact(name, { 'type': 'text', 'payload': definition })
    else:
        interact(name, { 'type': 'text', 'payload': "No" })
    # context = input("input context\n")
    answer = interact(name, { 'type': 'text', 'payload': context })
    print("answer")
    return answer

# user_id defines who is having the conversation, e.g. steve, john.doe@gmail.com, username_464
def interact(user_id, request):
    response = requests.post(
        f'https://general-runtime.voiceflow.com/state/user/{user_id}/interact',
        json={ 'request': request },
        headers={ 
            'Authorization': os.getenv("API_KEY"),
            'versionID': 'production'
        },
    )
    # return response.json()

@app.route('/interact', methods=['POST'])
def handle_interaction():
    data = request.json  # Get the input data (e.g., reply, definition, context)
    reply = data.get('reply')
    definition = data.get('definition')
    context = data.get('context')

    answer = vfFunction(reply, definition, context)
    return jsonify({'answer': answer})

@app.route('/api/test', methods=['GET'])
def test_endpont(): 
    return "Server is running"

@app.route('/asr', methods=['POST'])
def asr():
    # Access the uploaded file
    audio_file = request.files.get('audio_file')
    if not audio_file:
        return jsonify({'error': 'No file uploaded'}), 400

    # Call your transcription function (assuming it works with the uploaded file)
    transcript = transcribe_audio(audio_file)

    return jsonify({'transcript': transcript})

if __name__ == '__main__':
    app.run(host="localhost", port=9000)
