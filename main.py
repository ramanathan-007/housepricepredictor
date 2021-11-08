import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd

dataset =pd.read_csv('bhp.csv')
df2 = dataset.drop(['location','size','price'],axis='columns')
df2['price_per_sqft'] = (df2['price_per_sqft']*df2['total_sqft'])/100000
print(df2)


df2['bhk'].fillna(df2['bhk'].mean(), inplace=True)

X = df2.iloc[:, :3]

y = df2.iloc[:, -1]

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X,y)

pickle.dump(regressor, open('main.pkl','wb'))

main = pickle.load(open('main.pkl','rb'))
print(main.predict([[2000.0, 3.0, 2]]))
