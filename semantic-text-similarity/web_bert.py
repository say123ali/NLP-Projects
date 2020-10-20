from semantic_text_similarity.models import WebBertSimilarity


class webbertSimilarity:
    def __init__(self, sentence1, sentence2):
        self.sentence1 = sentence1
        self.sentence2 = sentence2

    def predict(self):
        model = WebBertSimilarity()
        model_input = [(self.sentence1, self.sentence2)]
        predictions = model.predict(model_input)
        #print(predictions)
        return predictions

# similar = Webbert_similarity(sentence1="A man with a hard hat is dancing.", sentence2="A woman wearing a lingerie is dancing.")
# similar.predict()
