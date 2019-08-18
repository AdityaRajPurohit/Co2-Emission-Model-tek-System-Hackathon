# Co2-Emission-Model-tek-System-Hackathon
Tek System Hackathon

<b>Solution</b>
The solution for the problem can be, if we can find the CO2 emissions of vehicles and give a approx. value for a set of data of vehicle emissions dependencies like Engine Size, No. of cylinders, Fuel Consumption of the vehicle etc.

Here we tried to find out the most accurately possible value of the CO2 emissions based on the similar dependencies. The result will be a value of CO2 emission for the set of values given by the user, based on Engine Size, No. of cylinders, Fuel Consumption of the vehicle. A Machine Learning model is used to predict the result value. And the same model is integrated with a Python code. Also, an interactive and responsive website is made to use of the model easily. The website is deployed on Heroku to give a complete user experience.

This solution will help the concerned government authorities to check a measure on how the CO2 emissions of vehicle varies with different vehicles. The government can use this solution to find out a moderate range of values of attributes which are responsible for the CO2 emissions in a vehicle, and they can take action by putting a limit on the usages of these attributes (Engine Size, No. of cylinders, Fuel Consumption of the vehicle) and can ask the car manufacturers to make a vehicle under the limit of predefined values.

The vehicle manufacturers can directly take advantage of this model. It will help them know the CO2 emissions of a vehicle before-hand. It will save the money wastage by making a vehicle within the defined limits.

<b>Machine Learning Model:</b>
Data analysis and pre-processing is done on the dataset. Using a machine learning algorithm (XGBoost) the prediction output is obtained. Pickle is used to save the trained classifier model to disk. The prediction obtained is 96% accurate. 

<b>Python:</b>
Flask Library is used to integrate the machine learning model. The python code will activate the html file which is used to take inputs and display the output provided by the Machine learning algorithm. And using panda library the input is converted into a data-frame and then passed to the ML model.

<b>Web:</b>
A responsive web page is made using HTML and CSS. In CSS using MEDIA QUERY the website is made compatible to all screen ratio & sizes. This website is deployed using a python code on Heroku and can be accessed on this url: https://co2emi.herokuapp.com/

<b>Deployment:</b>
Heroku is used to deploy the website. And the python script will be deployed on the server because Heroku doesn’t allow to run a static website (HTML). The python code deployed on Heroku will activate the machine learning model and will show the result on the website created. 


