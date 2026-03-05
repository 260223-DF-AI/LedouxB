import re

def flesch_reading_ease(word_count, sentence_count, syllable_count):
    """
    Calculate Flesch Reading Ease score.
    Formula: 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
    
    Score interpretation:
    - 90-100: Very easy (5th grade)
    - 60-70: Standard (8th-9th grade)
    - 30-50: Difficult (college)
    - 0-30: Very difficult (college graduate)
    """
    return 206.835 - (1.015 * (word_count/sentence_count)) - (84.6 * (syllable_count/word_count))

def count_syllables(word):
    """
    Count syllables in a word.
    Simple heuristic: count vowel groups.
    """
    vowel_groups = re.findall('[aeiouAEIOU]+', word)
    return len(vowel_groups)

def calculate_readability(analyzer):
    """
    Calculate readability metrics for an analyzed document.
    Returns: Dict with various readability scores
    """
    num_syllables = sum(count_syllables(w) for w in analyzer.words)
    score = flesch_reading_ease(len(analyzer.words), len(analyzer.sentences), num_syllables)
    return {"score": score,
            #descriptions
            }