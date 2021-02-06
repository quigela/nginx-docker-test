import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_ibm():
    response = requests.get("https://api.polygon.io/v2/aggs/ticker/IBM/prev?unadjusted=true&apiKey=qKC33tW0gXmBUIDg_A3eltmY4YzRvZJJ")
    ibm_v = 0
    if response.status_code == 200:
        ibm_v = response.json()['results'][0]['c']

    return { 'ibm_v': ibm_v }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')