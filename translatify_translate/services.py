from textblob import TextBlob
from textblob.exceptions import NotTranslated

from .models import TranslatedPhrase


def translate_phrase(in_phrase, destination_lang='en'):
    """ Returns a TranslatedPhrase object containing the translated phrase.

        Arguments:
            in_phrase (str): The phrase to translate
            destination_lang (str): The language to translate the phrase to; 'en'
                (English) by default
        Returns:
            (TranslatedPhrase)
    """

    try:
        in_blob = TextBlob(in_phrase)
        detected_lang = in_blob.detect_language()
        translated_blob = str(in_blob.translate(to=destination_lang))
    except NotTranslated:
        detected_lang = 'xx'
        translated_blob = in_phrase
    return TranslatedPhrase(input_phrase=in_phrase, input_language=detected_lang, output_phrase=translated_blob)
