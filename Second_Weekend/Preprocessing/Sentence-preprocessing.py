import nltk
from nltk.tokenize import sent_tokenize # 문장 Tokenization


text="His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to mae sure no one was near."
text_="I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text))
print(sent_tokenize(text_))