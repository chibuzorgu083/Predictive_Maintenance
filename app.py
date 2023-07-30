from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    type_val = request.form['type']
    air_temp = float(request.form['air_temp'])
    process_temp = float(request.form['process_temp'])
    rotational_speed = float(request.form['rotational_speed'])
    torque = float(request.form['torque'])
    tool_wear = float(request.form['tool_wear'])
    power = float(request.form['power'])

    # Preprocess the features
    if type_val == 'L':
        type_val = 0
    elif type_val == 'M':
        type_val = 1
    elif type_val == 'H':
        type_val = 2

    # Create a feature vector
    features = np.array([type_val, air_temp, process_temp, rotational_speed, torque, tool_wear, power]).reshape(1, -1)

    # Load the trained model
    model = pickle.load(open('model.pkl', 'rb'))

    # Make the prediction
    prediction = model.predict(features)
    if prediction[0] == 1:
        result =  'Equipment Needs Maintenance'
    else:
        result = 'Equipment Does Not Need Maintenance'
    return render_template('result.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)
