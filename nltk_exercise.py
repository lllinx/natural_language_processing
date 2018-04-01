import nltk
from nltk.book import *
text1
############# searching text############
text1.concordance("monstrous")
text1.similar("monstrous")
# common_contexts allows us to examine just the contexts that are shared by two or more words
text2.common_contexts(["monstrous", "very"])
# dispersion plot: determine the location of a word in the text: how many words from the beginning it appears
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
# randomly generating some sentence
text1.generate()


########### Counting Vocabulary###############
len(text3)
sorted(set(text3))
len(set(text3))

# Frequency Distributions
fdist1 = FreqDist(text1)
vocabulary1 = list(fdist1.keys())
vocabulary1[:50]
fdist1.plot(50, cumulative=True)
# words that occur once only, the so-called hapaxes
fdist1.hapaxes()
# select long words that exists several times 
fdist5 = FreqDist(text5)
sorted([w for w in set(text5) if len(w)>7 and fdist5[w]>7]


# Collocations and Bigrams
