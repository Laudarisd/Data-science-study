import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
#import class from other files
from models.model_knn import ModelKNN
from models.model_rf import ModelRF
from models.model_decission_tree import DecissionTree
from models.model_svc import ModelSVC
from models.model_gaussiannb import ModelGaussianNB
from models.model_mlp import ModelMLP
from sklearn.preprocessing import LabelEncoder

def main():
    #read data
    df = pd.read_csv('./data/original_csv.csv')
    X = df.drop('class', axis=1)
    y = df['class']
    #conver categorical data to numerical data
    labelencoder = LabelEncoder()
    y = labelencoder.fit_transform(y)
    #normalize data
    X = (X - X.mean()) / X.std()
    #standardize data
    # scaler = StandardScaler()
    # X = scaler.fit_transform(X)
    #replace NaN with 0
    X = X.fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    #knn model
    model_knn = ModelKNN(X_train, y_train, X_test, y_test)
    model_knn.model()
    model_knn.actaul_vs_prediction_dataframe()
    print("#######################################################################")
    #rf model
    model_rf = ModelRF(X_train, y_train, X_test, y_test)
    model_rf.model()
    model_rf.actaul_vs_prediction_dataframe()
    model_rf.feature_importance()
    print("#######################################################################")
    #decision tree model
    model_decision_tree = DecissionTree(X_train, y_train, X_test, y_test)
    model_decision_tree.model()
    model_decision_tree.actaul_vs_prediction_dataframe()
    model_decision_tree.feature_importance()
    print("#######################################################################")
    #svc model
    model_svc = ModelSVC(X_train, y_train, X_test, y_test)
    model_svc.model()
    model_svc.actaul_vs_prediction_dataframe()
    print("#######################################################################")
    #model GaussianNB
    model_gaussiannb = ModelGaussianNB(X_train, y_train, X_test, y_test)
    model_gaussiannb.model()
    model_gaussiannb.actaul_vs_prediction_dataframe()
    print("#######################################################################")
    #model mlp
    model_mlp = ModelMLP(X_train, y_train, X_test, y_test)
    model_mlp.model()
    model_mlp.actaul_vs_prediction_dataframe()
    print("#######################################################################")

if __name__ == '__main__':
    main()
 
