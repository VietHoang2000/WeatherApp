from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    api_key = 'b040117e1a49b4572f8a7a23c15c5a5f'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()
    weather_data['main']['temp'] = kelvin_to_celsius(weather_data['main']['temp'])
    return render_template('weather.html', weather=weather_data)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    app.run(debug=True)
