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
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    response = requests.get(base_url.format(city, api_key)).json()

    if response['cod'] == 200:
        weather_data = {
            'city': response['name'],
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        return render_template('index.html', weather=weather_data)
    else:
        return render_template('index.html', error='City not found')

if __name__ == '__main__':
    app.run(debug=True)
