from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    middle_name: str = Field(alias="middleName")


class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id="1",
    title="Super Course",
    maxScore=100,
    minScore=1,
    description="very interesting course",
    previewFile=FileSchema(
        id="1",
        filename="course_preview.jpg",
        directory="course_preview",
        url="http://localhost:8000"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="1",
        email="alice@examlpe.com",
        firstName="Alice",
        lastName="Example",
        middleName="Mid",
    )
)

print("Course default model", course_default_model)

course_dict = {
    "id": "2",
    "title": "Puper Course",
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
        "id": "1",
        "filename": "course_preview.jpg",
        "directory": "course_preview",
        "url": "http://localhost:8000"
    },
    "description": "The best course ever",
    "estimatedTime": "2 weeks",
    "createdByUser": {
        "id": "1",
        "email": "al@examlpe.com",
        "firstName": "Tik",
        "lastName": "Tak",
        "middleName": "Toe",
    }
}

course_dict_model = CourseSchema(**course_dict)
print("Course model", course_dict_model)


course_json = """
{
    "id": "2",
    "title": "Puper Course",
    "maxScore": 100,
    "minScore": 10,
    "previewFile": {
        "id": "1",
        "filename": "course_preview.jpg",
        "directory": "course_preview",
        "url": "http://localhost:8000"
    },
    "description": "The best course ever",
    "estimatedTime": "2 weeks",
    "createdByUser": {
        "id": "1",
        "email": "al@examlpe.com",
        "firstName": "Tik",
        "lastName": "Tak",
        "middleName": "Toe"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("Course model", course_json_model)

print(course_dict_model.model_dump_json(by_alias=True))

try:
    file = FileSchema(
        id="1",
        filename="course_preview.jpg",
        directory="course_preview",
        url="localhost:8000"
    )
except ValidationError as err:
    print(err)