import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv('my_data.csv')
feature_cols = ['delta_v', 'direction_of_force', 'adj_passenger', 'multiple_events', 'belt_usage', 'age', 'gender']
target_col = 'ISP'

# Convert 'ISP' into binary classification problem
df['ISP'] = df['ISP'].apply(lambda x: 1 if x > 15 else 0)

df['belt_usage'] = df['belt_usage'].astype(int)

X = df[feature_cols]
y = df[target_col]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
