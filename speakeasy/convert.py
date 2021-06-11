from snowballstemmer import stemmer

from speakeasy.conversion_rules import (
    UNIT_NUMBERS,
    TENS_NUMBERS,
    SCALE_NUMBERS,
    CURRENCY_SYMBOLS,
    QUANTIFIERS,
    stem_dict,
)

UNIT_NUMBERS = stem_dict(UNIT_NUMBERS)
TENS_NUMBERS = stem_dict(TENS_NUMBERS)
SCALE_NUMBERS = stem_dict(SCALE_NUMBERS)
CURRENCY_SYMBOLS = stem_dict(CURRENCY_SYMBOLS)
QUANTIFIERS = stem_dict(QUANTIFIERS)


class SpeakEasyConvertor(object):
    def __init__(self):
        self.__stemmer = stemmer("english")

    @staticmethod
    def __get_family(wrd):
        if wrd in dict(**UNIT_NUMBERS, **TENS_NUMBERS, **SCALE_NUMBERS).keys():
            return 0
        elif wrd in QUANTIFIERS.keys():
            return 1
        elif wrd in CURRENCY_SYMBOLS.keys():
            return 2
        elif len(wrd) == 1 and wrd.isalpha():
            return 3
        else:
            return -1

    @staticmethod
    def __words_to_numbers(buffer):
        reduced_buffer = []
        n = len(buffer)
        i = n - 1
        while i >= 0:
            if buffer[i][1] == "s":
                cur = 1
                for j in range(i, -1, -1):
                    cur = buffer[j][0] * cur
                    if buffer[j][1] != "s":
                        i -= i - j
                        break
                reduced_buffer.append((cur, "s"))
            else:
                reduced_buffer.append(buffer[i])
            i -= 1
        reduced_buffer.reverse()

        final_buffer = []
        for i in range(len(reduced_buffer)):
            cur = reduced_buffer[i]
            if i > 0:
                if final_buffer[0][1] == "s":
                    final_buffer[0] = (final_buffer[0][0] + cur[0], cur[1])
                elif final_buffer[0][1] == "t":
                    if cur[1] == "t":
                        final_buffer[0] = (int(f"{final_buffer[0][0]}{cur[0]}"), cur[1])
                    else:
                        final_buffer[0] = (final_buffer[0][0] + cur[0], cur[1])
                else:
                    final_buffer[0] = (int(f"{final_buffer[0][0]}{cur[0]}"), cur[1])
            else:
                final_buffer.append(cur)

        return int(final_buffer[0][0])

    def convert(self, text):
        sentence = []
        buffer = []

        i = 0
        text = text.split()
        prev = None

        while i < len(text):
            wrd = self.__stemmer.stemWord(text[i].lower())
            family = self.__get_family(wrd)
            if family == 3 and prev not in (-1, 3) and i != 0:
                family = -1

            if family == -1:
                if prev == 1:
                    if len(wrd) == 1:
                        sentence.append(QUANTIFIERS[buffer[0]] * text[i])
                    else:
                        sentence.extend([buffer[0][0], text[i]])

                    buffer.clear()
                elif prev == 0:
                    if wrd != "and":
                        sentence.extend([self.__words_to_numbers(buffer), text[i]])
                        buffer.clear()
                elif prev == 3:
                    sentence.append(buffer[0])
                    sentence.append(text[i])
                    buffer.clear()
                else:
                    sentence.append(text[i])
            elif family == 0:
                if prev == 3:
                    sentence.append("".join(buffer))
                    buffer.clear()
                if wrd in UNIT_NUMBERS:
                    n = UNIT_NUMBERS[wrd]
                    buffer.append((n, "u"))
                elif wrd in TENS_NUMBERS:
                    n = TENS_NUMBERS[wrd]
                    buffer.append((n, "t"))
                else:
                    n = SCALE_NUMBERS[wrd]
                    buffer.append((n, "s"))
            elif family == 1:
                if prev == 3:
                    sentence.append("".join(buffer))
                    buffer.clear()
                if prev == 0:
                    sentence.append(self.__words_to_numbers(buffer))
                elif prev == 1:
                    sentence.append(buffer[0])

                buffer.clear()
                buffer.append(wrd)
            elif family == 2:
                if prev == 3:
                    sentence.append("".join(buffer))
                    buffer.clear()
                if prev == 0:
                    if wrd == "cent":
                        sentence.append(
                            f"{self.__words_to_numbers(buffer)}{CURRENCY_SYMBOLS[wrd]}"
                        )
                    else:
                        sentence.append(
                            f"{CURRENCY_SYMBOLS[wrd]}{self.__words_to_numbers(buffer)}"
                        )
                    buffer.clear()
                else:
                    sentence.append(text[i])
            elif family == 3:
                buffer.append(text[i])

            prev = family
            i += 1

        if len(buffer) > 0:
            if prev == 0:
                sentence.append(self.__words_to_numbers(buffer))
            elif prev == 1:
                sentence.append(text[i - 1])
            elif prev == 3:
                sentence.append("".join(buffer))
        return " ".join(map(str, sentence))
