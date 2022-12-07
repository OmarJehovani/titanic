from pydantic import BaseModel

class requestParameters(BaseModel):
    """parameters for predictions"""
    pclass: int
    name: str
    sex: str
    age: str
    sibsp: int
    parch: int
    ticket: str
    fare: str
    cabin: str
    embarked: str
    boat: str
    body: str


class response(BaseModel):
    """parameters with prediction info"""
    prediction: int
    message: str