# Importing essential libraries
import numpy as np
import pandas as pd
import pickle

# Loading the dataset
df = pd.read_csv('dataset/kaggle_diabetes.csv')

# Renaming DiabetesPedigreeFunction as DPF
df = df.rename(columns={'DiabetesPedigreeFunction': 'DPF'})

# Replacing the 0 values from ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'] by NaN
df_copy = df.copy(deep=True)
df_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = df_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)

# Replacing NaN value by mean, median depending upon distribution
df_copy['Glucose'] = df_copy['Glucose'].fillna(df_copy['Glucose'].mean())
df_copy['BloodPressure'] = df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean())
df_copy['SkinThickness'] = df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].median())
df_copy['Insulin'] = df_copy['Insulin'].fillna(df_copy['Insulin'].median())
df_copy['BMI'] = df_copy['BMI'].fillna(df_copy['BMI'].median())

# Model Building
from sklearn.model_selection import train_test_split
X = df_copy.drop(columns='Outcome')  # Ensure 'df_copy' is used for cleaned data
y = df_copy['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

from sklearn.ensemble import RandomForestClassifier
import pickle

# Tạo mô hình mới
classifier = RandomForestClassifier()
# Huấn luyện mô hình với dữ liệu của bạn (thay thế X_train, y_train bằng dữ liệu thực tế)
classifier.fit(X_train, y_train)

# Lưu mô hình
filename = r"C:\Users\ASUS\Desktop\end2end\Diabetes-prediction deployed\diabetes-prediction-rfc-model.pkl"
with open(filename, 'wb') as file:
    pickle.dump(classifier, file)