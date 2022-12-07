from fastapi import FastAPI, Depends
import uvicorn
import titanic_apputils

from titanic_pipe import TitanicPipe

app = FastAPI(title = 'Titanic FastAPI',
              description = 'Entregable módulo 3. Omar López',
              version = '1.0.0')

titanic_delegate = TitanicPipe()

@app.get('/')
def home():
    return {'text': 'App Titanic Survival Prediction'}

@app.post('/predict')
def predict(response : titanic_apputils.response = Depends(titanic_delegate.predict) ):
    """
    function called in order to make predictions

    Args:
        response (titanic_apputils.response, optional): _description_. Defaults to Depends(titanic_delegate.predict).

    Returns:
        response : contains the prediction
    """
    return response

if __name__ == '__main__':
    uvicorn.run(app)