from flask import *
from flask_cors import CORS,cross_origin
import pickle
from features import *
import inputScript
import pickle
import requests
import json

app = Flask(__name__) # initializing a flask app
app.secret_key = "fuga"
@app.route('/',methods=['GET']) # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")
    
    
@app.route('/offline',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def offline():
    if request.method == 'POST':
        try:
            web_data=request.form['data']
            print(web_data)
            data = web_data.split(",")
            filename = 'DecisionTree.pickle.dat'
            loaded_model_d = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction_d=loaded_model_d.predict([data])
            d = prediction_d[0]
            print('prediction is', prediction_d[0])
            
            
            filename = 'RandomForest.pickle.dat'
            loaded_model_r = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction_r=loaded_model_r.predict([data])
            r = prediction_r[0]
            print('prediction is', prediction_r[0])
            
            checker = {1:"PHISHING WEBSITE",0:"LEGITIMATE WEBSITE"}
            
            return render_template('offline.html', pred_d=checker[d], pred_r=checker[r] )
        except Exception as e:
            print('The Exception message is: ',e)
            E_message = f"{str(e)}"
            flash(E_message, 'error')
            return redirect(url_for("error"))
    # return render_template('results.html')
    else:
        return render_template('offline.html')
        
@app.route('/error')
def error():
    
    return render_template('error.html')

@app.route('/online',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def online():

    if request.method == 'POST':
        try:
            url = request.form['url']
            print(url)
            URLfeatures = inputScript.main(url)
          
            api ='http://1079582b-459b-41f0-9e68-c2d6b3f2cf55.eastus2.azurecontainer.io/score'

            data = {
                "data": URLfeatures,
                "method": "predict" 
            }

            headers = {'Content-Type': 'application/json'}

            r = requests.post(api, str.encode(json. dumps (data)), headers = headers) 
            s = r.json()
            predicted_value = s['predict']

            print(predicted_value)
            
                 
            if predicted_value == 1:
                value = "Legitimate"
                return render_template("home.html",error=value)
            if predicted_value == -1:
                 value = "Phishing"
                 return render_template("home.html",error=value)
            
            
            
            return render_template('online.html', pred_d=value )
            #return render_template('online.html', pred_d =d, pred_r =r ,link=web_link )
            
        
           
        except Exception as e:
            print('The Exception message is: ',e)
            
            E_message = f"{str(e)}"
            flash(E_message, 'error')
            return redirect(url_for("error"))
    # return render_template('results.html')
    else:
        return render_template('online.html')
        
        
if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=False) # running the app
    
    
