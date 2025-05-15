from sqlmodel import SQLModel, Field, Text,Column, TIMESTAMP
from uuid import UUID
from uuid import uuid4
from pydantic import ConfigDict
from datetime import datetime



class Autograder_Logs(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 

    id: UUID = Field(default_factory=uuid4,primary_key=True)
    submission_id: UUID = Field(foreign_key="submissions.id",index=True)
    log: str | None = Field(default=None,sa_column=Column(Text))
    created_at: datetime = Field(default=None,sa_column=Column(TIMESTAMP(timezone=True)))

class Submissions(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 

    id: UUID = Field(default_factory=uuid4,primary_key=True)
    assignment_id: UUID = Field(foreign_key="assignments.id",index=True)
    student_id: UUID = Field(foreign_key= "users.id",index=True)
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True)))
    # ! need to add a content addition / way to store submissions, maybe store the zip instead of the file 

class Classroom_Teachers(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 

    id: UUID = Field(default_factory=uuid4,primary_key=True)
    classroom_id: UUID = Field(foreign_key="classrooms.id",index=True)
    teacher_id: UUID = Field(foreign_key="users.id",index=True)
    is_primary: bool = Field(default=False),
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True)))

class Classroom_Members:
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 
    
    id: UUID = Field(default_factory=uuid4,primary_key=True)
    classroom_id: UUID = Field(foreign_key="classrooms.id",index=True)
    user_id : UUID = Field(foreign_key="users.id",index=True)
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True)))



class Classrooms(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 

    id: UUID = Field(default_factory=uuid4,primary_key=True)
    name: str = Field(sa_column=Column(Text))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True)))


class Assignments(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 

    id: UUID = Field(default_factory=uuid4,primary_key=True)
    classroom_id: UUID = Field(foreign_key="classrooms.id",index=True)
    name: str = Field(sa_column=Column(Text))
    due_date:datetime = Field(sa_column=Column(TIMESTAMP(timezone=True)))
    test_case : str = Field(sa_column=Column(Text))
    max_grade: int = Field(default=100) 
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True)))



class Grades(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 

    id: UUID = Field(default_factory=uuid4,primary_key=True)
    submission_id: UUID = Field(foreign_key="submissions.id") # to get the assignment, do a double join -> submissions -> assignments
    grader_id : UUID = Field(foreign_key="classroom_teachers.id")
    grade: int 
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True)))

class Users(SQLModel,table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True,validate_assignment=True) 
    id: UUID = Field(default_factory=uuid4,primary_key=True)
    email: str = Field(sa_column=Column(Text))
    role: str = Field()

