import requests # lib uses for making HTTP requests
import json # lib used for working with JSON objects

url = "https://interview-flask-app.herokuapp.com/predict?level=Junior&lang=Java&tweets=yes&phd=yes"

response = requests.get(url)

if response.status_code == 200:
    json_object = json.loads(response.text) # load Json object from the message body
    print(json_object)
    prediction = json_object["prediction"]
    print(prediction)


    