from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze")
def register():
    data = request.args.get("data")
    data_length = len(data)
    word_list = data.split()
    word_count = len(word_list)

    reverse_data = data[::-1]
    return render_template("analyze.html", data = data, word_count=word_count, data_length = data_length, word_list=word_list, reverse_data=reverse_data)
