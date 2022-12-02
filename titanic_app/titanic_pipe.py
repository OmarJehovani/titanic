import joblib
import pandas as pd
import titanic_const
import titanic_apputils
from sklearn.pipeline import Pipeline

class TitanicPipe:

    prod_model: Pipeline

    def load_model(self):
        self.prod_model = joblib.load(titanic_const.PATH_MODEL)

    def predict(self, input: titanic_apputils.requestParameters) -> titanic_apputils.response:
        """load model"""
        self.load_model()

        """Runs a prediction"""
        df = pd.DataFrame([input.dict()])
        prediction = self.prod_model.predict(df)[0]
        
        return self.response(prediction)
    
    def response(self,prediction: int):
        """process result to send api response"""
        if(prediction == 0):
            message = "This person did not survive"
        elif(prediction == 1):
            message = "This person survived"

        return titanic_apputils.response(prediction=prediction, message=message)
