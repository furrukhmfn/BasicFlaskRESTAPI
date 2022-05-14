from flask import Flask, render_template, request
from ml_predict_fun import ml_predict_fun

app = Flask(__name__)

# Main File
@app.route("/hi")
def hello():
    return render_template("index.html")


# Sub FIle 
@app.route("/sub", methods=["POST"])
def submit():
    if request.method == "POST":
        amount = request.form['amount']
        currency = request.form['currency']
        risk_cat = ml_predict_fun(amount,currency)
    return render_template("sub.html", n = risk_cat )


if __name__ == "__main__":
    app.run(debug=True)