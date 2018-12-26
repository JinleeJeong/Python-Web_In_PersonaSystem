import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# ==============================================================================
tokenizer = TreebankWordTokenizer() # 표준 단어 Tokenization
text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
x = tokenizer.tokenize(text)
# print(x)
# ==============================================================================


# ==============================================================================
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
# print(word_tokenize(text)) # word_tokenize
y = word_tokenize(text)
print(y)
y_ = pos_tag(y)
print(y_)
# ==============================================================================