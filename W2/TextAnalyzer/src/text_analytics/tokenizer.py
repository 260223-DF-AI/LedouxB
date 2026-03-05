import re
from collections import Counter
from models import NGram

def tokenize(text):
    """
    Split text into words.
    - Convert to lowercase
    - Remove punctuation
    - Remove extra whitespace
    Returns: List of words
    """
    # string.punctuation
    punctuation = ",.?!"
    text = ''.join(char for char in text if char not in punctuation)
    words = text.lower().strip().split()
    return words

def get_sentences(text):
    """
    Split text into sentences.
    - Handle abbreviations (Dr., Mr., etc.)
    - Handle multiple punctuation (!! or ...)
    Returns: List of sentences
    """
    titles = r'(?<!Dr)(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Prof)(?<!Sr)(?<!Jr)(?<!St)'
    sentences = re.split(titles + r"\.\s+", text)
    return sentences


def get_ngrams(words, n):
    """
    Generate n-grams from a list of words.
    Example: get_ngrams(['a', 'b', 'c'], 2) -> [('a', 'b'), ('b', 'c')]
    Returns: List of tuples
    """

    ngrams: list = []
    for i in range(len(words)-n+1):
        ngrams.append(tuple(words[i:i+n]))

    return ngrams

def remove_stopwords(words, stopwords=None):
    """
    Remove common stopwords from word list.
    Use a default set if stopwords not provided.
    Returns: Filtered list of words
    """
    if not stopwords:
        stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    return list(filter(lambda x: x not in stopwords, words))

# get_ngrams(["a", "b", "c", "d", "e"], 2)

# print(remove_stopwords(["i", "i", "i", "i", "me", "me", "me", "me", "notstopword"]))