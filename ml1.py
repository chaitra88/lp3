df=pd.read_csv("uber.csv")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df.head()
df.columns
df.isnull().sum()

df=df[(df['passenger_count']>=0) & (df['passenger_count']<=6)]
df=df[(df['fare_amount']>=0) & (df['fare_amount']<=200)]
df=df[(df['pickup_latitude']>=40.5) & (df['pickup_latitude']<=40.9)]
df=df[(df['pickup_longitude']>=-74.255) & (df['pickup_longitude']<=-73.7)]
df=df[(df['dropoff_latitude']>=40.5) & (df['dropoff_latitude']<=40.9)]
df=df[(df['dropoff_longitude']>=-74.25) & (df['dropoff_longitude']<=-73.7)]

df.shape

def haversine(lat1,lon1,lat2,lon2):
    lat1,lon1,lat2,lon2=map(np.radians,[lat1,lon1,lat2,lon2])
    dlat=lat2-lat1
    dlon=lon2-lon1
    a=(np.sin(dlat/2)**2)+(np.cos(lat1)*np.cos(lat2)*(np.sin(dlon/2)**2))
    c=2*np.arcsin(np.sqrt(a))
    r=6371
    return c*r

df['distance_km']=haversine(df['pickup_latitude'],df['pickup_longitude'],df['dropoff_latitude'],df['dropoff_longitude'])
df=df[(df['distance_km']>=0)]

df['pickup_datetime']=pd.to_datetime(df['pickup_datetime'])
df['hour']=df['pickup_datetime'].dt.hour
df['day_of_week']=df['pickup_datetime'].dt.day_of_week
df['month']=df['pickup_datetime'].dt.month
df['year']=df['pickup_datetime'].dt.year

sns.scatterplot(data=df, x='distance_km', y='fare_amount', alpha=0.5)
plt.title("Fare vs Distance")
plt.show()

sns.boxplot(data=df, x='passenger_count', y='fare_amount')
plt.title("Fare vs Passenger Count")
plt.show()


sns.barplot(data=df, x='day_of_week', y='fare_amount', estimator='mean')
plt.title("Average Fare by Day of Week")
plt.show()

features=['fare_amount','distance_km','passenger_count','year','month','day_of_week','hour']
corr_matrix=df[features].corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')

feats=['distance_km','hour','day_of_week','month','passenger_count']
x=df[feats]
y=df['fare_amount']

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

lin_model=LinearRegression()
lin_model.fit(x_train,y_train)
lin_preds=lin_model.predict(x_test)

print("--------r2_score regression-------- ",r2_score(y_test,lin_preds))
print()
print("-------accuracy rmse score--------- ",np.sqrt(mean_squared_error(y_test,lin_preds)))

rand_model=RandomForestRegressor(n_estimators=50,n_jobs=-1,random_state=42,max_depth=10)
rand_model.fit(x_train,y_train)
rand_preds=rand_model.predict(x_test)

print("--------r2_score rand_forest-------- ",r2_score(y_test,rand_preds))
print()
print("-------accuracy rmse score--------- ",np.sqrt(mean_squared_error(y_test,rand_preds)))