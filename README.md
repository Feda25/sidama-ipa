# Sidama IPA Converter & Spell Checker

It was created to assist the transcription of Sidama headwords for an electronic dictionary compiled by native speakers of the language.

## Features
- **Phonetic Conversion:** Automatically transcribes Sidama Latin orthography into International Phonetic Alphabet (IPA). Handles consonant digraphs (`ch`, `ny`, `dh`, etc.), geminates (`madːa`), long vowels (`aː`), and automatic glottal stop recovery (`kaʔe`) during vowel hiatus.
- **Strict Phonotactic Spell Checking:** Validates dictionary headwords against 7 native linguistic rules governing consonant clusters, syllable boundaries, vowel limits, and minimum word requirements.

---

## The 7 Phonotactic Rules Enforced
1. Consonant clusters are limited to two phonemes and occur strictly intervocalically.
2. Consonant clusters cannot begin or end a word.
3. No more than two identical consecutive vowels are allowed.
4. Sequences of dissimilar vowels trigger glottal stop insertion.
5. Long vowels can appear in any position (initial, medial, or final).
6. The shortest valid word requires at least one vowel and one consonant.
7. Words cannot consist of only vowels or only consonants.

---

## Installation

If you have downloaded or cloned this repository, you can install it locally for your project via pip:

```bash
pip install -e .

# Usage example one 
from sidama_ipa import SidamaSpellChecker

checker = SidamaSpellChecker()

# Test a valid headword
is_valid, msg = checker.validate("madda")
print(is_valid)  # Output: True

# Test an invalid word (violates Rule 3: >2 identical vowels)
is_valid, msg = checker.validate("aaandd")
print(msg)  # Output: Rule 3 violation: Sequence of more than two identical vowels ('aaa') detected.

# Usage example two
from sidama_ipa import SidamaIPAConverter, SidamaSpellChecker

converter = SidamaIPAConverter()
checker = SidamaSpellChecker()

headwords = ["chanya", "aaandd", "maaeela", "mm", "giddo"]

print(f"{'Headword':<10} | {'Status':<8} | {'IPA / Error Message'}")
print("-" * 50)

for word in headwords:
    is_valid, message = checker.validate(word)
    if is_valid:
        ipa = converter.convert(word)
        print(f"{word:<10} | {'Valid':<8} | /{ipa}/")
    else:
        print(f"{word:<10} | {'Invalid':<8} | {message}")

