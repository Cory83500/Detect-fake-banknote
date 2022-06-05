import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# Pour data, il faut un format csv, a 6 colonnes quantitative sans valeur manquantes. 
# Coder simplement data = pd.read_csv("votrefichier.csv")
# Puis vérifier bien qu'il n'y ait que 6 colonnes est que se soit des colonnes quantitatives.
def detection(data):
    billet = pd.read_csv("billet_finish.csv")
    y = billet["is_genuine"] # Target
    X = billet.drop(["is_genuine"],axis=1) # Features
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    pred =model.predict(data)
    proba = model.predict_proba(data)
    data["prediction"] = pred
    proba = proba[:,1]
    data['proba'] = proba*100
    return data