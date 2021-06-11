from flask import Flask, request, jsonify

from speakeasy.convert import SpeakEasyConvertor

app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert_text():
    converter = SpeakEasyConvertor()
    input_txt = request.get_json(force=True)
    ret = {'written': converter.convert(input_txt['input'])}
    return jsonify(ret)


if __name__ == '__main__':
    app.run(debug=True)
