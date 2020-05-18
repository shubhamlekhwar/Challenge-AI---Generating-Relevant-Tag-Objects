from summarizer import Summarizer, TransformerSummarizer
from tag_skill.services.text_preprocess_extractor import remove_stopwords_POS
import nltk


def summerize(input_text):
    model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
    summary = ''.join(model(input_text, min_length=60, max_length=500))
    return summary


def pos_tagger(input_text):
    tokens=remove_stopwords_POS(input_text)
    tagged_token = nltk.pos_tag(tokens)
    phrase = ''
    i=1
    for word in tagged_token:
        if i == 3:
            break
        if word[1] == 'NN' or word[1] == 'NN' == 'VBP':
            phrase = phrase + ' ' + word[0]
            i=i+1
    return phrase



