from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from ExampleSynchronous import plagiarism

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    text = request.json["text"]
    email = request.json["email"]
    key = request.json["key"]
    check = plagiarism(text, email, key)
    words = check.plag()
    return jsonify({"Results": str(words)})

#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=9000, debug=True)