#First we need to import the libraries
from fastapi import FastAPI

#Then, create an INSTANCE
app = FastAPI()

#Then, create a decorator to call and use the main app
@app.get("/todo")      ##.get(metodo de ruta) returns information
##Path Operation Decorator - Define el metodo y permite dar nombre a la ruta para hacer la petición
##Creamos la funcion
async def get_all(): #Path Operation Function - La funcion proxima inmediata a nuestro decorador
    #return "List of todo"
    ##Nuetro endpoint puede retornar Strings
    #Igualmente puede devolver Diccionario o Listas
    return [{"id": 1, 
            "description": "Learning Python", 
            "completed": True},
            {"id": 2, 
            "description": "Learning FastAPI", 
            "completed": False} 
    ]

