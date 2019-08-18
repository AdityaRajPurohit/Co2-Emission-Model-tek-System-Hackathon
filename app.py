import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open(f'model/Co2_emission.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        ENGINESIZE = flask.request.form['ENGINESIZE']
        CYLINDERS = flask.request.form['CYLINDERS']
        FUELCONSUMPTION_COMB = flask.request.form['FUELCONSUMPTION_COMB']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[ENGINESIZE, CYLINDERS, FUELCONSUMPTION_COMB]],
                                       columns=['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={'ENGINESIZE':ENGINESIZE,
                                                     'CYLINDERS':CYLINDERS,
                                                     'FUELCONSUMPTION_COMB':FUELCONSUMPTION_COMB},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()