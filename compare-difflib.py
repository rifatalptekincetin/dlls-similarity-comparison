import difflib
import os
import time

def makestr(bf):
    ret=[]
    for i in bf.split("\n"):
        if i.startswith(" ") and len(i)>=32:
            ret.append(i[31:])
    return ret

def retaddress(bf,index):
    ret=0
    for i in bf.split("\n"):
        if i.startswith(" ") and len(i)>=32:
            ret+=1
            if ret==index:
                return i[2:10]

documents={}

for i in os.listdir("asm"):
    with open("asm/"+i,"r") as f:
        documents[i]=makestr(f.read())

##somesh

t=time.time()
s=difflib.SequenceMatcher(None,documents["1.txt"],documents["2.txt"],autojunk=False)
longest=s.find_longest_match(0,len(documents["1.txt"]),0,len(documents["2.txt"]))
print(time.time()-t,longest)


##find da longest matchs address

with open("asm/1.txt","r") as f:
    print("1.txt: {} - size: {}".format(retaddress(f.read(),longest.a),longest.size))

##find for da other file

with open("asm/2.txt","r") as f:
    print("2.txt: {} - size: {}".format(retaddress(f.read(),longest.b),longest.size))

