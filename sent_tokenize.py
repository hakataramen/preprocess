import nltk
import sys

print(sys.argv[0])
print(sys.argv[1])
print(len(sys.argv))

if(len(sys.argv) < 2):
    print("引数が足りません")
    exit()

fname = sys.argv[1]

f = open(fname,"r")
document = f.read() 

sents = nltk.sent_tokenize(document)
#print(sents)

for sent in sents:
    print(sent)

   

    

    
