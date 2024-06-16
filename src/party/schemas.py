from datetime import datetime,date

from pydantic import BaseModel


class addParticipant(BaseModel):
    user_id:int

class addPC(BaseModel):
    PC_class:str
