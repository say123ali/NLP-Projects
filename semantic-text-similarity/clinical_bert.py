from semantic_text_similarity.models import ClinicalBertSimilarity


class clinicbertSimilarity:
    def __init__(self, sentence1, sentence2):
        self.sentence1 = sentence1
        self.sentence2 = sentence2

    def predict(self):
        model = ClinicalBertSimilarity()
        model_input = [(self.sentence1, self.sentence2)]
        predictions = model.predict(model_input)
        #print(predictions)
        return predictions


#clinic = clinicbertSimilarity(sentence1="A man with a sexy hat is dancing.",sentence2="A woman wearing a lingerie is dancing.")
#clinic.predict()