import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')


#make class for model

class ModelRF:
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
    def model(self):
        #train model
        self.rf = RandomForestClassifier(n_estimators=100,
                                criterion='gini', 
                                max_depth=None, 
                                min_samples_split=2, 
                                min_samples_leaf=1, 
                                min_weight_fraction_leaf=0.0, 
                                max_features='auto', 
                                max_leaf_nodes=None, 
                                bootstrap=True, 
                                oob_score=False, 
                                n_jobs=None, 
                                random_state=None, 
                                verbose=0, 
                                warm_start=False, 
                                class_weight=None)
        self.rf.fit(self.X_train, self.y_train)
        #predict
        self.y_pred = self.rf.predict(self.X_test)
        #evaluate model
        print("Random Forest")
        print('Accuracy: ', accuracy_score(self.y_test, self.y_pred))
        print('F1 score: ', f1_score(self.y_test, self.y_pred, average='weighted'))
        print('Confusion matrix: ', confusion_matrix(self.y_test, self.y_pred))
        print('Classification report: ', classification_report(self.y_test, self.y_pred))
    def actaul_vs_prediction_dataframe(self):
        #create dataframe to compare actual vs predicted
        self.df = pd.DataFrame({'Actual': self.y_test, 'Predicted': self.y_pred})
        print(self.df)
    def feature_importance(self):
        #get feature importance
        self.feature_importances = pd.DataFrame(self.rf.feature_importances_,
                                   index = self.X_train.columns,
                                    columns=['importance']).sort_values('importance', ascending=False)
        print(self.feature_importances)