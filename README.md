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
