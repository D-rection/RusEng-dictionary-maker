import requests
import re


def ru_en(t):
    en = [chr(i) for i in range(65, 123)]
    for i in t[:5]:
        if i in en:
            return 'en-ru'
        else:
            return 'ru-en'


def translate_yandex(text):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    KEY = 'trnsl.1.1.20160119T035517Z.50c6906978ef1961.08d0c5ada49017ed764c042723895ffab867be7a'
    TEXT = text
    LANG = ru_en(text)
    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    return r.text[r.text.find('['):-1]


def get_file_content(filename):
    content_reader = open(filename, 'r')
    content = content_reader.read()
    content_reader.close()
    return content


def write_in_file(filename, content, dictionary):
    content_writer = open(filename, 'w')
    for word in content:
        format_word = dictionary[word][2:-2]
        line = word + " - " + format_word + '\n'
        content_writer.write(line)
    content_writer.close()


def magic():
    eng_text = get_file_content("eng_text.txt")
    words_in_text = re.split(r'\W',eng_text)
    dictionary = {}
    array = []
    for word in words_in_text:
        if word != "" :
            if word not in dictionary:
                trnslt = translate_yandex(word)
                dictionary[word] = trnslt
            array.append(word)
    write_in_file("dictionary.txt", array, dictionary)


magic()