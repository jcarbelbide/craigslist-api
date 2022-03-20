from flask import Flask, Response
from flask_cors import CORS, cross_origin
from craigslist_scraper import get_craigslist_listings


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api/<location>/<sub_location>/<board>/<starting_index>/<query>")
@cross_origin()
def craigslist_api(location, sub_location, board, starting_index, query):

    json_list = get_craigslist_listings(location, sub_location, board, starting_index, query)

    resp = Response(response=json_list,
                    status=200,
                    mimetype="application/json")

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0")
