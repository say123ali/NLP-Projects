from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

import cosineSimilarity
from levenshteinDistance import levenshtein
from web_bert import webbertSimilarity
from clinical_bert import clinicbertSimilarity

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
        data = request.json['data']
        sentence1 = data[0]
        sentence2 = data[1]
        predict1 = levenshtein(sentence1,sentence2)
        vector1 = cosineSimilarity.text_to_vector(sentence1)
        vector2 = cosineSimilarity.text_to_vector(sentence2)
        predict2 = cosineSimilarity.get_cosine(vector1,vector2)
        webbert_object = webbertSimilarity(sentence1,sentence2)
        clinicbert_object = clinicbertSimilarity(sentence1, sentence2)
        webert_prediction = webbert_object.predict()
        clinic_prediction = clinicbert_object.predict()
        return jsonify({ "Levenshtein Distance" : predict1 , "CosineSimilarity" : predict2, "Web Bert Model" : str(webert_prediction[0]),
                         "clinic Bert Model" : str(clinic_prediction[0])})




#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=7000, debug=True)

# The [0,5] is a standard annotation range for STS tasks with 0 representing
# complete dissimilarity and 5 total similarity.