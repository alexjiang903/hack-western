from flask import Flask, jsonify, request

import requests

import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()

