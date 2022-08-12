import csv
import os
import math
import time
import pydot
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, IncrementalPCA
from sklearn.tree import export_graphviz
from sklearn.model_selection import GridSearchCV, KFold
from pandas.plotting import scatter_matrix
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_curve, recall_score, roc_curve

ratio = round(20/80,2)

start_time = time.time()

df = pd.read_csv('./0.01_0.020/20_80/data/merged.csv')
#fill missing values with 0
df.fillna(0, inplace=True)
print(df['type'].value_counts())
#rename columns as we want
print("Total columns head of original data:", df.columns)
X = df.drop(['id', 'type'], axis=1)
y = df['type']

save_figure = './0.01_0.020/20_80/figures'
if not os.path.exists(save_figure):
    os.makedirs(save_figure)

class TrainwithRandomForest():
    def __init__(self,X, y):
        self.X = X
        self.y = y
    def train_model(self):
        self.X_train,self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)
        # Create the model
        n_estimators = 200
        oob = []
        self.model = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42, oob_score=True)
        for i in range(1, n_estimators +1):
            self.model.set_params(n_estimators=i)
            self.model.fit(self.X_train, self.y_train)
            print ("oob_score:", self.model.oob_score_)
            oob.append(self.model.oob_score_)
        # Make dataframe with oob_score and n_estimators
        self.oob_df = pd.DataFrame({'n_estimators': range(1, n_estimators +1), 'oob_score': oob})
        print(self.oob_df.head())
        # Plot the oob_score vs n_estimators
        plt.figure(figsize=(12,8))
        plt.plot(self.oob_df.n_estimators, self.oob_df.oob_score, label='oob_score')
        plt.legend()
        plt.xlabel('n_estimators')
        plt.ylabel('oob_score')
        plt.savefig('./0.01_0.020/20_80/figures/oob_score.png')
        plt.close()
        

        
        # # Train the model
        # self.model.fit(self.X_train, self.y_train)
        # # Predict on the test data
        self.y_pred = self.model.predict(self.X_test)
        # # Evaluate the model
        print("Accuracy:", accuracy_score(self.y_test, self.y_pred))
        print("F1 score:", f1_score(self.y_test, self.y_pred))
        print("Classification report:")
        print(classification_report(self.y_test, self.y_pred))
    def plot_important_features(self):
        #get first 20 importnat features
        importnat_features = self.model.feature_importances_
        importnat_features_index = np.argsort(importnat_features)
        importnat_features_index = importnat_features_index[::-1]
        importnat_features_index = importnat_features_index[:30]
        importnat_features = importnat_features[importnat_features_index]
        importnat_features_index = self.X.columns[importnat_features_index]
        #plot importnat features
        plt.figure(figsize=(10,10))
        plt.barh(range(len(importnat_features_index)), importnat_features, align='center')
        plt.yticks(range(len(importnat_features_index)), importnat_features_index)
        plt.xlabel('Feature Importance')
        plt.ylabel('Feature')
        plt.savefig('./0.01_0.020/20_80/figures/feature_importance.png')
        plt.close()
    def actual_vs_predicted(self):
        # Plot the confusion matrix
        cm = confusion_matrix(self.y_test, self.y_pred)
        plt.figure(figsize=(10,10))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.title('Confusion matrix')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        plt.savefig('./0.01_0.020/20_80/figures/confusion_matrix.png')
        plt.close()
        # Plot the precision-recall curve
        precision, recall, thresholds = precision_recall_curve(self.y_test, self.y_pred)
        plt.figure(figsize=(10,10))
        plt.plot(recall, precision, label='Precision-Recall curve')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.ylim([0.0, 1.05])
        plt.xlim([0.0, 1.0])
        plt.title('Precision-Recall curve')
        plt.legend(loc="lower left")
        plt.savefig('./0.01_0.020/20_80/figures/precision_recall_curve.png')
        plt.close()
        # Plot the ROC curve
        fpr, tpr, thresholds = roc_curve(self.y_test, self.y_pred)
        plt.figure(figsize=(10,10))
        plt.plot(fpr, tpr, label='ROC curve')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC curve')
        plt.legend(loc="lower left")
        plt.savefig('./0.01_0.020/20_80/figures/roc_curve.png')
        plt.close()
    def dataframe_actual_vs_predicted(self):
        # Create a dataframe with actual vs predicted
        df_actual_vs_predicted = pd.DataFrame({'actual': self.y_test, 'predicted': self.y_pred})
        print(df_actual_vs_predicted)
        print("F1 score:", f1_score(self.y_test, self.y_pred))
        header = ['rotaion', 'f1_score']
        result = [ratio, round(f1_score(self.y_test, self.y_pred), 3)]
        with open ('./0.01_0.020/20_80/result.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerow(result)

    # def classificationReport(self):
    #     self.actual_vs_predicted = pd.DataFrame({'Actual':self.y_test, 'Predicted':self.y_pred})
    #     print(self.actual_vs_predicted.head(10))
    #     self.data = {}
    #     self.data.update({'index':self.X_test.index.values})
    #     self.data.update({'type': self.y_test.values})
    #     self.data.update({'prediction':self.y_pred})
    #     self.data.update({'101000': self.X_test['101000']})
    #     self.data.update({'98000': self.X_test['98000']})
    #     self.data.update({'613000': self.X_test['613000']})
    #     self.data.update({'119000': self.X_test['119000']})
    #     self.data.update({'537000': self.X_test['537000']})
    #     self.data.update({'163000': self.X_test['163000']})
    #     self.data_coutcome = pd.DataFrame(self.data)
    #     self.data_coutcome.to_csv('./0.01_0.020/20_80/result.csv', index=False)
    #     print(self.data_coutcome.head(10))
    #     print("F1 score:", f1_score(self.y_test, self.y_pred))

    def run(self):
        self.train_model()
        self.plot_important_features()
        self.actual_vs_predicted()
        self.dataframe_actual_vs_predicted()
t1 = TrainwithRandomForest(X, y)
t1.run()
