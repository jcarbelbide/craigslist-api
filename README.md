# craigslist-api
Simple Craigslist API to grab listings as JSON data. 
There is a showcase of this API running at:

https://jcarbelbide.com/craigslist-api

<h2>Technologies used</h2> 

Python-Flask, Beautiful Soup, Docker

<h2>Run on Your Docker Machine</h2>

To use this on your docker machine, run the following commands:
```bash
git clone https://github.com/jcarbelbide/craigslist-api.git
cd craigslist-api
docker build -t craigslist-api .
docker run -dp 8082:8082 craigslist-api
```

Please feel free to change the port in app.py and in the above command to run on a different port. 

<h2>To Use the API</h2>
Send a GET request over HTTP to your running Docker server and wait for the response. The larger the query, the longer the request will take. The URL will have the following form:

```JavaScript
`http://localhost:8082/api/${location}/${subLocation}/${board}/${startingIndex}/${formatQuery(query)}`
```

```location``` will be an area like ```sfbay``` or ```portland```.

```subLocation``` is a location within the main location. ```all``` will give all results within a location, while ```sby``` combined with ```sfbay``` as the ```location``` will give only results in the South Bay of the San Francisco Bay Area. 

```board``` is the Craigslist board you are searching. ```sss``` is "For Sale", ```jjj``` is the job board, ```eee``` is the event board. To find the code for a board, I recommend visiting the Craigslist site, going to the board you are interested in, and look at the URL.

Changing the ```startingIndex``` will result in only returning postings after and including the ```startingIndex```. If there are 500 postings, ```startingIndex=0``` will return posts 0-120. If ```startingIndex``` was 50, it would return posts 50-170. 

```query``` is your search string, which should use ```+``` in place of spaces. For example, if ```query = "mountain+bike"```, the API will return posts related to mountain bikes. 

If you are unsure what codes to use, play around with the actual Craigslist site and see what URL Craigslist creates. 

<br/>

An example request to the API is:

http://localhost:8082/api/sfbay/all/sss/0/mountain+bike
