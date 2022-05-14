import pickle
import sklearn
def ml_predict_fun(amount,currency):
    filename = "final_modal.sav"
    amount_redone = amount.replace('$','')
    amount_redone = float(amount_redone)
    if currency=='USD':
        currency_redone=1
    else:
        currency_redone=0
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[amount_redone,currency_redone]])
    if result == 1:
        return_result = "REGULAR"
    else:
        return_result = "IRREGULAR"
    return return_result