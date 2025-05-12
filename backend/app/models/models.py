from sqlmodel import SQLModel, Field, Text,Column, TIMESTAMP
from uuid import UUID
from pydantic import ConfigDict



class Autograder_Logs(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True) # needed for the created_at since its not natively supported

    id: UUID = Field(default=None,primary_key=True)
    submission_id: UUID 
    log: str | None #= Field(sa_column=Column(Text))
    created_at: TIMESTAMP = Field(sa_column=Column(TIMESTAMP(timezone=True)))
