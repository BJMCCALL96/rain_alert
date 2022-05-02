
import requests
from twilio.rest import Client
OWM_end="https://api.openweathermap.org/data/2.5/onecall"
api_key=""
account_sid = ''
auth_token = ''



#https://api.openweathermap.org/data/2.5/weather?lat=37.6922361&lon=-97.3375448&appid=5d902227bbb3723953ebd6140c482511


def text():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='-',
        body='It is going to rain today, bring an umbrella  ☂',
        to='+000000000'
    )

param={
    "lat": "YOUR LAT",
    "lon": -"YOUR LONG",
    "appid": api_key,
    "units": "imperial",
    "exclude":"current,minutely,daily,alerts"

}

rain=False

response=requests.get(url=(OWM_end), params=param)
print(response.json()["hourly"][0]["weather"][0]["main"])
while rain is False:
    for x in range(0,12):
        main=(response.json()["hourly"][x]["weather"][0]["main"])
        if main == "Rain":
            rain = True
            text()
            break