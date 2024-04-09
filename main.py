import os

import requests 

from dotenv import load_dotenv

from models import Course

from fastapi import FastAPI

app = FastAPI()

#https://canvas.instructure.com/doc/api/discussion_topics.html

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")

base_url = "https://dixietech.instructure.com/api/v1"


headers: dict[str, str] = {
    "Authorization": f"Bearer {access_token}"
}


@app.get("/courses")
async def get_courses() -> list[Course]:
    response = requests.get(url=f"{base_url}/courses", headers=headers)
    r_json = response.json()

    courses: list[Course] = []
    for course_json in r_json:
        course = Course(id=course_json["id"], name=course_json["name"])
        courses.append(course)

    return courses

@app.get("/discussions")
async def get_discussions() -> list:
    response = requests.get(url=f"{base_url}/discussions", headers=headers)
    r_json = response.json()

    discussions = []
    for discussion_json in r_json:
        # Process discussion data as needed
        discussions.append(discussion_json)

    return discussions
