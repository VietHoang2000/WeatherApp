from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = 'b040117e1a49b4572f8a7a23c15c5a5f'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(weather_url)
    weather_data = response.json()

    if weather_data.get('cod') != '404':
        weather = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        weather = None

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
