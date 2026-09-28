"""
Sidama IPA Converter & Spell Checker Library
Created to assist the transcription of Sidama headwords for an electronic dictionary 
compiled by native speakers of the language.
"""

class SidamaIPAConverter:
    """
    A converter for translating Sidama Latin orthography 
    into International Phonetic Alphabet (IPA) representation.
    """
    def __init__(self):
        self.digraphs = {
            'ch': 'tʃ', 'dh': 'ɗ', 'ny': 'ɲ', 'ph': 'pʼ',
            'sh': 'ʃ', 'ts': 'sʼ', 'zh': 'ʒ'
        }
        self.singles = {
            '’': 'ʔ', 'b': 'b', 'c': 'tʃʼ', 'd': 'd', 'f': 'f',
            'g': 'g', 'h': 'h', 'j': 'dʒ', 'k': 'k', 'l': 'l',
            'm': 'm', 'n': 'n', 'p': 'p', 'q': 'kʼ', 'r': 'r',
            's': 's', 't': 't', 'v': 'v', 'w': 'w', 'x': 'tʼ',
            'y': 'j', 'z': 'z', 'a': 'a', 'e': 'e', 'i': 'i',
            'o': 'o', 'u': 'u'
        }
        self.vowels = set("aeiou")

    def convert(self, text: str) -> str:
        if not text:
            return ""
        text = text.lower()
        raw_tokens = []
        i, n = 0, len(text)
        
        while i < n:
            if i < n - 1 and text[i] == text[i+1] and text[i] in self.singles:
                ipa_char = self.singles[text[i]]
                raw_tokens.append(ipa_char + 'ː')
                i += 2
            elif i < n - 1 and text[i:i+2] in self.digraphs:
                raw_tokens.append(self.digraphs[text[i:i+2]])
                i += 2
            elif text[i] in self.singles:
                raw_tokens.append(self.singles[text[i]])
                i += 1
            else:
                raw_tokens.append(text[i])
                i += 1
                
        final_result = []
        for idx in range(len(raw_tokens)):
            final_result.append(raw_tokens[idx])
            if idx < len(raw_tokens) - 1:
                curr_base = raw_tokens[idx].rstrip('ː')
                nxt_base = raw_tokens[idx+1].rstrip('ː')
                if curr_base in self.vowels and nxt_base in self.vowels and curr_base != nxt_base:
                    final_result.append('ʔ')
                    
        return "".join(final_result)


class SidamaSpellChecker:
    """
    Validates Sidama orthography based on the 7 structural phonotactic rules:
    1) Clusters limited to two phonemes and occur only intervocalically.
    2) Clusters cannot begin or end a word.
    3) No more than two identical consecutive vowels allowed.
    4) Dissimilar vowel hiatus triggers glottal stops.
    5) Long vowels can come in any position.
    6) The shortest word has at least one vowel and one consonant.
    7) Vowels or consonants alone cannot make a word.
    """
    def __init__(self):
        self.vowels = set("aeiou")
        self.consonants = set("bcdfghjklmnpqrstvwxyz’")

    def validate(self, word: str) -> tuple[bool, str]:
        word = word.lower()
        if not word:
            return False, "Word is empty."

        for v in self.vowels:
            if v * 3 in word:
                return False, f"Rule 3 violation: Sequence of more than two identical vowels ('{v*3}') detected."

        tokens = []
        i, n = 0, len(word)
        digraphs = {'ch', 'dh', 'ny', 'ph', 'sh', 'ts', 'zh'}
        
        while i < n:
            if i < n - 1 and word[i] == word[i+1] and word[i] in self.vowels:
                tokens.append(word[i:i+2])
                i += 2
            elif i < n - 1 and word[i] == word[i+1] and word[i] in self.consonants:
                tokens.append(word[i:i+2])
                i += 2
            elif i < n - 1 and word[i:i+2] in digraphs:
                tokens.append(word[i:i+2])
                i += 2
            else:
                tokens.append(word[i])
                i += 1

        is_vowel = lambda t: t[0] in self.vowels or t in self.vowels

        has_vowel = any(is_vowel(t) for t in tokens)
        has_consonant = any(not is_vowel(t) and t != '’' for t in tokens)

        if not has_vowel or not has_consonant:
            return False, "Rule 6/7 violation: A word cannot consist of only vowels or only consonants."

        if len(tokens) >= 2:
            first_is_c = not is_vowel(tokens[0]) and tokens[0] != '’'
            second_is_c = not is_vowel(tokens[1]) and tokens[1] != '’'
            if first_is_c and second_is_c:
                return False, "Rule 2 violation: Word cannot begin with a consonant cluster."

            last_is_c = not is_vowel(tokens[-1]) and tokens[-1] != '’'
            second_last_is_c = not is_vowel(tokens[-2]) and tokens[-2] != '’'
            if last_is_c and second_last_is_c:
                return False, "Rule 2 violation: Word cannot end with a consonant cluster."

        for idx in range(len(tokens) - 1):
            curr_is_c = not is_vowel(tokens[idx])
            next_is_c = not is_vowel(tokens[idx+1])
            
            if curr_is_c and next_is_c:
                pre_is_vowel = (idx > 0 and is_vowel(tokens[idx-1]))
                post_is_vowel = (idx + 2 < len(tokens) and is_vowel(tokens[idx+2]))
                
                if not (pre_is_vowel and post_is_vowel):
                    return False, f"Rule 1 violation: Consonant cluster '{tokens[idx]}{tokens[idx+1]}' is not strictly intervocalic."

        return True, "Word is valid."
