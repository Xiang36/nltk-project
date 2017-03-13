
def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

sentence='吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮。'
chlist=[ch for ch in sentence]

print(chlist)
chfreqdict=list2freqdict(chlist)
