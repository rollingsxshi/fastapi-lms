from fastapi import FastAPI
from dotenv import load_dotenv

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

load_dotenv()

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI LMS",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact={
        "name": "Enaya",
        "email": "rollingsxshi@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
