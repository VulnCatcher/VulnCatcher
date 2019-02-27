

from lxml import etree
import commands
import os
import subprocess
import git 

i=0
repo = git.Repo('path OpenSSL')
gitt = repo.git
with open('path/file.txt', 'r') as f:
    for line in f.readlines():
        ch,fin=line.split("\n")
        #print ch
        dat = gitt.show(ch, pretty="fuller",date="iso")
        myFile = open("/home/delwende/Documents/compare/opensssl-hash", 'a')
        myFile.write(dat.encode('utf-8'))
        myFile.write("\n")
        myFile.write("End-of-patch")
        myFile.write("#### ####################end of patch##############################################")
        myFile.write("###################################################################################")
        myFile.write("\n")
        i=i+1

def date_extraction(path):
    with open(path, 'r') as f:
        t=f.readlines()
        k=0
        AuthorDate=[]
        CommitDate=[]
        date=[]
        temp=0
        while (k<len(t)):
            if "AuthorDate" in t[k]:
                if "$Date" in t[k]:
                    k=0
                else:
                    AuthorDate.append(t[k])
                    temp=1
                    #print t[k]
            if "CommitDate" in t[k]:
                    CommitDate.append(t[k])
                    temp=0
            k=k+1
            date.append(AuthorDate)
            date.append(CommitDate)
    return AuthorDate,CommitDate

def conv_heures(duree):
    r_liste=[]
    for i in range(len(duree)):
        r=int(duree[i])/1200
        r_liste.append(r)
    return r_liste

def liste_heures(duree1,duree2):
    if len(duree1)>len(duree2):
        var=len(duree2)
    else:
        var=len(duree1)
    listefi=[]
    ligne=[]
    for i in range(var):
        ligne.append(duree1[i])
        ligne.append(duree2[i])
        listefi.append(ligne)
        ligne=[]
    return np.array(listefi)

    def parsedate(dateAuteur,dateCommit):
    heure_liste=[]
    anneeCliste=[]
    moisCnewliste=[] 
    jourCnewliste=[]
    heureCnewliste=[]
    diffheures=0
    diffjours=0
    diff_mois=0
    diff_annee=0
    jours_liste=[]
    for i in range(len(dateAuteur)):
        date1A=str(dateAuteur[i]).split("\n")
        date1C=str(dateCommit[i]).split("\n")
        s=date1A[0] 
        w=date1C[0]
        anneeA=int(s[12]+s[13]+s[14]+s[15]) 
        anneeC=int(w[12]+w[13]+w[14]+w[15]) 
        moisA=int(s[17]+s[18] )
        moisC=int(w[17]+w[18]) 
        jourA=int(s[20]+s[21])
        jourC=int(w[20]+w[21]) 
        heureA=int(s[23]+s[24])
        heureC=int(w[23]+w[24]) 
        minnuteA=int(s[26]+s[27]) 
        minnuteC=int(w[26]+w[27]) 
        decalageA=int(s[33]+s[34]) #shift
        decalageC=int(w[33]+w[34]) #shift
        signe_decalA=s[32] #sign of the shift
        signe_decalC=w[32] #sign of the shift
        #Deccalage#######################################################
        jourCnew=jourC
        jourAnew=jourA
        moisCnew=moisC
        moisAnew=moisA
        heureCnew=heureC
       

        #####################################################################################
        anneeCliste.append(anneeC)
        moisCnewliste.append(moisCnew)
        jourCnewliste.append(jourCnew)
        heureCnewliste.append(heureCnew)
      
     
    return anneeCliste, moisCnewliste, jourCnewliste,heureCnewliste