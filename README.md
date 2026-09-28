# Sidama IPA Converter & Spell Checker

It was created to assist the transcription of Sidama headwords for an electronic dictionary compiled by native speakers of the language.

## Features
- **Phonetic Conversion:** Automatically transcribes Sidama Latin orthography into International Phonetic Alphabet (IPA). Handles consonant digraphs, geminates, long vowels, and automatic glottal stop recovery during vowel hiatus.
- **Strict Phonotactic Spell Checking:** Validates dictionary headwords against 7 native linguistic rules governing consonant clusters, syllable boundaries, vowel limits, and minimum word requirements.

---

## Installation

If you have downloaded or cloned this repository, you can install it locally for your project via pip:

```bash
pip install -e .

# Usage Example
from sidama_ipa import SidamaSpellChecker

checker = SidamaSpellChecker()

# Test a valid headword
is_valid, msg = checker.validate("madda")
print(is_valid)  # Output: True

# Test an invalid word (violates Rule 3: >2 identical vowels)
is_valid, msg = checker.validate("aaandd")
print(msg)  # Output: Rule 3 violation: Sequence of more than two identical vowels ('aaa') detected.
