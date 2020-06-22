from sql_films import get_films_db
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "super secret key"


@app.route('/api/v1/', methods=['GET'])
@cross_origin()
def get_films():
    url = "https://ghibliapi.herokuapp.com/films"
    request = requests.get(url).json()
    for film in get_films_db():
        for api_film in request:
            if film["code"] in api_film["id"]:
                api_film["title_rus"] = film["title_rus"]
    return jsonify(request)


if __name__ == "__main__":
    app.run(debug=True)
