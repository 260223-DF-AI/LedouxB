from collections import Counter, defaultdict
from models import WordFrequency, NGram, DocumentStats, AnalysisResult
from tokenizer import tokenize, get_sentences, get_ngrams, remove_stopwords

class TextAnalyzer:
    """Analyzes text documents for various metrics."""
    
    def __init__(self, text):
        self.text = text
        self.words = tokenize(text)
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
        
        # Get frequency of n-grams
        
        # Sort n-grams by frequency

        # Return top n
    
    def get_trigrams(self, top_n=10):
        """
        Get top N trigrams (3-word phrases).
        Returns: List of NGram namedtuples
        """
        pass
    
    def get_document_stats(self):
        """
        Calculate overall document statistics.
        Returns: DocumentStats namedtuple
        """
        pass
    
    def get_word_length_distribution(self):
        """
        Group words by length.
        Returns: defaultdict mapping length -> list of words
        """
        pass
    
    def analyze(self):
        """
        Run complete analysis.
        Returns: AnalysisResult namedtuple
        """
        pass

analyzer = TextAnalyzer("hello hello hello hello !! ! ! 1! my name is ben i like to go partying and get crunkt")
print(analyzer.get_word_frequencies())