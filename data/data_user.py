from data.user import User


class TestData(User):
    STANDARD_USER = User("bizarrewizard@gmail.com", "Nikita88", "standard")
    WRONG_EMAIL_USER = User("123456@gmail.com", "Nikita88", "WRONG_EMAIL")
    INCORRECT_EMAIL_USER = User("bizarrewizard@gmail", "Nikita88", "INCORRECT_EMAIL")
    WRONG_PASSWORD_USER = User("bizarrewizard@gmail.com", "Nikita888", "WRONG_PASSWORD")
