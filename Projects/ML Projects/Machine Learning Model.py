import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
# data = pd.read_csv('data.csv') #Use This 
data = pd.read_csv(r'D:\Visual Stdio\Python Practice\Projects\ML Projects\data.csv')  # Ensure you have a dataset

# Define features and target
X = data[['feature1', 'feature2']]  # Replace with actual feature names
y = data['target']  # Replace with the actual target name

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Predictions:", predictions)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
