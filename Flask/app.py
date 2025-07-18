from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = np.array([features])
    prediction = model.predict(final_features)
    return render_template('result.html', prediction_text=f'Traffic Volume will be {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)