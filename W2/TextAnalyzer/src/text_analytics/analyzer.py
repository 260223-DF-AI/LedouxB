from collections import Counter, defaultdict
from .models import WordFrequency, NGram, DocumentStats, AnalysisResult
from .tokenizer import tokenize, get_sentences, get_ngrams, remove_stopwords
from .metrics import calculate_readability

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
        avg_sentence_length = round(sum(sentence_lengths) / len(self.sentences), 1)
        return DocumentStats(
            self.word_counter.total(),
            len(self.unique_words),
            len(get_sentences(self.text)),
            avg_word_length,
            avg_sentence_length
        )

    
    def get_word_length_distribution(self):
        """
        Group words by length.
        Returns: defaultdict mapping length -> list of words
        """
        len_dict = defaultdict(list)
        for w in self.unique_words:
            len_dict[len(w)].append(w)
        return len_dict
    
    def analyze(self, wfn, exclude_stop, bgn, tgn):
        """
        Run complete analysis.
        Returns: AnalysisResult namedtuple
        """
        result = AnalysisResult(
            self.get_document_stats(),
            self.get_word_frequencies(wfn, exclude_stop),
            self.get_bigrams(bgn),
            self.get_trigrams(tgn),
            calculate_readability(self)
        )
        return result