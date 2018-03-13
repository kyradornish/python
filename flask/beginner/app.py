#1. Import Flask
from flask import Flask
from flask import render_template #will render html pages in route

#Create app variable
app = Flask(__name__)

#Create a route. You have to define what you want to automatically run
@app.route("/")
def index():#this is how you connect the python page to html
    context = {"name": "Kyra"}
    return render_template("index.html", **context) #string is page we want to route to

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True, host="0.0.0.0", port=8080)
