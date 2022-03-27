from flask import Flask, Response
from flask_cors import CORS, cross_origin
from craigslist_scraper import get_craigslist_listings


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'


@app.route("/api/<location>/<sub_location>/<board>/<starting_index>/<query>", methods=['GET', 'OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type', 'Authorization'])
def craigslist_api(location, sub_location, board, starting_index, query):

    json_list = get_craigslist_listings(location, sub_location, board, starting_index, query)

    resp = Response(response=json_list,
                    status=200,
                    mimetype="application/json")
    resp.headers.add('Access-Control-Allow-Origin', '*')

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
