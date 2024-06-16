from pydantic import BaseModel


class addPartner(BaseModel):
    partner_name:str
    partner_desc:str
    partner_logo:str
    partner_type:int