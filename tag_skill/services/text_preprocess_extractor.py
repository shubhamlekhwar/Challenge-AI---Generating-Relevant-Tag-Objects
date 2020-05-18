import nltk
import string
import re
from nltk.corpus import stopwords
from skill_tagging.settings import BASE_DIR

stop_words = stopwords.words('english')

stopword_filepath = BASE_DIR + '/tag_skill/resources/stopword.txt'

with open(stopword_filepath) as f:
    stop_words = {line.rstrip() for line in f}

def text_preprocesing_emsi(input_data):
    data = remove_html(input_data)
    text = remove_url(data)
    text = text.replace(u'\t', '')
    text = re.sub(r'\n+', '\n', text).strip()
    text = text.replace(u'[#:}{[]/\\]', ' ')
    text = text.replace(u'?', '')
    text = text.replace(u'_', '')
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    text = text.lower()
    # text = remove_stopwords(text)
    return text


def text_preprocesing_summerizer(input_data):
    data = remove_html(input_data)
    text = remove_url(data)
    text = re.sub(r"\\t", '', text)
    text = re.sub(r'\\n+', '\n', text).strip()
    text = text.replace("&nbsp", "")
    text = text.replace("&rdquo", "")
    text = text.replace("&rsquo", "")
    text = text.replace("&ldquo", "")
    text = text.replace("&lsquo", "")
    text = text.replace("&ndash", "")
    text = text.replace("&quot", "")
    text = re.sub(r'\(.*\)', '', text)
    text = re.sub(r'\[.*\]', '', text)
    text = re.sub(r'\{.*\}', '', text)
    text = text.replace(u';', '')
    text = text.replace(u'\S*@\S*\s?', "")
    pattern = '[0-9]'
    text = re.sub(pattern, '', text)
    text = re.sub('[&#$]', '', text)
    text = re.sub(' {2,}', ' ', text)
    text = text.replace(u'\n', ' ')

    text = remove_stopwords(text)
    print(text)
    return text.strip()


def remove_html(text):
    html = re.compile(r'<.*?>')
    return html.sub(r'', text)


def remove_url(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www.\S+", "", text)
    text = re.sub(r"/\S+", "", text)
    return  text


def remove_stopwords(text):
    tokens = nltk.tokenize.word_tokenize(text)
    filtered_text = ' '.join([w for w in tokens if not w in stop_words])
    return filtered_text

def remove_stopwords_POS(text):
    tokens = nltk.tokenize.word_tokenize(text)
    filtered_text = [w for w in tokens if not w in stop_words]
    return filtered_text


