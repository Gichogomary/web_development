from flask import Flask,render_template
app = Flask(__name__)
@app.route("/about")
def about():
    return "this is about page" 
    return render_template("index.html")