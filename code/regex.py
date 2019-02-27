import re
from lxml import etree
import commands
import os
import subprocess
import git 
import csv

def bug_reporter_hash(filepath):
    with open(filepath, 'r') as f:
        i=0
        k=0
        t=f.readlines()
        enre=[]
        test_str =""
        liste1=[]
        compt=0
        while (k<len(t)):
            temp=""
            if ("commit " in t[k]):
                if(t[k][0]!="c"):
                    z=0
                    i=i+1
                else:
                    i=k
                    i=i+1
                    j=0
                    #print h
                    compt=compt+1
                    while(j==0):
                        if("diff --" in t[i]):
                            j=1
                        else:
                            #print t[i]
                            test_str = test_str+str(t[i])
                            #bag.write(t[i])
                        i=i+1
                k=i
                if 'show_bug.cgi?id=' in test_str:
                    liste1.append(h)

            #print ok    
                    test_str="" 

            k=k+1
    return liste
            
def hash_extraction(repo):
    import git 

    
    repo = git.Repo(repo)
    gitt = repo.git

    for i in range(len(liste3)):
        dat = gitt.show(liste3[i],pretty="fuller",date="iso")
        myFile = open(repo+"test-new-linuxkernel-BUGfix.txt", 'a')
        gfile= open(repo+"global.txt", 'a')
        myFile.write(dat.encode('utf-8'))
        gfile.write(dat.encode('utf-8'))
        myFile.write("\n")
        gfile.write("\n")
        myFile.write("End-of-patch")
        gfile.write("End-of-patch")
        myFile.write("#### ####################end of patch##############################################")
        gfile.write("#### ####################end of patch##############################################")
        myFile.write("###################################################################################")
        myFile.write("\n")
        gfile.write("\n")
        i=i+1


        ###################################Troisieme liste######################################################
        

def regex(path):
    rep=path+'/bug_reporter'
    regex = r"(?i)(denial.of.service|\bXXE\b|remote.code.execution|\bopen.redirect|OSVDB|\bvuln|\bCVE\b|\bXSS\b|\bReDoS\b|\bNVD\b|malicious|x-frame-options|attack|cross.site|exploit|directory.traversal|\bRCE\b|\bdos\b|\bXSRF\b|clickjack|session.fixation|hijack|advisory|insecure|security|\bcross-origin\b|unauthori[z|s]ed|infinite.loop)"
    compt=0
    test_str=""
    line=""
    for dossier, sous_dossiers, fichiers in os.walk(rep):
        for w in range(len(fichiers)):
            print fichiers[w]
            with open(rep+'/'+fichiers[w], 'r') as f:
                t=f.readlines()
                k=0
                while (k<len(t)):
                    temp=""
                    if ("commit " in t[k]):
                        if "cherry" in t[k]:
                            z=0
                            i=i+1
                        else:
                            h=t[k][7]+t[k][8]+t[k][9]+t[k][10]+t[k][11]+t[k][12]+t[k][13]+t[k][14]+t[k][15]+t[k][16]+t[k][17]+t[k][18]+t[k][19]+t[k][20]+t[k][21]+t[k][22]+t[k][23]+t[k][24]+t[k][25]+t[k][26]+t[k][27]+t[k][28]+t[k][29]+t[k][30]+t[k][31]+t[k][32]+t[k][33]+t[k][34]+t[k][35]+t[k][36]+t[k][37]+t[k][38]+t[k][39]+t[k][40]+t[k][41]+t[k][42]+t[k][43]+t[k][44]+t[k][45]+t[k][46]+t[k][47]
                            i=k
                        #temp=temp+str(t[i])
                            i=i+1
                            j=0
                            compt=compt+1
                            while(j==0):
                                if("End-of-patch" in t[i]):
                                    j=1
                                else:
                                    test_str = test_str+str(t[i])
                                    line=line+t[i]
                     
                                i=i+1
                        k=i
                        #print("end")
                        matches = re.findall(regex, test_str, re.MULTILINE)
                        if (len(matches)==0):
                            dossier = open(rep+'/bug_fixs/'+fichiers[w]+'bugfixes.txt', 'a')
                            doss = open(rep+'/bug_fixs/txt/'+fichiers[w]+'bugfixes.txt', 'a')
                            dossier.write(h)
                            doss.write("commit "+h+'\n')
                            doss.write(test_str)
                            doss.write("End-of-patch")
                            doss.write("\n")
                        else:
                            #print "match"
                            dossier1 = open(rep+'/bug_fixs/'+fichiers[w]+'vulnerability.txt', 'a')
                            doss1 = open(rep+'/bug_fixs/txt/'+fichiers[w]+'vulnerability.txt', 'a')
                            dossier1.write(h)
                            doss1.write("commit "+h+'\n')
                            doss1.write(test_str)
                            doss1.write("End-of-patch")
                            doss1.write("\n")
                        test_str=""
                k=k+1
        
        ###########################################################fin de la premiere fonction###################
#############################################