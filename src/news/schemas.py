from pydantic import BaseModel


class addNews(BaseModel):
    name_news:str
    text_news:str
    photo_news:str
    user_id:int