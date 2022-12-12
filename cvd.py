import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


def cvd_prediction(age, gender, height, weight ,ap_hi ,ap_lo ,cholesterol, gluc, smoke, alco, active):
    df=pd.read_csv('cardio_train.csv')
    df=df.drop(['id','age','gender','height'],axis=1)
    y=df['cardio']
    x=df.drop(['cardio'],axis=1)
    from sklearn.linear_model import LogisticRegression
    lr=LogisticRegression()
    lr.fit(x,y)
    xtr,xts,ytr,yts=train_test_split(x,y,test_size=0.25,stratify=y)
    lr.fit(xtr,ytr)
    yp=lr.predict(xts)
    lr.score(xts,yts)
    confusion_matrix(yts,yp)
    print(classification_report(yts,yp))
    y_pred=lr.predict(xts)