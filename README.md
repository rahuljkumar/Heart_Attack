Heart attack prediction:
This machine learning model is to classify whether a patient has the risk of getting a heart attack or not using inputs such as age, gender, cholesterol, heart rate, etc

I have performed extensive EDA over the dataset and inferred a lot of insights.
I have used multiple machine learning algorithms for training and have chosen the CatBoostClassifier model as the best model since it has given an accuracy of 93%. The entire notebook can be accessed from notebook(folder)->modeltrain.ipynb file.

I have containerized the entire code into modules ready for deployment in production. All the containerized code can be accessed from the src folder.
I have used Flask API to consume the model using a webpage. The entire code can be accessed in the app.py file in the main folder.
