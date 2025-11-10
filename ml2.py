import pandas as pd
import numpy as np

df=pd.read_csv("emails.csv")
df.columns
df['predictions'].value_counts()
df.shape
df.isnull().sum()
df=df.drop(columns=['Email No.'])


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report

x=df.drop(columns=['Prediction'])
y=df['Prediction']

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.2)

from sklearn.preprocessing import StandardScaler,Normalizer

Sscaler=StandardScaler()
xtr_svm=Sscaler.fit_transform(x_train)
xtest_svm=Sscaler.transform(x_test)

svm_model=SVC(kernel-'linear',class_weight='balanced',random_state=42)
svm_model.fit(xtr_svm,y_train)
svm_pred=svm_model.predict(xtest_svm)
print("accuracy svm:  ",accuracy_score(y_test,svm_pred))

Knormalizer=Normalizer()
xtr_knn=Knormalizer.fit_transform(x_train)
xtest_knn=Knormalizer.transform(x_test)

knn_model=KNeighborsClassifier(n_eighbors=5,metric='euclidean')
knn_model.fit(xtr_knn)
knn_pred=knn_model.predict(knn_)