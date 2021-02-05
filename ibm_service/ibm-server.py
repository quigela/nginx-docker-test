import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_ibm():
    ibm_v = round(random.uniform(120.52, 121.80), 2)
    return { 'ibm_v': ibm_v }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')