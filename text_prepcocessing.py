# we will define sample cases and will divide the function on analysis and cleaning of the preprocessed test 
# so two function needed 
# celan text and Analyse text

# imports 
import re
import  nltk
nltk.download('stopwords')
from nltk.corpus import stopwords as nltk_stopwords


# DEFAULT LISTS
SPECIAL_CHARCTERS_REGEX = re.compile("""[~` !@#$%\^&*\(\)\-_\+=\{\}\[\]\|\\/:;"'<>,\.\?]""")
SPECIAL_CHARCTERS = """~`!@#$%^&*()-_+={}[]|\/:;"'<>,.?"""
HASHTAG_REGEX = re.compile("#[a-zA-Z0-9]+")
EMAIL_REGEX = re.compile('\s[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}\s')

def celan_sentences(list_of_sentences, case=True, hashtag=True, special_char=True, special_chars=SPECIAL_CHARCTERS,
                     email=True,stopword=True,stopwords=[],stopwords_language = 'english',
                     root_form=True,root_method='Lemmatization'):
    
    """takes a list of sentences as input and return the same list of sentences after cleaning them
    current implementation with switches :
    1. lowercase
    2. removal of Hashtags
    3. removal of special characters 
    4. emails
    5. stopwords 
    6. reduction to root form using Lemmatization[default] or stemming 
    """
    stopwords = set(stopwords or nltk_stopwords.words(stopwords_language))
    print(stopwords)
    cleaned_sentences = []
    for sentence in list_of_sentences:
        sentence = sentence.lower()
        sentence = re.sub(HASHTAG_REGEX,'',sentence)
        sentence = re.sub(EMAIL_REGEX,'',sentence)
        sentence = "".join(filter(lambda x : x not in special_chars,sentence)).strip()
        sentence = " ".join([w for w in sentence.split(" ") if w not in stopwords ])
        cleaned_sentences.append(sentence)

    return cleaned_sentences
    