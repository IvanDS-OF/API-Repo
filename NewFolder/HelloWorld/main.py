#Primero vamos a hacer la importación de la librería para este ejercicio

from fastapi import FastAPI

##Luego creamos una nueva istancia que en el futuro tendrá mas cuerpo para considerar los endpoints
app = FastAPI()

#Creamos un endPoint get que la respuesta va a ser un mensaje de bienvenida.
@app.get("/") ##This is a Pass Operation Decorator
#be cause this last command is a decorator
#Luego generamos una funcion asincrona 
async def hello_world():
    return {"message": "HelloWorld"}
#To return something, in this cae we neet to create a dictionary and the key is gonna be "message"

#To run this file: we must type in our terminal the next command: 
#   uvicorn main:app --reload 
#Se usa uvicorn como el servidor que corre el programa
# main -> es el nombre del archivo
# app >es el nombre de la aplicacion creada en el file
# reload -> el servidor se va a reiniciar cada que se haga algún cambio en el código








