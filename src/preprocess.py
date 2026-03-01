import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download required resources (only first time)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


def preprocess(text):
    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove digits
    text = re.sub(r'\d+', '', text)

    # Tokenize
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    tokens = [t for t in tokens if t not in stop_words]

    # Stemming
    tokens = [stemmer.stem(t) for t in tokens]

    return " ".join(tokens)