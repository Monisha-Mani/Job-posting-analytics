# Import Required Libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from xgboost import XGBClassifier


# Load Final Engineered Dataset

df = pd.read_csv(
    "../data/cleaned/final_engineered_jobs_dataset.csv",
    low_memory=False
)

print(df.head())


# Remove Missing Role Values

df = df.dropna(subset=["standardized_role"])

print(df.shape)


# Remove Generic Others Category

df = df[df["standardized_role"] != "Others"]

print(df["standardized_role"].value_counts())


# Select Features For Prediction

features = [
    "python_flag",
    "sql_flag",
    "power_bi_flag",
    "tableau_flag",
    "excel_flag",
    "selenium_flag",
    "aws_flag",
    "azure_flag",
    "gcp_flag",
    "java_flag",
    "spark_flag",
    "hadoop_flag",
    "docker_flag",
    "kubernetes_flag",
    "jira_flag",
    "jenkins_flag",
    "rest_api_flag",
    "testng_flag",
    "power_apps_flag",
    "minimum_experience",
    "maximum_experience",
    "total_skills"
]

X = df[features]

y = df["standardized_role"]


# Fill Missing Values

X = X.fillna(0)

print(X.head())


# Encode Target Labels

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

print(label_encoder.classes_)


# Split Training And Testing Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

print("Training Data Shape:", X_train.shape)

print("Testing Data Shape:", X_test.shape)


# Train XGBoost Model

model = XGBClassifier(
    n_estimators=200,
    max_depth=8,
    learning_rate=0.1,
    random_state=42,
    eval_metric="mlogloss"
)

model.fit(X_train, y_train)

print("XGBoost Model Training Completed")


# Predict Job Roles

y_pred = model.predict(X_test)

print(y_pred[:10])


# Evaluate Model Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)


# Generate Classification Report

report = classification_report(
    y_test,
    y_pred,
    target_names=label_encoder.classes_
)

print(report)


# Generate Confusion Matrix

matrix = confusion_matrix(y_test, y_pred)

print(matrix)


# Feature Importance Analysis

feature_importance = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
})

feature_importance = feature_importance.sort_values(
    by="importance",
    ascending=False
)

print(feature_importance)


# Save Prediction Insights

feature_importance.to_csv(
    "../data/cleaned/job_role_feature_importance.csv",
    index=False
)

print("Job Role Prediction Completed Successfully")