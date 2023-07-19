#code1
'''import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
data = pd.read_csv('data.csv')  # Replace 'crop_data.csv' with your dataset filename

# Split the data into features (X) and target variable (y)
X = data[['fertilizer', 'water']]
y = data['yield']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("Training Score:", train_score)
print("Testing Score:", test_score)

# Save the model as a pickle file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)'''
#code2
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv("data.csv")

# Create the model
model = LinearRegression()

# Train the model
model.fit(data[["fertilizer", "water"]], data["yield"])

# Make predictions
y_pred = model.predict(data[["fertilizer", "water"]])
#print(y_pred)
# Evaluate the model
print("R-squared:", model.score(data[["fertilizer", "water"]], data["yield"]))
#print(data.head())