from pydantic import Basemodel


class Course(Basemodel):
    id: int
    name: str