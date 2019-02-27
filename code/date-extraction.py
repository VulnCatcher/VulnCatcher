import re
from lxml import etree
import commands
import os
import subprocess
import git 
import csv
from datetime import datetime

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
def parsedate(dateAuteur,dateCommit):
    heure_liste=[]
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
        anneeA=int (s[12]+s[13]+s[14]+s[15]) 
        anneeC=int(w[12]+w[13]+w[14]+w[15]) 
        moisA=int(s[17]+s[18] )
        moisC=int(w[17]+w[18]) 
        jourA=int(s[20]+s[21])
        jourC=int(w[20]+w[21])
        heureA=int(s[23]+s[24]) 
        heureC=int(w[23]+w[24]) 
        minnuteA=int(s[26]+s[27]) 
        minnuteC=int(w[26]+w[27]) 
        decalageA=int(s[33]+s[34]) 
        decalageC=int(w[33]+w[34]) 
        signe_decalA=s[32] 
        signe_decalC=w[32] 
    
      
        datetimeAuteur=datetime(anneeA, moisA, jourA,heureA)
        datetimeCommit=datetime(anneeC, moisC, jourC,heureC)
        duree = datetimeCommit- datetimeAuteur 
        jours_liste.append(duree.seconds)
    return jours_liste
def parsedate(dateAuteur,dateCommit):
    heure_liste=[]
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
        anneeA=int(s[12]+s[13]+s[14]+s[15]) #
        anneeC=int(w[12]+w[13]+w[14]+w[15]) #
        moisA=int(s[17]+s[18] )#
        moisC=int(w[17]+w[18]) #
        jourA=int(s[20]+s[21])#  
        jourC=int(w[20]+w[21])#  
        heureA=int(s[23]+s[24]) # 
        heureC=int(w[23]+w[24]) # 
        minnuteA=int(s[26]+s[27]) #
        minnuteC=int(w[26]+w[27]) #
        decalageA=int(s[33]+s[34]) #
        decalageC=int(w[33]+w[34]) #
        signe_decalA=s[32] #
        signe_decalC=w[32] #
       
        kA=0
        KC=0
        if signe_decalA=="+":
            if (decalageA!=0):
                kA=decalageA
            else:
                kA=0
        if signe_decalA=="-":
            if (decalageA!=0):
                kA=-decalageA
            else:
                kA=0
        #pour les commits
        if signe_decalC=="+":
            if (decalageC!=0):
                kC=decalageC
            else:
                kC=0
        if signe_decalC=="-":
            if (decalageC!=0):
                kC=-decalageC
            else:
                kC=0
        constanteA=heureA-kA
        constanteC=heureC-kC
        #valeurs initales
        heureAnew=constanteA
        heureCnew=constanteC
        jourCnew=jourC
        jourAnew=jourA
        moisCnew=moisC
        moisAnew=moisA
        if (constanteA)<0:
            jourAnew=jourA-1
            heureAnew=24+constanteA
        else:
            if constanteA>=24:
                jourAnew=jourA+1  
                heureAnew=constanteA-24
        
        if ((constanteC)<0):
            jourCnew=jourC-1
            heureCnew=24+constanteC
        else:
            if constanteC>=24:
                jourCnew=jourC+1
                heureCnew=constanteC-24
        if jourAnew<=0:
            temp=jourAnew
            jourAnew=30+temp
            moisAnew=moisAnew-1
        else:
            if jourAnew>30:
                temp=jourAnew
                moisAnew=moisAnew+1
                jourAnew=temp-30
        if jourCnew<=0:
            temp=jourCnew
            jourCnew=30+temp
            moisCnew=moisCnew-1
        else:
            if jourCnew>30:
                temp=jourCnew
                moisCnew=moisCnew+1
                jourCnew=temp-30
        ########################################
        #cas de fevrier 
        if moisAnew==2:
            if jourAnew>28:
                temp=jourAnew
                jourAnew=temp-28
                moisAnew=moisAnew+1
        if moisCnew==2:
            if jourCnew>28:
                temp=jourCnew
                jourCnew=temp-28
                moisCnew=moisCnew+1
        
        if moisAnew>12:
            anneeA=anneeA+1
            temp=moisAnew
            moisAnew=temp-12
        else:
            if moisAnew<=0:
                anneeA=anneeA-1
                temp=moisAnew
                moisAnew=12+temp
        if moisCnew>12:
            anneeC=anneeC+1
            temp=moisCnew
            moisCnew=temp-12
        else:
            if moisCnew<=0:
                anneeC=anneeC-1
                temp=moisCnew
                moisCnew=12+temp

        #####################################################################################
        datetimeAuteur=datetime(anneeA, moisAnew, jourAnew,heureAnew)
        datetimeCommit=datetime(anneeC, moisCnew, jourCnew,heureCnew)
        duree = datetimeCommit- datetimeAuteur 
        jours_liste.append(duree.seconds)
    return jours_liste
def conv_heures(duree):
    r_liste=[]
    for i in range(len(duree)):
        r=int(duree[i])/1200
        r_liste.append(r)
    return r_liste

def conv_jours(duree):
    r_liste=[]
    for i in range(len(duree)):
        r=int(duree[i])/24
        r_liste.append(r)
    return r_liste

def liste_jours(duree1,duree2):
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