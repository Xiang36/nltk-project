import nltk
# nltk.download()
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.tree import Tree


SampleTXT='The yellow dog barked at the cat'
sentence= pos_tag(word_tokenize(SampleTXT))
print (sentence)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print (result)
result.draw()
