import nltk
import re

from wordcloud import WordCloud
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import pymorphy2

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')

morph = pymorphy2.MorphAnalyzer()  # Анализатор для русскоязычного текста
lemmatizer = WordNetLemmatizer()  # Анализатор для англоязычного текста
wc = WordCloud()


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


# Облако слов
def word_cloud(text):
    sentence = nltk.sent_tokenize(text)
    count_vectorizer = CountVectorizer()

    bag_of_words = count_vectorizer.fit_transform(sentence)

    feature_names = count_vectorizer.get_feature_names_out()
    print(f'Полученный фрейм:\n\n{pd.DataFrame(bag_of_words.toarray(), columns=feature_names)}')


# Частота встречаемости
def frequency_of_occurrence(text):
    f_dist = nltk.FreqDist(text)
    for f in f_dist:
        print(f'{f}: {f_dist[f]}')
    print('\n')


# Процесс лемматизации для англоязычных слов
def lemma(text):
    text = nltk.word_tokenize(text)
    result = []
    for word in text:
        word_lemm = lemmatizer.lemmatize(word, get_wordnet_pos(word))
        result.append(word_lemm)
    print(f'\nПеречень слов текста до лемматизации:\n{text}')
    print(f'\nПеречень слов текста после лемматизации:\n{result}')
    for i in range(len(result)):
        if text[i] != result[i]:
            print(f'{text[i]} => {result[i]}')


# Токены слов
def word_tokens(text):
    text_tokens = nltk.word_tokenize(text)

    print(f'Разбиение по токенам слов: {text_tokens}')

    frequency_of_occurrence(text_tokens)


# Процесс лемматизации для русского текста
def lemma_ru(text):
    text = nltk.word_tokenize(text)
    result = []
    for word in text:
        p = morph.parse(word)[0]
        result.append(p.normal_form)
    print(f'\nПеречень слов текста до лемматизации:\n{text}')
    print(f'\nПеречень слов текста после лемматизации:\n{result}')

    for i in range(len(result)):
        if text[i] != result[i]:
            print(f'{text[i]} => {result[i]}')


# Организация чтения из файла (английский текст)
with open("data.txt", "r", encoding="utf-8-sig") as file:
    file_eu_text = file.read().lower()

res_eu_file = re.compile('[^a-z ]').sub(' ', file_eu_text)

print('\nВыполняем анализ англоязычного текста....\n')
# word_tokens(res_eu_file)
# word_cloud(file_eu_text)
# lemma(res_eu_file)

wc.generate(res_eu_file)

wc.to_file("output.png")

# Организация чтения из файла (русский текст)
with open("translate.txt", "r", encoding="utf-8-sig") as file:
    file_ru_text = file.read().lower()

res_ru_file = re.compile('[^а-ё ]').sub(' ', file_ru_text)

print('\nВыполняем анализ русскоязычного текста....\n')
# word_tokens(res_ru_file)
# word_cloud(file_ru_text)
# lemma_ru(res_ru_file)

wc.generate(res_ru_file)

wc.to_file("output2.png")
