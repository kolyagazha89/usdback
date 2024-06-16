from datetime import datetime,date

from pydantic import BaseModel


class addStage(BaseModel):
    stage_name:str
    stage_desc:str
    stage_photo:str
    stage_city:str
    stage_place:str
    stage_date:date
    stage_type:int

class addSP(BaseModel):
    SP_stage:int
    SP_partner:list

class addST(BaseModel):
    ST_stage:int
    ST_tags:list