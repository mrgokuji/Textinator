import pickle
from sklearn.feature_extraction.text import CountVectorizer


def predict(input_text):
    vectorizer, loadedModel = pickle.load(open('/home/gilfoyle/Documents/VeritasProject/Veritas_Project/backend/Textinator/Summarisation/utils/textClassificationML_model.sav', 'rb'))
    cv = vectorizer.transform(input_text)
    return loadedModel.predict(cv)

