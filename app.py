from flask import Flask, render_template,request
import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

app = Flask(__name__)
api_key = os.getenv('KEY')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        weather_data_hourly = get_hourly_forecast(city)

        return render_template('index.html',weather_data=weather_data)
    else:
        return render_template('index.html')

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def get_hourly_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    data = requests.get(url).json()
    return data

if __name__ == '__main__':
    app.run(debug=True)
