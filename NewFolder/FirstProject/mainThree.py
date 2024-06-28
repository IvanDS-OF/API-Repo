#Import the library
from fastapi import FastAPI, HTTPException

##Creation of a new app
app = FastAPI()

##Creation of a new instance
    #Creation of a list of dictionaries

todo_list = [{"id": 1,"description": "Learning Python" ,"completed": True}, 
             {"id": 2,"description": "Learning FastAPI" ,"completed": False}, 
             {"id": 3,"description": "This is my third task xd" ,"completed": False}]

    #Creation of my get method
@app.get("/todo") #Decorator
async def get_all(complete: bool):
    data_filtered = list(filter(lambda todo:todo["completed"] == complete, todo_list))
    return data_filtered


#The objective of this file is: How to use a Path parameter to obtain the information 
#of one of the TODO LIST element

@app.get("/todo1/{todo_id}")
##Around brackets we need to type the name ouf our parameter, in this case we will type it
# as an Fstring 
async def get_todo(todo_id:int): #In the argument we declare the path id
    #return todo_id ##With this code, we return the value introduced in the FastAPI Docs website

    todo_data = next(todo for todo in todo_list if todo["id"] == todo_id)
    return todo_data
    #With this code, we search through the values of the list and return the 
    #id number corresponding

    ##Currently, if we type on the gui one number out of the id number, returns an error
    #W need to round the function with an Error Handling - Try Except

##Creation of the same function 
@app.get("/todo/{todo_id_2}")
async def get_todo_2(todo_id_2:int):
    try:
        todo_data_2 = next(todo for todo in todo_list if todo["id"] == todo_id_2)
        return todo_data_2
    except:
        #The error needs to be imported from the FASTAPI librery as HTTPException
        #raise "Error encontrado padresanto, intenta más tarde krnal,  bai"
        raise HTTPException(status_code=404, detail="Sobres, no jaló, bai")

