"""
Language generation starter
"""

import os
from lab_4.main import tokenize_by_letters, LetterStorage, \
     encode_corpus, LanguageProfile, decode_sentence, NGramTextGenerator,\
     LikelihoodBasedTextGenerator, translate_sentence_to_plain_text

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    def score_4():
        print('--point 4--')
        with open(os.path.join(PATH_TO_LAB_FOLDER, 'reference_text.txt'), 'r', encoding="utf-8") \
                as file:
            text = file.read()
        tokenized_text = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized_text)
        number_of_letters = storage.get_letter_count()
        the_lowest_id = list(storage.storage.items())[:5]
        the_highest_id = list(storage.storage.items())[-5:]
        print('Number of letters = {} '.format(number_of_letters))
        print('Letters with the lowest id: {}'.format(the_lowest_id))
        print('Letters with the highest id: {}'.format(the_highest_id))
        return number_of_letters, the_lowest_id, the_highest_id


    def score_6():
        print ('--point 6--')
        with open(os.path.join(PATH_TO_LAB_FOLDER, 'reference_text.txt'), 'r', encoding="utf-8") \
                as file:
            text = file.read()
        tokenized_text = tokenize_by_letters(text)
        storage = LetterStorage()
        storage.update(tokenized_text)
        encoded_text = encode_corpus(storage, tokenized_text)
        language_profile = LanguageProfile(storage, 'en')
        language_profile.create_from_tokens(encoded_text, (2,))

        generator = NGramTextGenerator(language_profile)
        for length in range(5, 10):
            generated_text = generator.generate_sentence((1,), length)
            decoded_text = decode_sentence(storage, generated_text)
            RESULT = translate_sentence_to_plain_text(decoded_text)
            print(RESULT)

    def score_8():
        print('--point 8--')
        with open(os.path.join(PATH_TO_LAB_FOLDER, 'reference_text.txt'), 'r', encoding="utf-8") \
                as file:
            text = file.read()
        storage = LetterStorage()
        storage.update(tokenize_by_letters(text))
        encoded_corpus = encode_corpus(storage, tokenize_by_letters(text))
        language_profile = LanguageProfile(storage, 'en')
        language_profile.create_from_tokens(encoded_corpus, (2,))
        generated_text = LikelihoodBasedTextGenerator(language_profile)
        sentences = []
        for length in range(5, 10):
            sentences.append(generated_text.generate_decoded_sentence((1,), length))
        return sentences
    score_4()
    score_6()
    RESULT = score_8()
    print(RESULT)

    # find the appropriate start.py task in your lab_4 description file
    # your code goes here

    # RESULT = ''
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Detection not working'
