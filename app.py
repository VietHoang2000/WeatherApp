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
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
