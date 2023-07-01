from flask import Flask , render_template


app = Flask(__name__)

@app.route("/bootstrap")
def Anuj():
    return render_template("bootstrap.html")
# app.run(debug=True)
@app.route("/tude3")
def anuj():
    return render_template("tude3.html")
@app.route("/form")
def Form():
    return render_template("form.html")
app.run(debug=True)