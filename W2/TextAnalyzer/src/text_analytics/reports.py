from collections import OrderedDict
from datetime import date
from .analyzer import TextAnalyzer
from .models import *

def generate_text_report(analysis_result: AnalysisResult, output_path: str):
    """
    Generate a formatted text report.
    
    Sections:
    1. Document Overview
    2. Top Words
    3. Top Phrases (bigrams/trigrams)
    4. Readability Assessment
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=== Text Analysis Report ===\n")
        f.write(f"Generated: {date.today()}\n\n")
        ds = analysis_result.document_stats
        f.write(
f"""Document Statistics:
- Word Count: {ds.word_count}
- Unique Words: {ds.unique_words}
- Sentence Count: {ds.sentence_count}
- Average Word Length: {ds.avg_word_length} characters
- Average Sentence Length: {ds.avg_sentence_length} words
""")
        f.write(f"\nTop {len(analysis_result.top_words)} Words:\n")
        f.write(generate_frequency_table(analysis_result.top_words))
        f.write(f"\nTop {len(analysis_result.top_bigrams)} Bigrams:\n")
        for i, b in enumerate(analysis_result.top_bigrams, 1):
            f.write(f"{i}. \"{b[0]}\" ({b[1]})\n")
        f.write(
f"""\nReadability:
- Flesch Reading Ease: {analysis_result.readability_score[0]} ({analysis_result.readability_score[1]})
"""
        )
        

def generate_word_cloud_data(word_frequencies: list[WordFrequency]) -> OrderedDict:
    """
    Prepare data for word cloud visualization.
    Returns: OrderedDict of word -> weight (ordered by frequency)
    """

    data: OrderedDict = OrderedDict()
    for wf in word_frequencies:
        data[wf.word] = wf.percentage
    return data
    
    

def generate_frequency_table(word_frequencies):
    """
    Generate a formatted frequency table.
    Uses OrderedDict to maintain ranking order.
    """
    table: str = ""
    # frequency_table = generate_word_cloud_data(word_frequencies)
    for i, word_freq in enumerate(word_frequencies, 1):
        table += f"{i}. {word_freq.word} ({word_freq.count}) - {word_freq.percentage}%\n"
        
    return table