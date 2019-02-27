import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
import os
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

#treatment of the introduced nature variable to know if it is a commit or a fix log
def bagofword(path,nature):
    rep=path+'/commits'
    repertoire=path+'/bagofw'
    if nature=="commit":
        rep=path+'/commits'
    else:
        if nature=="fix":
            rep=path+'/fixs'
        else:
            print ("Erreur sur la nature des logs à extraire")
            
# #creation of the directory that will contain the logs
    if (nature=='commit'):
        repertoire= path+'/commits_logs'
        try: 
            os.makedirs(repertoire)
        except OSError:
            if not os.path.isdir(repertoire):
                Raise
    if (nature=='fix'):
        repertoire=path+'/fixs_logs'
        try: 
            os.makedirs(repertoire)
        except OSError:
            if not os.path.isdir(repertoire):
                Raise
    try: 
        os.makedirs(path+'/csv/logs')
    except OSError:
        if not os.path.isdir(path+'/csv/logs'):
            Raise
# Start of file parsing
    for dossier, sous_dossiers, fichiers in os.walk(repertoire):
        s=sous_dossiers
        for w in range(len(s)):
            filename=s[w]
            #print sous_dossiers[w]
            sentences = open(repertoire+'/'+filename+'.txt', 'r')
            #fitting de toutes les données du dictionaire 
            transformer = TfidfTransformer()
            vectorizer = TfidfVectorizer(encoding="utf-8",min_df=0.0,analyzer = "word", tokenizer = None, lowercase= "True",preprocessor = None, stop_words = "english" , max_features = 100,use_idf="True") 
            train_data_features = vectorizer.fit_transform(sentences)
            transformer.fit(vectorizer.idf_)
            print vectorizer.vocabulary_
            
            for dossier, sous_dossiers, fichiers in os.walk(repertoire+'/'+filename):
                
                for j in range(len(fichiers)):
                    dc= open(dossier+'/'+fichiers[j], 'r')
                    charac1=vectorizer.transform(dc).toarray()
                    tfidf = transformer.fit_transform(charac1)
                    c = csv.writer(open(path+'/csv/logs/'+filename+'.csv', "a"))
                    c.writerow(transformer.idf_)
                    
                ##################################################################################
     