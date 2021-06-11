from snowballstemmer import stemmer

UNIT_NUMBERS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
}

TENS_NUMBERS = {
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

SCALE_NUMBERS = {
    "hundred": 100,
    "thousand": 1000,
    "million": 1e6,
    "billion": 1e9,
    "crore": 1e7,
    "lakh": 1e5,
}

QUANTIFIERS = {
    "single": 1,
    "double": 2,
    "triple": 3,
    "quadruple": 4,
    "quintuple": 5,
    "sextuple": 6,
    "septuble": 7,
    "octuple": 8,
    "nonuple": 9,
    "decuple": 10,
}

CURRENCY_SYMBOLS = {
    "cent": "¢",
    "dollar": "$",
    "rupee": "₹",
    "pound": "£",
    "euro": "€",
    "yen": "¥",
    "won": "₩",
    "franc": "CHF",
    "ruble": "RUB",
    "peso": "₱",
}

stemmer = stemmer("english")


def stem_dict(dic: dict) -> dict:
    new_dict = {}
    for i in dic:
        new_dict[stemmer.stemWord(i)] = dic[i]
    return new_dict
