from flask import Flask, render_template, request,redirect,url_for
import pickle

#app = Flask(__name__)
app=Flask(__name__,template_folder='templates')
# Load the model from the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
#@app.route('/predict/')
def predict():
    fertilizer_amount = float(request.form['fertilizer'])
    water_amount = float(request.form['water'])

    # Make a prediction using the loaded model
    prediction = model.predict([[fertilizer_amount, water_amount]])

    #return render_template('index.html', predict="the answer is {}".format(prediction))
    return render_template('result.html', prediction=int(prediction[0]))

if __name__ == '__main__':    
    app.run(debug="True")
