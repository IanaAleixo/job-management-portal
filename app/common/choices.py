from model_utils import Choices

TYPE_USER = Choices((0,"admin", "admin"), (1, "company", "company"), (2, "candidate", "candidate"))
SALARY_RANGE = Choices((0, "up to 1.000"), (1, "from 1.000 to 2.000"), (2, "from 2.000 to 3.000"), (3, "over 3.000"))
SCHOOLING = Choices((0, "Elementary School"), (1, "High school"), (2, "Technologist"), (3, "University education"),
                    (4, "Post / MBA / Master's"), (5, "Doctorate degree"))
