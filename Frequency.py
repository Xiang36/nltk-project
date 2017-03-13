from operator import itemgetter

def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

def list2bigram(mylist):
    return [mylist[i:i+2] for i in range(0,len(mylist)-1)]

def list2trigram(mylist):
    return [mylist[i:i+3] for i in range(0,len(mylist)-2)]

def bigram2freqdict(mybigram):
    mydict=dict()
    for (ch1,ch2) in mybigram:
        mydict[(ch1,ch2)]=mydict.get((ch1,ch2),0)+1
    return mydict

def trigram2freqdict(mytrigram):
    mydict=dict()
    for (ch1,ch2,ch3) in mytrigram:
        mydict[(ch1,ch2,ch3)]=mydict.get((ch1,ch2,ch3),0)+1
    return mydict

sentence='吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮。'
chlist=[ch for ch in sentence]

# print(chlist)
chfreqdict=list2freqdict(chlist)
chfreqsorted=sorted(chfreqdict.items(),key=itemgetter(1),reverse=True)
# print(chfreqsorted)

# 限定印出前幾個最高次數的字及次數
## 僅印出前五個
chfreqsorted2=chfreqsorted[:5]
## 印出符合條件之結果
chfreqsorted3=list()
for (ch,num) in chfreqsorted:
    if num > 1:
        chfreqsorted3.append((ch,num))

# print(chfreqsorted2)
# print(chfreqsorted3)


chbigram=list2bigram(chlist)
chtrigram=list2trigram(chlist)
# print(chbigram)
# print(chtrigram)

## 印出 bigram trigram 頻率
bigramfreqdict=bigram2freqdict(chbigram)
trigramfreqdict=trigram2freqdict(chtrigram)
print(bigramfreqdict)
print(trigramfreqdict)