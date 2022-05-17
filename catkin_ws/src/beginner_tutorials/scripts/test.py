from multiprocessing.sharedctypes import Value
import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+[^@]+")

def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None


class User:
    def __init__(self, username) -> None:
        self.username = username
        self._email = None

    # Get Property
    @property
    def email(self):
        return self._email

    # Set Property
    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"Error {new_email}")
        self._email = new_email


u1 = User('smith')

u1.email="smith@co"
print(u1.email)