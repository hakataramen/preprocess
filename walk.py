#coding: utf-8
import os
import nltk
import sys
import shelve
from collections import OrderedDict

#print(sys.argv[0])
#print(sys.argv[1])
#print(len(sys.argv))

if(len(sys.argv) < 2):
        print("引数が足りません")
        exit()

dirpath = sys.argv[1]

#print(sents)
a = []
dic = OrderedDict()
dic2 = OrderedDict()
count = 0
for files in os.listdir(dirpath):
        print(files)
#        f = open(file, "r")
#        document = f.read()
#        d = shelve.open("freq_shelve.db")
#        i = len(d)+1
#        sents = nltk.sent_tokenize(document)
