from model_utils import Choices

TYPE_USER = Choices((0,"admin", "admin"), (1, "company", "company"), (2, "candidate", "candidate"))

SALARY_RANGE = Choices(
    ("up_to_1000", "up to 1.000"),
    ("from_1000_to_2000", "from 1.000 to 2.000"), 
    ("from_2000_to_3000", "from 2.000 to 3.000"),
    ("over_3000", "over 3.000"),
)


SCHOOLING = Choices(("Elementary_School", "Elementary School"), ("High_school", "High school"), 
                    ("Technologist", "Technologist"), ("University_education", "University education"),
                    ("Post_MBA _Master's", "Post / MBA / Master's"), ("Doctorate_degree", "Doctorate degree"))


SCHOOLING_DICT = {
    "Elementary_School": 1,
    "High_school": 2,
    "Technologist": 3,
    "University_education": 4,
    "Post_MBA _Master's": 5,
    "Doctorate_degree": 6
}

SALARY_RANGE_DICT = {
    "up_to_1000": 1,
    "from_1000_to_2000": 2,
    "from_2000_to_3000": 3,
    "over_3000": 4,
}
        