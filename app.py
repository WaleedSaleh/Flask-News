from flask import Flask, render_template, jsonify
import requests as r

app = Flask(__name__)

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=16016d749e704781988e56c4f384df07')


def get_data():
    res = r.get(url)
    data = res.json()
    data = data['articles']
    return data


@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
