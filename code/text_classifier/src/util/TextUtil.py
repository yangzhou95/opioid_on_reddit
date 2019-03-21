import string
import nltk
from nltk.corpus import stopwords
import enchant


class TextUtil:

    SHORT_WORD_LENGTH = 3

    _exclude = []
    _stop_words = set(stopwords.words('english'))
    _english_words = enchant.Dict("en_us")

    def purify_string(self, s: str):

        # remove punctuations
        s = ''.join(ch for ch in s if ch not in self._exclude)
        # remove number
        s = ''.join(ch for ch in s if not ch.isdigit())

        # remove short words
        list_of_words = s.split()
        for w in list_of_words:
            if len(w) < self.SHORT_WORD_LENGTH:
                list_of_words.remove(w)

        # remove stop words
        delete_stop_words = [word for word in list_of_words if word.lower() not in self._stop_words]

        # rmove non-english words
        filtered_words = [word.lower() for word in delete_stop_words if self._english_words.check(word.decode('utf-8'))]

        # filtered_words_2 = [ lmtzr.lemmatize(word) for word in filtered_words ]

        return ' '.join(filtered_words)

