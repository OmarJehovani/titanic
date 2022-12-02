# titanic
Proyecto para el entregable del módulo 3 del diplomado en Despliegue de Modelos de ML

#crear entorno virtual: 
python3 -m venv venv 

#activar entorno virtual: 
source venv/bin/activate 

#Instalar requirements.txt 
pip install -r requirements.txt 

#poetry 
Poetry new titanic_utils 
poetry build  

#Instalar libreria propia de titanic_utils:  
pip install titanic_utils-0.1.0-py3-none-any.whl

#crear el modelo ejecutando el script train_model.py 
python3 -m train_model 

#activar fastappi: 
uvicorn titanic_app:app  --reload

Copiar este bloque para hacer el request: 

{
    "pclass": 1,
    "name": "Allen, Miss. Elisabeth Walton",
    "sex": "female",
    "age": "29",
    "sibsp": 0,
    "parch": 0,
    "ticket": "24160",
    "fare": "211.3375",
    "cabin": "B5",
    "embarked": "S",
    "boat": "2",
    "body": "?",
    "home_dest": "St Louis, MO"
}
