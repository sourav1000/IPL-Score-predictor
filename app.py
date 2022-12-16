# importing the libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load Lasso Regression model
filename = './Batting-score-LassoReg-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)               

# ****************HOME ROUTE********************
@app.route("/")
def home():
    return render_template('index.html')

# ****************PREDICT ROUTE*****************
@app.route("/predict", methods=['POST'])
def predict():
    feature_aaray = list()

    if request.method == 'POST':
        
        data = construct_feature_array(request.form)

        my_prediction = int(regressor.predict(data)[0])
        
              
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)

if __name__ == '__main__':
	app.run(debug=True)

# function for making the np array for prediction
def construct_feature_array(form_data):
    feature_array = list()

    runs = int(form_data['runs'])
    overs = float(form_data['overs'])
    wickets = int(form_data['wickets'])
    runs_in_prev_5 = int(form_data['runs_in_prev_5'])
    wickets_in_prev_5 = int(form_data['wickets_in_prev_5'])

    feature_array += [runs,wickets,overs,runs_in_prev_5,wickets_in_prev_5,1]

    batting_team = form_data['batting-team']

    feature_array += [0,0,0,0,0,0,0,0]
    
    if batting_team == 'Chennai Super Kings':
        feature_array[5] = 1
    elif batting_team == 'Delhi Daredevils':
        feature_array[6] = 1
    elif batting_team == 'Kings XI Punjab':
        feature_array[7] = 1
    elif batting_team == 'Kolkata Knight Riders':
        feature_array[8] = 1
    elif batting_team == 'Mumbai Indians':
        feature_array[9] = 1
    elif batting_team == 'Rajasthan Royals':
        feature_array[10] = 1
    elif batting_team == 'Royal Challengers Bangalore':
        feature_array[11] = 1
    elif batting_team == 'Sunrisers Hyderabad':
        feature_array[12] = 1

    bowling_team = form_data['bowling-team']

    feature_array += [0,0,0,0,0,0,0,0]

    if bowling_team == 'Chennai Super Kings':
        feature_array[13] = 1
    elif bowling_team == 'Delhi Daredevils':
        feature_array[14] = 1
    elif bowling_team == 'Kings XI Punjab':
        feature_array[15] = 1
    elif bowling_team == 'Kolkata Knight Riders':
        feature_array[16] = 1
    elif bowling_team == 'Mumbai Indians':
        feature_array[17] = 1
    elif bowling_team == 'Rajasthan Royals':
        feature_array[18] = 1
    elif bowling_team == 'Royal Challengers Bangalore':
        feature_array[19] = 1
    elif bowling_team == 'Sunrisers Hyderabad':
        feature_array[20] = 1
    
    venue = form_data['venue']

    feature_array += [0,0,0,0,0,0,0,0]

    if venue == 'Eden Gardens':
        feature_array[21] = 1
    elif venue == 'Feroz Shah Kotla':
        feature_array[22] = 1
    elif venue == 'M Chinnaswamy Stadium':
        feature_array[23] = 1
    elif venue == 'MA Chidambaram Stadium, Chepauk':
        feature_array[24] = 1
    elif venue == 'Punjab Cricket Association Stadium, Mohali':
        feature_array[25] = 1
    elif venue == 'Rajiv Gandhi International Stadium, Uppal':
        feature_array[26] = 1
    elif venue == 'Sawai Mansingh Stadium':
        feature_array[27] = 1
    elif venue == 'Wankhede Stadium':
        feature_array[28] = 1
    
    data = np.array([feature_array])

    return data
