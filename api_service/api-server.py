import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_weather():
    response = requests.get("http://api.weatherapi.com/v1/current.json?key="+
                                "7baba497c77c4bb58a7202216210502&q=18976")
    temp = 0
    print(response.json())
    if response.status_code == 200 :
        temp = response.json()['current']['temp_f']
    
    return { 'temp_f': temp }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')