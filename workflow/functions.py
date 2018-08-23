 
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
import os
import csv


#traitement de la variable nature introduite pour savoir s'il s'agit des logs d'un commit ou d'un fix

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
            
    # #creation du repertoire qui vas contenir les logs 
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
    # Debut du parsing par fichier 
    for dossier, sous_dossiers, fichiers in os.walk(repertoire):
        s=sous_dossiers
        for w in range(len(s)):
            filename=s[w]
            #print sous_dossiers[w]
            sentences = open(repertoire+'/'+filename+'.txt', 'r')
            vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 18) 
            train_data_features = vectorizer.fit_transform(sentences)
            for dossier, sous_dossiers, fichiers in os.walk(repertoire+'/'+filename):
                
                for j in range(len(fichiers)):
                    dc= open(dossier+'/'+fichiers[j], 'r')
                    charac1=vectorizer.transform(dc).toarray()
                    liste2=[]
                    #print charac1
                    #traitement du vecteur une fois recuperé
                    vr=[]
                    liste=[]
                    ch=""
                    for i in range(len(charac1)):
                        for j in range(len(charac1[i])):
                            #print len(charac1[i])
                            vr.append(charac1[i][j])
                            ch=str(charac1[i][j])+ch
                        liste.append(vr)
                        liste2.append(ch)
                        ch=''
                    #print liste2
                ##################################################################################
     
                ## Creation du fichier CSV pour sauvegarder les logs
                    #print len(liste2)
                    #print (path+'/csv/'+filename+'.csv')
                    for r in range(len(liste2)):
                        c = csv.writer(open(path+'/csv/logs/'+filename+'.csv', "a"))
                        c.writerow(liste2[r])


    #Exemple d'utilisation de la fonction 
    f=bagofword('/home/delwende/Documents/machine3','commit')

    from lxml import etree
import commands
import os
import subprocess
import git 
import collections, re


def commit_extraction(path): 
    #On verifie si le repertoire existe dans le cas echeant on le crée de nouveau
    repertoire=path+'/commits'
    try: 
        os.makedirs(repertoire)
    except OSError:
        if not os.path.isdir(repertoire):
            Raise
    #On commence a parcourir tous les fichiers xmls contenus dans le dossier 
    for dossier, sous_dossiers, fichiers in os.walk(path+'/xml'):
        for j in range(len(fichiers)):
            tree = etree.parse(path+'/xml/'+fichiers[j])
            #
            #
            #  pour recuperer les hash de chaque commit avant et apres 
            fil,ext=fichiers[j].split("-")
            
            i=0
            repo = git.Repo(path+'/git/'+fil)
            gitt = repo.git
            for mess in tree.xpath("/data7/cve/patches/commit"):
                before= tree.xpath("/data7/cve/patches/commit/files/file/before")
                befor=before[i]
                dat = gitt.show(mess.get("hash"))
                myFile = open(path+'/commits/'+ fil+'.txt', 'a')
                myFile.write(dat.encode('utf-8'))
                myFile.write("\n")
                myFile.write("End-of-patch")
                myFile.write("#### ####################end of patch##############################################")
                myFile.write("###################################################################################")
                myFile.write("\n")
                i=i+1
                myFile.close()
#Exemple d'application de la fonction de commi-extraction
commit_extraction('/home/delwende/Documents/machine3')

from lxml import etree
import commands
import os
import subprocess
import git 
import csv

#fonction qui supprime les logs vides 

def commit_empty(rep):
    #script-pour supprimer tous les fichiers nulls 
    for dossier, sous_dossiers, fichiers in os.walk(rep):
         for j in range(len(fichiers)):
                #print fichiers[j]
                if (os.path.getsize(dossier+'/'+fichiers[j])==1):
                    os.remove(dossier+'/'+fichiers[j]) 
                    print(fichiers[j])
    #fin du script 




#Fonction qui extrait les logs des fichiers 



