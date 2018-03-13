#1. Import Flask
from flask import Flask
from flask import render_template #will render html pages in route

#Create app variable
app = Flask(__name__)

#Create a route. You have to define what you want to automatically run
@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/contact")
def about():
    return render_template("contact.html")

@app.route("/attorneys")
def contact():
    return render_template("attorneys.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/where")
def where():
    return render_template("where.html")

@app.route("/who")
def who():
    return render_template("who.html")


app.run(debug=True, host="0.0.0.0", port=8081)