def find_anagrams(word, candidates):
    word_lower = word.lower()
    sorted_word = sorted(word_lower)
    anagrams = []
    for candidate in candidates:
        cand_lower = candidate.lower()
        if cand_lower == word_lower:
            continue
        if sorted(cand_lower) == sorted_word:
            anagrams.append(candidate)
    return anagrams
