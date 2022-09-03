import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')



#make class for model

class ModelKNN:
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
    def model(self):
        #train model
        #knn = KNeighborsClassifier(n_neighbors=5)
        knn = KNeighborsClassifier(n_neighbors=5, 
                            weights='uniform', 
                            algorithm='auto', 
                            leaf_size=30, 
                            p=2, 
                            metric='minkowski', 
                            metric_params=None, 
                            n_jobs=None)
        knn.fit(self.X_train, self.y_train)
        #predict
        self.y_pred = knn.predict(self.X_test)
        #evaluate model
        print('Accuracy: ', accuracy_score(self.y_test, self.y_pred))
        print('F1 score: ', f1_score(self.y_test, self.y_pred, average='weighted'))
        print('Confusion matrix: ', confusion_matrix(self.y_test, self.y_pred))
        print('Classification report: ', classification_report(self.y_test, self.y_pred))
    def actaul_vs_prediction_dataframe(self):
        #create dataframe to compare actual vs predicted
        self.df = pd.DataFrame({'Actual': self.y_test, 'Predicted': self.y_pred})
        print(self.df)
    
        