## SPEAKEASY

A simple library that gives you the functionality of converting
spoken english to written english. The only secondary dependency used was the snowball stemmer to stem plurals for ease of conversion.

Conversion features include:
- Quantifiers:
"Quadruple H" => "HHHH" , "Triple H" => "HHH"
  
- Number Comprehension:
"Forty five" => "45" , "Fifty Thousand Fifty" => "50050"

- Currency Symbols:
"four dollars" => "$4"

- Abbreviations:
"H T M L" => "HTML"

### Logic behind the implementation

We iterate over each word in the input string and keep track of its family (Quantifier, number, currency or abbreviation) and the family of the previous word.
We then maintain two arrays: sentence and buffer. The buffer is where we append modifiers like quantifiers, quantifiers, abbreviations or nested numbers(eg: forty thousand five hundred fifty six) and carry out the specific modification. After all modifiers are computed we append the contents of the buffer to the sentence which is the final array, that
we join as a string to return as the output.

### Installation

To install the library, simply clone the repo and in the root folder run:
```
python setup.py install
```

### Usage

Then to use it in an example:
1. import the SpeakEasyConvertor class
```
>>> from speakeasy.convert import SpeakEasyConvert
```
2. create a convertor object
```
>>> convertor = SpeakEasyConvertor()
```
3. use the convert method on any string you wish to convert
```
>>> txt = "I and my friend triple H bought sixty thousand five hundred and fifty six dollars worth of apples at S F M L"
>>> convertor.convert(txt)
'I and my friend HHH bought $60556 worth of apples at SFML'
```

### API service example
The example folder contains a mini API demo built using Flask. The api_example.py file starts the flask server, then
the postrequest.py file sends a post request containing the input text to the API endpoint,
'http://localhost:5000/convert', and receives the converted text.


Run the following commands in this order
```
cd example
python api_example.py
python postrequest.py
```


