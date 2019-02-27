
from lxml import etree
import commands
import os
import subprocess
import git 
import csv
from git import Repo
import git
import numpy as np
import pandas as pd

def dowloadprojects(path):
    for dossier, sous_dossiers, fichiers in os.walk(repo):
        for j in range(len(fichiers)):
            with open(path+'/'+fichiers[j],"r") as f:
                for line in f.readlines():
                    if("https" in line):
                        lien=line
                        a=fichiers[j].split(".")
                        repertoire=path+a[0]
                        print a[0]
                        try: 
                            os.makedirs(repertoire)
                        except OSError:
                            if not os.path.isdir(repertoire):
                                Raise
                        repo_dir=repertoire
                        lien1=lien.split("\n")
                        git_url=str(lien1[0])
                        print git_url
                        Repo.clone_from(git_url, repo_dir)

def extraction_commits(repo):
    for dossier, sous_dossiers, fichiers in os.walk(repo):
        for j in range(len(fichiers)):
            with open(repo+'/'+fichiers[j],"r") as f:
                for line in f.readlines():
                    if("https" in line):
                        lien=line
                        a=fichiers[j].split(".")
                        repertoire=git.Repo(repo+a[0])
                        gitt = repertoire.git
                        print (repo+a[0])
                    else:
                        ch=line[0]+line[1]+line[2]+line[3]+line[4]+line[5]+line[6]+line[7]+line[8]+line[9]+line[10]+line[11]+line[12]+line[13]+line[14]+line[15]+line[16]+line[17]+line[18]+line[19]+line[20]+line[21]+line[22]+line[23]+line[24]+line[25]+line[26]+line[27]+line[28]+line[29]+line[30]+line[31]+line[32]+line[33]+line[34]+line[35]+line[36]+line[37]+line[38]+line[39]
                        if line[39]=='\n':
                            allo=0
                        else:
                            dat = gitt.show(ch,pretty="fuller")
                            myFile = open(repo, 'a')
                            myFile2 = open(repo"+a[0]+".txt", 'a')
                            myFile.write(dat.encode('utf-8'))
                            myFile2.write(dat.encode('utf-8'))
                            myFile.write("\n")
                            myFile2.write("\n")
                            myFile.write("mon_hash="+ch+"\n")
                            myFile2.write("mon_hash="+ch+"\n")
                            myFile2.write("\n")
                            myFile.write("End-of-patch")
                            myFile2.write("End-of-patch")
                            myFile.write("#### ####################end of patch##############################################")
                            myFile2.write("#### ####################end of patch##############################################")
                            myFile.write("###################################################################################")
                            myFile2.write("###################################################################################")
                            myFile.write("\n")
                            myFile2.write("\n")   