def log_extraction(path,nature):
    #traitement de la variable nature introduite pour savoir s'il s'agit des logs d'un commit ou d'un fix
    rep=path+'/commits'
    repertoire=path+'/commits_logs'
    if nature=="commit":
        rep=path+'/commits'
    else:
        if nature=="fix":
            rep=path+'/fixs'
        else:
            print ("Erreur sur la nature des logs à extraire")
            
    # #creation du repertoire qui vas contenir les logs 
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
    # Debut du parsing par fichier 
    
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
                    
#Exemple d'usage de la fonction d'extraction de logs 
log_extraction('/home/delwende/Documents/machine3','commit')
from lxml import etree
import commands
import os
import subprocess
import git 
import csv


#Definition de la fonction qui permettra d'ecrire les resultats des variables dans un fichier csv et retourner une liste 
def vul_features_csv(pathcsv,fichier,i):
    repertoire=path+"/csv"
    try: 
        os.makedirs(repertoire)
    except OSError:
        if not os.path.isdir(repertoire):
            Raise
    feature=[]
    ## Creation du fichier CSV pour sauvegarder lesfeatures concernant les vulnerabilites
    c = csv.writer(open(path+"/csv/"+fichier+'.csv', "wb"))
    for d in range(i):
        c.writerow([compter_size_off_p[d],compter_size_off_f[d],compter_return_p[d],compter_return_f[d],compter_break_p[d],compter_break_f[d],compter_continue_p[d],compter_continue_f[d],compter_INTMAX_p[d],compter_INTMAX_f[d],compter_define_p[d],compter_define_f[d],compter_struc_f[d],compter_struc_p[d],compter_void_f[d],compter_void_p[d],compter_offset_p[d],compter_offset_f[d],f17[d],f18[d],f19[d],f20[d],f21[d],f22[d],classe[d]])
        feature=feature.append([compter_size_off_p[d],compter_size_off_f[d],compter_return_p[d],compter_return_f[d],compter_break_p[d],compter_break_f[d],compter_continue_p[d],compter_continue_f[d],compter_INTMAX_p[d],compter_INTMAX_f[d],compter_define_p[d],compter_define_f[d],compter_struc_f[d],compter_struc_p[d],compter_void_f[d],compter_void_p[d],compter_offset_p[d],compter_offset_f[d],f17[d],f18[d],f19[d],f20[d],f21[d],f22[d],classe[d]])

        
    return feature  


# Definition de la fonction qui permettra d'ecrire des resultats des features des vulnerabilités du bug fix
def features_csv(pathcsv,fichier,i):
    repertoire=path+"/csv"
    try: 
        os.makedirs(repertoire)
    except OSError:
        if not os.path.isdir(repertoire):
            Raise
    feature=[]

    c = csv.writer(open(path+"/csv/"+fichier+'.csv', "wb"))
    for d in range(i):
        c.writerow([compterplus[d],comptermin[d],compter_if_p[d],compter_if_n[d],compter_boucle_p[d],compter_boucle_n[d],compter_ficher_p[d],compter_ficher_n[d],compter_func_p[d],compter_func_n[d],compter_paren_p[d],compter_paren_n[d],compter_bool_p[d],compter_bool_n[d],compter_aff_p[d],compter_aff_n[d],f1[d],f2[d],f3[d],f4[d],f5[d],f6[d],f7[d],f8[d],f9[d],f10[d],f11[d],f12[d],f13[d],f14[d],f15[d],f16[d],compter_size_off_p[d],compter_size_off_f[d],compter_return_p[d],compter_return_f[d],compter_break_p[d],compter_break_f[d],compter_continue_p[d],compter_continue_f[d],compter_INTMAX_p[d],compter_INTMAX_f[d],compter_define_p[d],compter_define_f[d],compter_struc_f[d],compter_struc_p[d],compter_void_f[d],compter_void_p[d],compter_offset_p[d],compter_offset_f[d],f17[d],f18[d],f19[d],f20[d],f21[d],f22[d],classe[d]])  
        
        
