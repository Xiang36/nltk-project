from operator import itemgetter

# 取單一字元算頻率
def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

## 產生 bigram
def list2bigram(mylist):
    return [mylist[i:i+2] for i in range(0,len(mylist)-1)]

## 產生trigram
def list2trigram(mylist):
    return [mylist[i:i+3] for i in range(0,len(mylist)-2)]

## 計算 bigram 頻率
def bigram2freqdict(mybigram):
    mydict=dict()
    for (ch1,ch2) in mybigram:
        mydict[(ch1,ch2)]=mydict.get((ch1,ch2),0)+1
    return mydict

## 計算 trigram 頻率
def trigram2freqdict(mytrigram):
    mydict=dict()
    for (ch1,ch2,ch3) in mytrigram:
        mydict[(ch1,ch2,ch3)]=mydict.get((ch1,ch2,ch3),0)+1
    return mydict

## final print
def freq2report(freqlist):
    chs=str()
    print('Char(s)\tCount')
    print('=============')
    for (token,num) in freqlist:
        for ch in token:
            chs=chs+ch
        print(chs,'\t',num)
        chs=''
    return

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
# print(bigramfreqdict)
# print(trigramfreqdict)

## 進行排序並取出前五筆
bigramfreqsorted=sorted(bigramfreqdict.items(), key=itemgetter(1), reverse=True)
trigramfreqsorted=sorted(trigramfreqdict.items(), key=itemgetter(1), reverse=True)
# print(bigramfreqsorted[:5])
# print(trigramfreqsorted[:5])


## 印出較好看的方式
freq2report(chfreqsorted)
freq2report(bigramfreqsorted)
freq2report(trigramfreqsorted)