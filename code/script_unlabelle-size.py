def metricsextr(X1_train,X2_train,X_label,X1,X2):
    metriques_co=[]
    metriques_logistic=[]
    metriques_co.append(["Accuracy","precision","recall","f1"])
    metriques_logistic.append(["Accuracy","precision","recall","f1"])
    fi=len(X1)
    pas=(fi-1000)/10
    k=np.arange(1000,150000, pas)
    for i in range(len(k)):
        X1predict=alea(X1,k[i])
        X2predict=alea(X2,k[i])
        r1,r2=cotrainingfunction(X1_train,X2_train,X_label,X1predict,X2predict)
        metriques_co.append(metricss(r1,r2))
    return metriques_co




def alea(X1,k[i]):
    deb=random.randint(1, (len(X1)-k[i])) 
    j=deb
    Xnew=[]
    while(j<deb+k[i]):
        Xnew.append(X[j])
        j=j+1
    return Xnew


