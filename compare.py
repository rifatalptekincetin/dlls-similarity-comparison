import os
import time

class Line():
    def __init__(self,address,val):
	    self.address=address
	    self.val=val

    def __call__(self):
        return self.val

def makestr(bf):
    ret=[]
    for i in bf.split('\n'):
        if i.startswith(" ") and len(i)>=32:
            ret.append(Line(i[2:10],i[31:]))
    return ret

def makestrx64(bf):
    ret=[]
    for i in bf.split('\n'):
        if i.startswith(" ") and len(i)>=40:
            ret.append(Line(i[2:18],i[39:]))
    return ret

def compare(a,b,minmatch=3):
    matches=[]
    lena=len(a)
    lenb=len(b)

    mij=[]
    for i in range(lena):
        for j in range(lenb):
            match=0
            try:
                while a[i+match].val==b[j+match].val:
                    match+=1
            except:
                continue
            if match >= minmatch:
                if [i-1,j-1] not in mij:
                    matches.append([a[i],b[j],match])
                mij.append([i,j])
                j+=match
    return matches

documents={}

for i in os.listdir("asm"):
    with open("asm/"+i,"r") as f:
        documents[i]=makestr(f.read())

t=time.time()
matches=compare(documents["1.txt"],documents["2.txt"],15)
print(time.time()-t, len(matches))
with open("out.txt","w") as f:
    for i in matches:
        f.write("1.txt:{} - 2.txt:{} - {}\n".format(i[0].address,i[1].address,i[2]))

