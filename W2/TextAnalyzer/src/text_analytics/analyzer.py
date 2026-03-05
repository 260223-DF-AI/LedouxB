from collections import Counter, defaultdict
from models import WordFrequency, NGram, DocumentStats, AnalysisResult
from tokenizer import tokenize, get_sentences, get_ngrams, remove_stopwords
from metrics import calculate_readability

class TextAnalyzer:
    """Analyzes text documents for various metrics."""
    
    def __init__(self, text):
        self.text = text
        self.words = tokenize(text)
        self.unique_words = set(self.words)
        self.sentences = get_sentences(text)
        self.word_counter = Counter(self.words)
        self.total_words = sum(self.word_counter.values())
    
    def get_word_frequencies(self, top_n=20, exclude_stopwords=True):
        """
        Get top N word frequencies.
        Returns: List of WordFrequency namedtuples
        """
        if exclude_stopwords:
            self.words = remove_stopwords(self.words)

        counter = Counter(self.words)
        top_common = counter.most_common(top_n)
        common_words = [WordFrequency(word, n, round((n / self.total_words) * 100 , 2)) for word,n in top_common]

        return common_words
    
    def get_bigrams(self, top_n=10):
        """
        Get top N bigrams (2-word phrases).
        Returns: List of NGram namedtuples
        """
        bigrams = get_ngrams(self.words, 2)
        
        counter = Counter(bigrams)

        return counter.most_common(top_n)
    
    def get_trigrams(self, top_n=10):
        """
        Get top N trigrams (3-word phrases).
        Returns: List of NGram namedtuples
        """
        trigrams = get_ngrams(self.words, 3)
        
        counter = Counter(trigrams)

        return counter.most_common(top_n)
    
    def get_document_stats(self):
        """
        Calculate overall document statistics.
        Returns: DocumentStats namedtuple
        """
        word_lengths = [len(word) for word in self.words]
        sentence_lengths = [len(s) for s in self.sentences]
        avg_word_length = round(sum(word_lengths) / len(self.words), 2)
        avg_sentence_length = round(sum(sentence_lengths) / len(self.sentences), 2)
        return DocumentStats(self.word_counter.total(), len(self.unique_words), len(get_sentences(self.text)), avg_word_length, avg_sentence_length)

    
    def get_word_length_distribution(self):
        """
        Group words by length.
        Returns: defaultdict mapping length -> list of words
        """
        len_dict = defaultdict(list)
        for w in self.unique_words:
            len_dict[len(w)].append(w)
        return len_dict
    
    def analyze(self):
        """
        Run complete analysis.
        Returns: AnalysisResult namedtuple
        """
        result = AnalysisResult(
            self.get_document_stats(),
            self.get_word_frequencies(),
            self.get_bigrams(),
            self.get_trigrams(),
            calculate_readability(self)
        )
        return result

