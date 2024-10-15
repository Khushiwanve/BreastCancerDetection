import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset (Make sure to have a CSV file with appropriate features and labels)
data = pd.read_csv('path_to_your_dataset.csv')

# Assume 'label' is the column name for tumor classification
# Features (you can change the feature names based on your dataset)
features = data.drop('label', axis=1)
labels = data['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model to a file
with open('model/cancer_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
