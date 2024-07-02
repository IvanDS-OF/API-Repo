from pydantic import BaseModel, Field

##Remember, this is the blueprint - Plano del objeto 
#We will us it as a validation method 

class TodoSchema(BaseModel):
    ##Remember this is like a constructor
    tittle: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=500)
    priority: int = Field(gt=0, le=5)
    complete: bool



