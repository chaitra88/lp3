import numpy as np
import pandas as pd

df = pd.read_csv("/content/Churn_Modelling.csv")

df.head()

df = df.drop(['CustomerId','Surname','RowNumber'],axis=1)

df.info()

df = pd.get_dummies(df,drop_first=True)

X = df.drop('Exited', axis=1)

y = df['Exited']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from imblearn.over_sampling import SMOTE
smote = SMOTE(sampling_strategy=0.4, random_state = 42)
X_train, y_train = smote.fit_resample(X_train, y_train)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
model = Sequential()
model.add(Dense(32, activation='relu',input_shape=(X_train.shape[1],)))
model.add(Dropout(0.2))
model.add(Dense(16,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1,activation='sigmoid'))

from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])

class_weight = {0: 1, 1: 2}

history = model.fit(X_train,y_train, epochs = 50, batch_size = 32, validation_split=0.2, callbacks=[early_stop],class_weight=class_weight)

y_prob = model.predict(X_test)
threshold = 0.50
y_pred = (y_prob > threshold).astype(int)

from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


import matplotlib.pyplot as plt
import seaborn as sns

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title("Model Accuracy")
plt.legend()

plt.show()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title("Model Loss")
plt.legend()
plt.show()