#Definition de la fonction qui vas contenir toutes les vulnerabilités





#Definition d ela fonction qui permettra d'extraire les attributs cwe et de retourner une liste 
def cwe_feature(path):
    liste=[]
    tree = etree.parse(path)
    root = tree.getroot()
    for decade in root.findall("./cve"):
        #print(decade.attrib)
        #print decade[0].text
        for year in decade.findall(".patches/commit"):
            liste.append(decade[0].text)
            #print(year.get("hash"), '\n')

    listenew=[]
    for i in range(len(liste)):
        if str(liste[i])=="None":
            listenew.append(0)
        else:
            listenew.append(liste[i])
    return listenew






#la fonction  feature est appellée avec deux parametre le premier etant le repertoire du projet(Data7) et le deuxieme etant la nature des features a extraires : s'il sagit d'un commit ou d'un fix a extraire 
def features(path,nature):
    #nature permet de savoir is on veux extraire les features d'un commit ou les feature d'un fix
    rep=path+'/commits'
    if nature=="commit":
        rep=path+'/commits'
    else:
        if nature=="fix":
            rep=path+'/fixs'
        else:
            print ("Erreur sur la nature des features à extraire")
    global_feature=[] # liste de feature globale
        
    for dossier, sous_dossiers, fichiers in os.walk(rep):
        for w in range(len(fichiers)):
            i=0
            kbp=0
            kbn=0
            t=0
            #
            #Les variables temporaires 
            #

            cmin=0
            cmax=0
            c_if_p=0
            c_if_n=0
            c_b_p=0
            c_b_n=0
            c_n_p=0
            c_n_n=0
            c_func_n=0
            c_func_p=0
            c_par_n=0
            c_par_p=0
            c_bool_n=0
            c_bool_p=0
            c_affec_p=0
            c_affec_n=0
            #
            #VAriables liées aux vulnerabilités 
            #
            c_bool_size_f=0
            c_bool_size_p=0
            c_bool_return_p=0
            c_bool_return_f=0
            c_bool_break_p=0
            c_bool_break_f=0
            c_bool_continue_p=0
            c_bool_continue_f=0
            c_bool_INTMAX_p=0
            c_bool_INTMAX_f=0
            c_bool_goto_p=0
            c_bool_goto_f=0
            c_bool_define_p=0
            c_bool_define_f=0
            c_nbr_struc_p=0
            c_nbr_struc_f=0
            c_nbr_void_p=0
            c_nbr_void_f=0
            c_nbr_offset_p=0
            c_nbr_offset_f=0
            #
            #Listes qui representent les compteurs
            #
            compterplus=[] #compteurs de lignes ajoutées
            comptermin=[]  #compteur de lignes retirees
            compter_if_p=[] #compteur de if ajoutés
            compter_if_n=[] #compteur de if enlevés
            compter_ficher_p=[] #nombre de fichiers ajoutés 
            compter_ficher_n=[] #nombre de fichiers ajoutés 
            compter_boucle_p=[] #compteur de boucle ajoutées
            compter_boucle_n=[] #compteur de boucles retirées
            compter_func_p=[]
            compter_func_n=[]
            compter_paren_p=[]
            compter_paren_n=[]
            compter_bool_p=[]
            compter_bool_n=[]
            compter_aff_p=[]
            compter_aff_n=[]

            #A ajouter dans la liste # les nouvelles valeurs booleennes
            compter_size_off_p=[]
            compter_size_off_f=[]
            compter_return_p=[]
            compter_return_f=[]
            compter_break_p=[]
            compter_break_f=[]
            compter_continue_p=[]
            compter_continue_f=[]
            compter_INTMAX_p=[]
            compter_INTMAX_f=[]
            compter_goto_p=[]
            compter_goto_f=[]
            compter_define_p=[]
            compter_define_f=[]
            compter_struc_f=[]
            compter_struc_p=[]
            compter_void_f=[]
            compter_void_p=[]
            compter_offset_f=[]
            compter_offset_p=[]
            #les listes composées de listes existantes 
            #f1=compter_if_p - compter_if_n
            #f2=compter_boucle_p - compter_boucle_n
            #f3=compterplus - comptermin
            #f4=compter_fichier_p-compter_fichier_n

            f1=[]
            f2=[]
            f3=[]
            f4=[]
            f5=[]
            f6=[]
            f7=[]
            f8=[]

            # Les compositions en additionant 
            #

            f9=[]
            f10=[]
            f11=[]
            f12=[]
            f13=[]
            f14=[]
            f15=[]
            f16=[]

            ### vulnerabilités
            f17=[]
            f18=[]
            f19=[]
            f20=[]
            f21=[]
            f22=[]
            classe_fix=[]

            ##
            # Initialisation des compteurs 
            #
            #compterplus.append(0)
            #comptermin.append(0)
            #combreficher.append(0)
            #compter_boucle_p.append(0)
            #compter_boucle_n.append(0)
            #compter_if_n.append(0)
            #compter_if_p.append(0)
            #compter_ficher_p=[] #nombre de fichiers ajoutés 
            #compter_ficher_n=[] #nombre de fichiers ajoutés 
            #
            # Debut du parsing 
            #
            #
            
            #
            with open(rep+'/'+fichiers[w], 'r') as f:
                for line in f.readlines():
                    if "End-of-patch" in line:
                        #si on est a la fin d'un patch on affecte les listes des valeures contenues dans les variables temporaires 
                        compterplus.append(cmax)
                        comptermin.append(cmin)
                        compter_if_p.append(c_if_p)
                        compter_if_n.append(c_if_n)
                        compter_boucle_p.append(c_b_n)
                        compter_boucle_n.append(c_b_p)
                        compter_ficher_p.append(c_n_p) 
                        compter_ficher_n.append(c_n_n)
                        compter_func_p.append(c_func_p)
                        compter_func_n.append(c_func_n)
                        compter_paren_p.append(c_par_p)
                        compter_paren_n.append(c_par_n)
                        compter_bool_p.append(c_bool_p-kbp)
                        compter_bool_n.append(c_bool_n-kbn)
                        compter_aff_p.append(c_affec_p)
                        compter_aff_n.append(c_affec_n)
                        classe_fix.append(-1)
                        #
                        #
                        #ajouté nouvellement 
                        compter_size_off_p.append(c_bool_size_p) 
                        compter_size_off_f.append(c_bool_size_f)
                        compter_return_p.append(c_bool_return_p)
                        compter_return_f.append(c_bool_return_f)
                        compter_break_p.append(c_bool_break_p)
                        compter_break_f.append(c_bool_break_f)
                        compter_continue_p.append(c_bool_continue_p)
                        compter_continue_f.append(c_bool_continue_f)
                        compter_INTMAX_p.append(c_bool_INTMAX_p)
                        compter_INTMAX_f.append(c_bool_INTMAX_f)
                        compter_goto_p.append(c_bool_goto_p)
                        compter_goto_f.append(c_bool_goto_f)
                        compter_define_p.append(c_bool_define_p)
                        compter_define_f.append(c_bool_define_f)
                        compter_struc_p.append(c_nbr_struc_p)
                        compter_struc_f.append(c_nbr_struc_f)
                        compter_void_p.append(c_nbr_void_p)
                        compter_void_f.append(c_nbr_void_f)
                        compter_offset_f.append(c_nbr_offset_f)
                        compter_offset_p.append(c_nbr_offset_p)

                        #
                        #---------------------------------------------------
                        #On rempli les valeurs des listes positives maintenant 
                        f1.append(compter_if_p[i]-compter_if_n[i])
                        f2.append(compter_boucle_p[i]-compter_boucle_n[i])
                        f3.append(compterplus[i]-comptermin[i])
                        f4.append(compter_ficher_p[i]-compter_ficher_n[i])
                        f5.append(compter_func_p[i]- compter_func_n[i])
                        f6.append(compter_paren_p[i]-compter_paren_n[i])
                        f7.append(compter_bool_p[i]-compter_bool_n[i])
                        f8.append(compter_aff_p[i]-compter_aff_n[i])
                        f17.append(compter_struc_p[i]-compter_struc_f[i])
                        f19.append(compter_void_p[i]-compter_void_f[i])
                        f21.append(compter_offset_p[i]-compter_offset_f[i])



                        #On calcule la somme des features maintenant 
                        f9.append(compter_if_p[i]+compter_if_n[i])
                        f10.append(compter_boucle_p[i]+compter_boucle_n[i])
                        f11.append(compterplus[i]+comptermin[i])
                        f12.append(compter_ficher_p[i]+compter_ficher_n[i])
                        f13.append(compter_func_p[i]+compter_func_n[i])
                        f14.append(compter_paren_p[i]+compter_paren_n[i])
                        f15.append(compter_bool_p[i]+compter_bool_n[i])
                        f16.append(compter_aff_p[i]+compter_aff_n[i])
                        f18.append(compter_struc_p[i]+compter_struc_f[i])
                        f20.append(compter_void_p[i]+compter_void_f[i])
                        f22.append(compter_offset_p[i]+compter_offset_f[i])

                        #on incremente une variable qui me premettra de lire le contenu des listes a l'instant t
                        i=i+1
                        #Puis on reinitialise les compteurs temporaires 
                        cmin=0
                        cmax=0
                        c_if_p=0
                        c_if_n=0
                        c_b_p=0
                        c_b_n=0
                        c_n_p=0
                        c_n_n=0
                        c_func_n=0
                        c_func_p=0
                        c_par_n=0
                        c_par_p=0
                        c_bool_n=0
                        c_bool_p=0
                        c_affec_p=0
                        c_affec_n=0
                        c_bool_size_p=0
                        c_bool_size_f=0
                        c_bool_return_p=0
                        c_bool_return_f=0
                        c_bool_break_p=0
                        c_bool_break_f=0
                        c_bool_continue_p=0
                        c_bool_continue_f=0
                        c_bool_INTMAX_p=0
                        c_bool_INTMAX_f=0
                        c_bool_goto_p=0
                        c_bool_goto_f=0
                        c_bool_define_p=0
                        c_bool_define_f=0
                        c_nbr_struc_p=0
                        c_nbr_struc_f=0
                        c_nbr_void_p=0
                        c_nbr_void_f=0
                        c_nbr_offset_p=0
                        c_nbr_offset_f=0            

                        #compte le nombre d'ajouts 
                    if line[0]=="+":
                        if "if (" in line:
                            c_if_p=c_if_p+1
                        if ("for (" in line) or ("while (" in line):
                            c_b_p=c_b_p+1
                        if line[1]=="+" and line[2]=="+": ##détection des fichiers ajoutés pour chaque patch 
                            c_n_p=c_n_p+1
                        if any(i in line for i in ["int", "static", "void", "float", "char", "char*", "string"]):
                            if "(" in line  and ")" in line:
                                c_func_p=c_func_p+1
                        if("(" in line) and (")" in line): # pour la recherche des expressions entre parenthèses
                            c_par_p=c_par_p+1
                        if any(i in line for i in ["||", "&&", "!"]): #operateurs booléens, on exclus l'operateur "#" du calcul
                            if "!="in line:
                                kbp=kbp+1
                            c_bool_p=c_bool_p+1
                        temp=0
                        for t in range(len(line)):
                            if line[t]=="=":
                                temp=temp+1
                        c_affec_p=c_affec_p+temp
                        if "sizeof" in line:
                            c_bool_size_p=1
                        if "break" in line:
                            c_bool_break_p=1
                        if "return" in line:
                            c_bool_return_p=1 
                        if "continue" in line:
                            c_bool_continue_p=1
                        if "int max" in line:
                            c_bool_INTMAX_p=1
                        if "goto" in line:
                            c_bool_goto_p=1
                        if "#define" in line:
                            c_bool_define_p=1 
                        if"struct" in line:
                            c_nbr_struc_p=c_nbr_struc_p+1 
                        if"void" in line:
                            c_nbr_void_p=c_nbr_void_p+1 
                        if"offset =" in line:
                            c_nbr_offset_p= c_nbr_offset_p+1 


                    #compte le nombre d'ajouts en terme de lignes 
                        cmax=cmax+1
                    if line[0]=="-":
                        if "if (" in line:
                            c_if_n=c_if_n+1
                        if "sizeof" in line:
                            c_bool_size_f=1
                        if "break" in line:
                            c_bool_break_f=1
                        if "return" in line:
                            c_bool_return_f=1 
                        if "continue" in line:
                            c_bool_continue_f=1
                        if "int max" in line:
                            c_bool_INTMAX_f=1

                        if "goto" in line:
                            c_bool_goto_f=1
                        if "#define" in line:
                            c_bool_define_f=1    
                        if"struct" in line:
                            c_nbr_struc_f=c_nbr_struc_f+1    
                        if"void" in line:
                            c_nbr_void_f=c_nbr_void_f+1 
                        if"offset =" in line:
                            c_nbr_offset_f= c_nbr_offset_f+1     



                    #----------------------------------------------------------
                        if ("for (" in line) or ("while (" in line):
                            c_b_n=c_b_n+1
                        if line[1]=="-" and line[2]=="-": ##détection des fichiers retirés pour chaque patch 
                            c_n_n=c_n_n+1
                        if any(i in line for i in ["int", "static", "void", "float", "char", "char*", "string"]):
                            if "(" in line and ")" in line:
                                c_func_n=c_func_n+1 
                        if ("(" in line) and (")" in line):
                            c_par_n=c_par_n+1
                        if any(i in line for i in ["||", "&&", "!"]): #operateurs booléens, on exclus l'operateur "#" du calcul
                            if "!="in line:
                                kbn=kbn+1
                            c_bool_n=c_bool_n+1
                        temp=0
                        for t in range(len(line)):
                            if line[t]=="=":
                                temp=temp+1
                        c_affec_n=c_affec_n+temp

                    #compte le nombre de retraits en termes de lignes 
                        cmin=cmin+1
            f.close()
            
            #on appelle maintenant la fonction qui permet de recuperer les ids cwe de chaque commmit pour les joindre aux features
            listenew=[] # On crée la liste qui vas recevoir les cwe
            if nature=='commit':
                if fichiers[w]=='systemd.txt':
                    listenew= cwe_feature(path+'/xml/systemd-data7.xml')
                if fichiers[w]=='wireshark.txt':
                    listenew= cwe_feature(path+'/xml/wireshark-data7.xml')
                if fichiers[w]=='openssl.txt':
                    listenew= cwe_feature(path+'/xml/openssl-data7.xml')
                if fichiers[w]=='linux_kernel.txt':
                    listenew= cwe_feature(path+'/xml/linux_kernel-data7.xml')
            if nature=='fix':
                listenew=classe_fix
            
            #On enregistre les resultats sous format csv et on crée une liste qui vas contenir les features de tous les fichiers 
            feature=[]

            c = csv.writer(open(path+"/csv/"+fichiers[w]+'.csv', "wb"))
            for d in range(i):
                c.writerow([compterplus[d],comptermin[d],compter_if_p[d],compter_if_n[d],compter_boucle_p[d],compter_boucle_n[d],compter_ficher_p[d],compter_ficher_n[d],compter_func_p[d],compter_func_n[d],compter_paren_p[d],compter_paren_n[d],compter_bool_p[d],compter_bool_n[d],compter_aff_p[d],compter_aff_n[d],f1[d],f2[d],f3[d],f4[d],f5[d],f6[d],f7[d],f8[d],f9[d],f10[d],f11[d],f12[d],f13[d],f14[d],f15[d],f16[d],compter_size_off_p[d],compter_size_off_f[d],compter_return_p[d],compter_return_f[d],compter_break_p[d],compter_break_f[d],compter_continue_p[d],compter_continue_f[d],compter_INTMAX_p[d],compter_INTMAX_f[d],compter_define_p[d],compter_define_f[d],compter_struc_f[d],compter_struc_p[d],compter_void_f[d],compter_void_p[d],compter_offset_p[d],compter_offset_f[d],f17[d],f18[d],f19[d],f20[d],f21[d],f22[d],listenew[d]])        
                #global_feature contient les instances de features de toutes les classes
                global_feature.append([compterplus[d],comptermin[d],compter_if_p[d],compter_if_n[d],compter_boucle_p[d],compter_boucle_n[d],compter_ficher_p[d],compter_ficher_n[d],compter_func_p[d],compter_func_n[d],compter_paren_p[d],compter_paren_n[d],compter_bool_p[d],compter_bool_n[d],compter_aff_p[d],compter_aff_n[d],f1[d],f2[d],f3[d],f4[d],f5[d],f6[d],f7[d],f8[d],f9[d],f10[d],f11[d],f12[d],f13[d],f14[d],f15[d],f16[d],compter_size_off_p[d],compter_size_off_f[d],compter_return_p[d],compter_return_f[d],compter_break_p[d],compter_break_f[d],compter_continue_p[d],compter_continue_f[d],compter_INTMAX_p[d],compter_INTMAX_f[d],compter_define_p[d],compter_define_f[d],compter_struc_f[d],compter_struc_p[d],compter_void_f[d],compter_void_p[d],compter_offset_p[d],compter_offset_f[d],f17[d],f18[d],f19[d],f20[d],f21[d],f22[d],listenew[d]])        
    return global_feature


    #Exemple d'usage de la fonction feature()

    f=features('/home/delwende/Documents/machine3','commit')

    #liste f contiendra l'ensemble des features extraites par la fonction.


    def oneclassfucntion(train,test):

    train1=train
    test1=test
    
    tt1=train1
    label_val=[]
    data_train=[]
    for i in range(len(tt1)):
        data_train.append(tt1[i])
        label_val.append(1)
    label_train=np.array(label_val)

    
                                        # Training    
    #One class classifier : on utilise la partie trainset2
    clf = svm.OneClassSVM(nu=0.1,kernel = "linear", gamma =0.5)
    y_score = clf.fit(data_train)
    preds = clf.predict(test1) 
    
    ######################################Extraction des valeurs positives et negatives dans le predictset########################"
    
    pred_pos=[]
    pred_neg=[]
    k=0
    tt=test1
    for i in range(len(preds)):
        if(preds[i]==-1):
            k=k+1
            pred_neg.append(tt[i])
        else:
            pred_pos.append(tt[i])
        
    #fin extraction
    posfi=[]
    #k=randint(0,40)
    #for i in range(len(pred_neg)-len(trainset2)):
    ##############Le trainset 
    positive=[]
    for i in range(len(pred_pos)):
        positive.append(pred_pos[i])
    for i in range(len(tt1)):
        positive.append(tt1[i])
    trainset2=[]
    lab_train2=[]
    return positive

def cotrainingfunction(X1_train,X2_train,X_label,X1_predict,X2_predict):

    #Next step
    X1=np.array(X1_train)
    X2=np.array(X2_train)
    label_train1=np.array(X_label)
    Xt1=np.array(X1_predict)
    Xt2=np.array(X2_predict)
    
    
    print 'SVM CoTraining'
    svm_co_clf = CoTrainingClassifier(LinearSVC())  #regarder le fichier classifier.py
    svm_co_clf.fit(X1, X2, label_train1)
    y_pred1 = svm_co_clf.predict(Xt1,Xt2)

    
    return  y_pred1 