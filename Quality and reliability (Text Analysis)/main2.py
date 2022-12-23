import re
import pandas as pd
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import wordnet

with open("text.txt", "r") as f:
    text = f.read()
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
# Токенизация
tokenize=nltk.word_tokenize((text))
print(tokenize)
# Конец токенизации


# Функция для указать правильный тег «part-of-speech» (POS-тег)
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)
# Конец функции
# Лемматизация
lemmatizer = nltk.WordNetLemmatizer()
lemmatized_output = ' '.join([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in tokenize])
print(lemmatized_output)

# Мешок слов
corpus = nltk.sent_tokenize(text)
for i in range(len(corpus )):
    corpus [i] = corpus [i].lower()
    corpus [i] = re.sub(r'\W',' ',corpus [i])
    corpus [i] = re.sub(r'\s+',' ',corpus [i])
vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names_out()
print(f'Полученный фрейм:\n\n{pd.DataFrame(bag_of_words.toarray(), columns=feature_names)}')
#Конец мешка
# Встречаемость
f_dist = nltk.FreqDist(tokenize)
for f in f_dist:
    print(f'{f}: {f_dist[f]}')


wc = WordCloud()
wc.generate(text)
# wc.to_file("output3.png")
