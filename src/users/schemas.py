from datetime import datetime,date

from pydantic import BaseModel


class addFront(BaseModel):
    front_din_brand:str
    front_amp_brand:str
    user_id:int

class addSub(BaseModel):
    sub_din_brand:str
    sub_amp_brand:str
    user_id:int

class addBack(BaseModel):
    back_din_brand:str
    back_amp_brand:str
    user_id:int

class addBattery(BaseModel):
    battery_type:str
    user_id:int