#coding: utf-8
import os
import nltk
import sys
import shelve
from collections import OrderedDict

#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
#print(len(sys.argv))

if(len(sys.argv) < 3):
    print("引数が足りません")
    exit()

dirpath = sys.argv[1]
if dirpath[-1] != "/": dirpath += "/"
label = sys.argv[2]
#f = open (fname,"r")

#document = f.read()

#sents = nltk.sent_tokenize(document)
#print(sents)
a = []

#dic2 = OrderedDict()
count = 0
d = shelve.open("freq_shelve.db")
for filename in os.listdir(dirpath):
    print(label,end=" ")
    dic = OrderedDict()
    f = open(dirpath+filename, "r")
    document = f.read()
    i = len(d)+1
    sents = nltk.sent_tokenize(document)
    for sent in sents:
        a=nltk.word_tokenize(sent) #sentsから読み込んだsentの1行分だけ単語分割したもの、以降この1行ずつの処理
        #print(a)
        for word in a:
            if(word in dic):
                dic[word] += 1
            else:
                dic[word] = 1
                # dic2[word] = i
                if not word in d:
                    d.update({word:i})
                    i+=1
#d.close()

#d = shelve.open("freq_shelve.db")            
    for word, index in sorted(d.items(), reverse=False, key=lambda x:x[1]):
        if word in dic:
            print("%d:%d" % (d[word], dic[word]),end=" ")
    print()
