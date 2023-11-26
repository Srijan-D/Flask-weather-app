import requests
from dotenv import load_dotenv
import os  # for accessing the environment variables
from pprint import pprint  # for pretty printing the JSON response


load_dotenv()


def get_weather_info(city="Mumbai"):
    api_key = os.getenv("API_KEY")
    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(request_url).json()
    return data


if __name__ == "__main__":
    city = input("Enter city name: ")
    data = get_weather_info(city)
    pprint(data)
