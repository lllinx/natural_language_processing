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