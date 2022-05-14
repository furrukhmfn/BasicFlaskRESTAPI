import pickle
import sklearn
from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'REST API FOR ML MODEL'
@app.route('/predict/<string:n>/<string:s>')
def ml_predict_fun(n,s):
    filename = "final_modal.sav"
    amount_redone = n.replace('$','')
    amount_redone = float(amount_redone)
    if s=='USD':
        currency_redone=1
    else:
        currency_redone=0
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[amount_redone,currency_redone]])
    if result == 1:
        return_result = "REGULAR"
    else:
        return_result = "IRREGULAR"
    result = {
        "Amount":n,
        "Currency":s,
        "Risk Category":return_result
    }
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)
