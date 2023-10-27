from fastapi import FastAPI, Path, UploadFile, Query
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from uvicorn import run

app = FastAPI(
    title    = "IISERB Communities Online",
    summary  = "Welcome to the backend of the project IISERB Communities which aims to form a link between different clubs of IISERB.",
    version  = "0.1.0",
    docs_url = "/"
)

class Role(Enum):
    Advisor = 1
    Coordinator = 2
    CoreCommittee = 3
    VolunteerCommittee = 4
    Member = 5

class Club(BaseModel):
    _id : int
    name : str
    label : str
    description : str
    logo : UploadFile

class Member(BaseModel):
    _id : int
    roll_no : int
    name : str
    role : Role
    description : str
    club_id : int
    picture : UploadFile

class Events(BaseModel):
    _id : int
    title : str
    venue : str
    time : datetime
    end_time : datetime
    poster : UploadFile

if __name__ == '__main__':
    run('main:app',
        host     = '127.0.0.1',
        port     = 8000,
        reload   = True,
        log_level= "info"
    )