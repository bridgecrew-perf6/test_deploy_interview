# we are going to use a micro web framework called Flask
# goal is to create a web app for our simple /predict API service
from flask import Flask, jsonify, request
import os
app = Flask(__name__)


# we need to add a route (2 actually)
# a route for the homepage
# a route is a path on a server to a function that handles the requests

@app.route("/", methods=["GET", "POST"])
# define the function that should execute when this request is routed to this function
def index():
    # return content and response code
    return"<h1>Welcome to the app!!</h1>", 200
# aroutefor /predict
@app.route("/prediction", methods=["GET"])
def predict():
    # goals
    # parse out the level, lang, tweets, phd, args from the query string
    # use the request object to get the current requests query args
    level = request.args.get("level", "")
    lang = request.args.get("lang", "")
    tweets = request.args.get("tweets", "")
    phd = request.args.get("phd", "")
    print("level:", level, lang, tweets, phd)
    result = {"prediction":"True_mm_onHeroku"} # TODO: fix hardcoding
    return jsonify(result), 200


if __name__ == "__main__":
    # deployment notes
    # two main categories on deployment
    # host your own server OR use a cloud provider AWS, Azure, Heroku, DigitalOcean,...)
    # we are going to use Heroku (BaaS, backend as a service)
    # there are quite a few ways to deploy a Flask app to Heroku
    # 1. deploy the app directly on an ubuntu "stack" (e.g. Procfile and requirements.txt)
        # Procfile is used by Heroku i order to know how to build the application

    # 2. deploy the app as a Docker container on a container "stack" (e.g. Dockerfile)
    # 2.A. build a Docker image locally and push the image to a container registry (e.g. Heroku's registry) 
    # 2.B. define a heroku.yaml and push your source code to Heroku's git and 
    # Heroku is going to build the Docker image (and register it)
    # 2.C define main.yaml and pushes the image to registry (e.g. Heroku's registry)

    port = os.environ.get("PORT", 5000) # 5000 by default and Heroku will set a port environment variable for web trafic
    app.run(debug=False, host="0.0.0.0", port = port) # set debug=False before deployement!!

