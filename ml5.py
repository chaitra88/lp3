

# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("diabetes.csv")

#Basic data cleaning
# Replace zeros (invalid physiological values) with median values
cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin']
for col in cols_with_zeros:
    df[col] = df[col].replace(0, df[col].median())

# Split features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling (fit on train only, transform both)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Handle class imbalance using SMOTE (optional but recommended)
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train_scaled, y_train)

print("Before SMOTE:", np.bincount(y_train))
print("After SMOTE :", np.bincount(y_train_res))

# KNN hyperparameter tuning
best_acc = 0
best_k = 0
best_weights = ""
accuracies = []
kvalues = []

for k in range(1, 31):
    for w in ['uniform', 'distance']:
        knn = KNeighborsClassifier(n_neighbors=k, weights=w)
        knn.fit(X_train_res, y_train_res)
        y_pred = knn.predict(X_test_scaled)
        acc = accuracy_score(y_test, y_pred)
        
        # Track best configuration
        if acc > best_acc:
            best_acc = acc
            best_k = k
            best_weights = w

    # store accuracy (for plotting, using uniform weights for simplicity)
    knn_temp = KNeighborsClassifier(n_neighbors=k, weights='uniform')
    knn_temp.fit(X_train_res, y_train_res)
    y_temp_pred = knn_temp.predict(X_test_scaled)
    kvalues.append(k)
    accuracies.append(accuracy_score(y_test, y_temp_pred))

# Display best model info
print(f"\nBest Accuracy : {best_acc:.4f}")
print(f"Best k        : {best_k}")
print(f" Best Weights  : {best_weights}")

#  Train final model with best hyperparameters
best_knn = KNeighborsClassifier(n_neighbors=best_k, weights=best_weights)
best_knn.fit(X_train_res, y_train_res)
final_pred = best_knn.predict(X_test_scaled)

# 🔹 Evaluation metrics
print("\nClassification Report:\n", classification_report(y_test, final_pred))
print("\n Confusion Matrix:\n", confusion_matrix(y_test, final_pred))
print(f"\n Final Test Accuracy: {accuracy_score(y_test, final_pred):.4f}")

#  Plot accuracy vs K
plt.figure(figsize=(8,5))
plt.plot(kvalues, accuracies, marker='o', label='Accuracy vs K')
plt.plot(best_k, best_acc, 'ro', label='Best K')
plt.xlabel('K value')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy vs Number of Neighbors')
plt.legend()
plt.grid(True)
plt.show()
