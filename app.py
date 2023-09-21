from flask import Flask, request, jsonify

from model import extract
app = Flask(__name__)

@app.route('/submit_text', methods=['POST'])
def submit_text():
    data = request.get_json()

    if 'text' not in data: 
        return jsonify({'error': 'Text is required'}), 400

    text = data['text']
    
    userdata = extract(text)
   

    return jsonify({'Modified text': userdata[0] , 'mappings': userdata[1]}), 200


if __name__ == '__main__':
    app.run(debug=True)
