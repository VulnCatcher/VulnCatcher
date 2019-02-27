from lxml import etree
import commands
import os
import subprocess
import git 
import csv





def log_extraction(path,nature):
    #processing of the introduced nature variable to know if it is the logs of a commit or a fix
    rep=path+'/commits'
    repertoire=path+'/commits_logs'
    if nature=="commit":
        rep=path+'/commits'
    else:
        if nature=="fix":
            rep=path+'/fixs'
        else:
            print ("Erreur sur la nature des logs à extraire")
            
    # #creation of the directory which will contain the logs
    if (nature=='commit'):
        repertoire=path+'/commits_logs'
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
    # Start of file parsing
    
    for dossier, sous_dossiers, fichiers in os.walk(rep):
        for w in range(len(fichiers)):
            bag= open(repertoire+'/'+fichiers[w]+'.txt', 'a')
            compt=0
            repp=repertoire+'/'+fichiers[w]
            os.makedirs(repp)
            with open(rep+'/'+fichiers[w], 'r') as f:
                i=0
                k=0
                t=f.readlines()
                enre=[]
                while (k<len(t)):
                    temp=""
                    if ("Date: " in t[k]):
                        if("$Date" in t[k]):
                            z=0
                            i=i+1
                        else:
                            i=k
                            #temp=temp+str(t[i])
                            i=i+1
                            j=0
                            compt=compt+1
                            while(j==0):
                                if("diff --" in t[i]):
                                    j=1
                                else:
                                    #print t[i]
                                    dossier = open(repp+'/log-'+str(compt)+'.txt', 'a')
                                    dossier.write(t[i])
                                    bag.write(t[i])
                                i=i+1
                        k=i
                        #print("end")

                    k=k+1
                    commit_empty(repp+'/log')
                    