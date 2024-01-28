Heart attack prediction:

This machine learning model is to classify whether a patient has the risk of getting a heart attack or not using inputs such as age, gender, cholesterol, heart rate, etc.

I have performed extensive EDA over the dataset.

I have used multiple machine learning algorithms for training and have chosen the CatBoostClassifier model as the best model since it has given an accuracy of 93%. The entire notebook can be accessed from notebook (folder)->modeltrain.ipynb file.

I have modularized the entire code ready for deployment in production. All the modules can be accessed from the src folder.

I have used Flask API to consume the model using a webpage. The entire code can be accessed in the app.py file in the main folder.

Setup.py: Gets the list of libraries from requirements.txt and includes them as installation dependencies. It also creates out project as a Py package.

App.py: Flask web app

Utils.py: Functions to pickle and unpickle the model and the scaler are defined here. The evaluation methods is also written here.

Data_ingestion.py: Reads the CSV file, creates train test split and stores the split dataframes as csv file. Calls the methods for data transformation and model training

Data_transformation.py: Pipeline for scaling, data transformation are defined. The Scaler is pickled in this file. Reads the train and test csv files and does scaling and returns the scaled dataset.

Model_trainer.py: Has the method for model training. Splits the dataset into Dependent and Independent variables. Performs model training and evaluation. Model is pickled here.

Predict_pipeline.py: Takes input from users through web app, loads the model and scalers from pickled files, transforms the input using preprocessor and uses the model to predict the output.



