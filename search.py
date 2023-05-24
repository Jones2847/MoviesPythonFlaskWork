from flask import Flask, render_template, jsonify
import requests
import json

from serpapi import GoogleSearch

app = Flask(__name__)

params = {
 

"engine":"google",
"q":"What are the top movies playing right now?",
"location_requested":"Portugal",
"location_used":"Portugal",
"google_domain":"google.pt",
"hl":"pt",
"gl":"pt",
"device":"desktop",
  "api_key": "43557ec561d73d75956e01a96594843777f01ab4889657914adf50333a0b019d"
}

search = GoogleSearch(params)
results = search.get_dict()
answer_box = results["answer_box"]
num_length = (len(answer_box["list"]))

for n in range (num_length):
  num_length_temp = (len(answer_box["list"][n]))
  answer_box["list"][n] = answer_box["list"][n][4:num_length_temp]
  answer_box["list"][n] = answer_box["list"][n].split('(')[0].strip()



def get_movies(strMovie):
    """url = f'https://api.themoviedb.org/3/search/movie?api_key=e207618e75816868e3d98474c4b2419b&query=Guardians of the Galaxy Vol. 3'"""
    url = f'https://api.themoviedb.org/3/search/movie?api_key=e207618e75816868e3d98474c4b2419b&query={strMovie}'
    response = requests.get(url)
    data = response.json()

    return data


@app.route("/")

def index():

    movies_list = answer_box["list"]
    movie_results = []  # Create an empty list to store movie results


    for num in range(5):
      movies = get_movies(answer_box["list"][num])
      movie_results.append(movies.get('results'))  # Append each movie result to the list

    """ 
    return render_template("search.html",results=movie_results[0]['overview'])
    """
    """
    return render_template("search.html",results=movie_results[0]['overview'], poster =movie_results[0]['poster_path'])
    """
    return render_template("search.html",results=movie_results)



app.run(debug=True,host="0.0.0.0", port=80)
