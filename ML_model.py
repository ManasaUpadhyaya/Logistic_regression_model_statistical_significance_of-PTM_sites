import pandas as pd
import numpy as np
from sklearn import preprocessing
import math
from sklearn.preprocessing import StandardScaler

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

data_model = pd.read_csv("Final_table.csv")
#sns.countplot(data_model, x="Known at the PTM-ID level", palette='hls')
'''
Dropping the unwanted columns 
'''
data_model.drop(['Column 1', 'Unnamed: 0.2', 'Unnamed: 0.1', 'Unnamed: 0', 'IPR-AP', 'IPR','Sum(OBSrc) agg PTM-ID level','PTM-ID', 'UID-NP', 'UID', 'Resi', 'ptm_type', 'per_PRC', 'UID_2','Sum(KFSC) agg PTM-ID level'], axis=1, inplace=True)

'''
The dependent variable is the Known PTM ID column - 1 or 0.
X is the every other column other than Known PTM ID 
'''
X = data_model.loc[:, data_model.columns != 'Known at the PTM-ID level']
y = data_model.loc[:, data_model.columns == 'Known at the PTM-ID level']

'''
SMOTE is used for oversampling of the training data only to remove imbalance of minor data (1 Known PTM ID in this case)

'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
columns = X_train.columns
os = SMOTE(random_state=42)
os_data_X,os_data_y=os.fit_resample(X_train,y_train)
# print("length of oversampled data is ",len(os_data_X))
# print("Number of Known PTMS in oversampled data",len(os_data_y[os_data_y['Known at the PTM-ID level']==1.0]))
# print("Number of subscription",len(os_data_y[os_data_y['Known at the PTM-ID level']== 0.0]))
'''
Recursive feature elimination - The model decides the best columns to predict the value of the y variable
The function RFE returns a false true array for the X variables. The true columns are used to further build the model
'''
data_final_vars=data_model.columns.values.tolist()
y=['y']
X=[i for i in data_final_vars if i not in y]
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='lbfgs', random_state=0, max_iter=100)
rfe = RFE(logreg,step=20)
print(os_data_X.columns.values)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)

# #final_cols = ['Number_of_motifs','Average_eval','Maximum_eval',
#  'Minimum_eval','Obsc_ranks', 'Motif_ranks']
'''
The logistic regression model is built, and the result summary is displayed 
The next snippet shows the classification summary for the accuracy of both 1 and 0 values
'''
numeric=['Number_of_motifs','Maximum_eval','Obsc_ranks', 'Motif_ranks', 'Average_eval']
sc= StandardScaler()
X_train[numeric]=sc.fit_transform(X_train[numeric])
X_test[numeric]=sc.transform(X_test[numeric])
X=os_data_X[numeric]
y=os_data_y['Known at the PTM-ID level']

import statsmodels.api as sm
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary2())

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
'''
Building the ROC curve with the roc_curve function from sklearn
'''
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()


