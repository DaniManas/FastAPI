
import pickle
import pandas as pd

#import the ml model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

#Model Versioning
MODEL_VERSION = "1.0.0"

#Get class labels from model (important for matching probabilities to lables)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    #make prediction
    prediction = model.predict(input_df)[0]


    #get prediction probabilities
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities) 

    #create dictionary mapping class labels to probabilities
    prob_dict = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))

    #return prediction and probabilities
    return {
        "prediction": prediction,
        "confidence": round(confidence, 4),
        "probabilities": prob_dict
    }