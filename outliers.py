# Pour les outliers (valeur abérante) il faut un dataset avec des valeurs quantitative int ou float;
# Selectionner à la question show or delete, repondre "show" pour voir les valeurs abérante et delete si on veut les supprimer du dataset.
import pandas as pd 
def outliers(data):
    global show
    global count
    global delete
    q1=data.quantile(q=0.25)
    q3=data.quantile(q=0.75)
    IQR=q3-q1
    borne_inf = q1-1.5*IQR  
    borne_sup = q3 +1.5*IQR
    show_inf = borne_inf.dropna()
    show_sup = borne_sup.dropna()
    count = data[data > borne_sup].count() + data[data < borne_inf].count()
    delete = data[(data < borne_sup) & (data > borne_inf)]
    choice = ""
    while choice != "exit":
        choice = input("show, count or delete outliers ? (help to understand choices)")
        if choice == "show":
            print("les valeurs abérantes inferieur:\n", show_inf, "\nles valeurs abérantes supérieur:\n", show_sup)
        elif choice == "count":
            print("le nombre de valeurs abérantes est de:\n", count)
        elif choice == "delete":
            print("le dataset est maintenant supprimé des valeurs abérantes; \n", pd.DataFrame(delete))
        else: 
            print("please choose show, count or delete or exit ")