text1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
text2 = """
I AM SAM. I AM SAM. SAM I AM.

THAT SAM-I-AM! THAT SAM-I-AM! I DO NOT LIKE THAT SAM-I-AM!

DO WOULD YOU LIKE GREEN EGGS AND HAM?

I DO NOT LIKE THEM,SAM-I-AM.
I DO NOT LIKE GREEN EGGS AND HAM.

WOULD YOU LIKE THEM HERE OR THERE?

I WOULD NOT LIKE THEM HERE OR THERE.
I WOULD NOT LIKE THEM ANYWHERE.
I DO NOT LIKE GREEN EGGS AND HAM.
I DO NOT LIKE THEM, SAM-I-AM.

WOULD YOU LIKE THEM IN A HOUSE?
WOULD YOU LIKE THEN WITH A MOUSE?

I DO NOT LIKE THEM IN A HOUSE.
I DO NOT LIKE THEM WITH A MOUSE.
I DO NOT LIKE THEM HERE OR THERE.
I DO NOT LIKE THEM ANYWHERE.
I DO NOT LIKE GREEN EGGS AND HAM.
I DO NOT LIKE THEM, SAM-I-AM.

WOULD YOU EAT THEM IN A BOX?
WOULD YOU EAT THEM WITH A FOX?

NOT IN A BOX. NOT WITH A FOX.
NOT IN A HOUSE. NOT WITH A MOUSE.
I WOULD NOT EAT THEM HERE OR THERE.
I WOULD NOT EAT THEM ANYWHERE.
I WOULD NOT EAT GREEN EGGS AND HAM.
I DO NOT LIKE THEM, SAM-I-AM.

WOULD YOU? COULD YOU? IN A CAR?
EAT THEM! EAT THEM! HERE THEY ARE.

I WOULD NOT, COULD NOT, IN A CAR.

YOU MAY LIKE THEM. YOU WILL SEE.
YOU MAY LIKE THEM IN A TREE!

I WOULD NOT, COULD NOT IN A TREE.
NOT IN A CAR! YOU LET ME BE.
I DO NOT LIKE THEM IN A BOX.
I DO NOT LIKE THEM WITH A FOX.
I DO NOT LIKE THEM IN A HOUSE.
I DO NOT LIKE THEM WITH A MOUSE.
I DO NOT LIKE THEM HERE OR THERE.
I DO NOT LIKE THEM ANYWHERE.
I DO NOT LIKE GREEN EGGS AND HAM.
I DO NOT LIKE THEM, SAM-I-AM.

A TRAIN! A TRAIN! A TRAIN! A TRAIN!
COULD YOU, WOULD YOU ON A TRAIN?

NOT ON TRAIN! NOT IN A TREE!
NOT IN A CAR! SAM! LET ME BE!
I WOULD NOT, COULD NOT, IN A BOX.
I WOULD NOT, COULD NOT, WITH A FOX.
I WILL NOT EAT THEM IN A HOUSE.
I WILL NOT EAT THEM HERE OR THERE.
I WILL NOT EAT THEM ANYWHERE.
I DO NOT EAT GREEM EGGS AND HAM.
I DO NOT LIKE THEM, SAM-I-AM.

SAY! IN THE DARK? HERE IN THE DARK!
WOULD YOU, COULD YOU, IN THE DARK?

I WOULD NOT, COULD NOT, IN THE DARK.

WOULD YOU COULD YOU IN THE RAIN?

I WOULD NOT, COULD NOT IN THE RAIN.
NOT IN THE DARK. NOT ON A TRAIN.
NOT IN A CAR. NOT IN A TREE.
I DO NOT LIKE THEM, SAM, YOU SEE.
NOT IN A HOUSE. NOT IN A BOX.
NOT WITH A MOUSE. NOT WITH A FOX.
I WILL NOT EAT THEM HERE OR THERE.
I DO NOT LIKE THEM ANYWHERE!

YOU DO NOT LIKE GREEN EGGS AND HAM?

I DO NOT LIKE THEM, SAM-I-AM.

COULD YOU, WOULD YOU, WITH A GOAT?

I WOULD NOT, COULD NOT WITH A GOAT!

WOULD YOU, COULD YOU, ON A BOAT?

I COULD NOT, WOULD NOT, ON A BOAT.
I WILL NOT, WILL NOT, WITH A GOAT.
I WILL NOT EAT THEM IN THE RAIN.
NOT IN THE DARK! NOT IN A TREE!
NOT IN A CAR! YOU LET ME BE!
I DO NOT LIKE THEM IN A BOX.
I DO NOT LIKE THEM WITH A FOX.
I WILL NOT EAT THEM IN A HOUSE.
I DO NOT LIKE THEM WITH A MOUSE.
I DO NOT LIKE THEM HERE OR THERE.
I DO NOT LIKE THEM ANYWHERE!
I DO NOT LIKE GREEN EGGS AND HAM!
I DO NOT LIKE THEM, SAM-I-AM.

YOU DO NOT LIKE THEM. SO YOU SAY.
TRY THEM! TRY THEM! AND YOU MAY.
TRY THEM AND YOU MAY, I SAY.

sAM! IF YOU LET ME BE,
I WILL TRY THEM. YOU WILL SEE.

(... and he tries them ...)

SAY! I LIKE GREEN EGGS AND HAM!
I DO! I LIKE THEM, SAM-I-AM!
AND I WOULD EAT THEM IN A BOAT.
AND I WOULD EAT THEM WITH A GOAT...
AND I WILL EAT THEM, IN THE RAIN.
AND IN THE DARK. AND ON A TRAIN.
AND IN A CAR. AND IN A TREE.
THEY ARE SO GOOD, SO GOOD, YOU SEE!
SO I WILL EAT THEM IN A BOX.
AND I WILL EAT THEM WITH A FOX.
AND I WILL EAT THEM IN A HOUSE.
AND I WILL EAT THEM WITH A MOUSE.
AND I WILL EAT THEM HERE AND THERE.
SAY! I WILL EAT THEM ANYWHERE!
I DO SO LIKE GREEN EGGS AND HAM!
THANK YOU! THANK YOU, SAM I AM.
"""
analyzer = TextAnalyzer(text1)
# print(analyzer.get_word_frequencies())
# print(analyzer.get_trigrams())
# print(analyzer.get_document_stats())
# print(analyzer.get_word_length_distribution())
print(analyzer.analyze())