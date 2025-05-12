from sqlmodel import SQLModel, Field

class Test(SQLModel,table=True):
    id:int = Field(primary_key=True)