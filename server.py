from flask import Flask, render_template, request
from weather import get_weather_info

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello index page"


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_weather_info(city)
    return render_template(
        'weather.html',
        title=f"{weather_data['name']}",
        status=f"{weather_data['weather'][0]['description']}",
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
