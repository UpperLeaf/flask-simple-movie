import requests
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route("/")
def form():
  movies = requests.get("http://movie-api/ns_movies/movies").json()
  movie_list = list(movies["movies"].values())
  return render_template("index.html", movies=movie_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)