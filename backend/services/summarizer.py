import re
from collections import Counter

def summarize_text(text: str):
    """
    Simple extractive summarization using sentence scoring.
    No model downloads needed.
    """
    if not text or len(text.strip()) < 20:
        return text
    
    # Split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) <= 2:
        return text
    
    # Calculate word frequencies
    words = re.findall(r'\w+', text.lower())
    word_freq = Counter(words)
    
    # Score sentences
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        words_in_sentence = re.findall(r'\w+', sentence.lower())
        score = sum(word_freq[word] for word in words_in_sentence if word in word_freq)
        sentence_scores[i] = score
    
    # Get top 30% of sentences
    num_sentences = max(1, len(sentences) // 3)
    top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
    
    # Maintain original order
    summary_sentences = [sentences[i] for i, _ in sorted(top_sentences)]
    
    return '. '.join(summary_sentences) + '.'