from operator import itemgetter

def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

sentence='吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮。'
chlist=[ch for ch in sentence]

print(chlist)
chfreqdict=list2freqdict(chlist)
chfreqsorted=sorted(chfreqdict.items(),key=itemgetter(1),reverse=True)
print(chfreqsorted)

# 限定印出前幾個最高次數的字及次數
## 僅印出前五個
chfreqsorted2=chfreqsorted[:5]
## 印出符合條件之結果
chfreqsorted3=list()
for (ch,num) in chfreqsorted:
    if num > 1:
        chfreqsorted3.append((ch,num))

print(chfreqsorted2)
print(chfreqsorted3)