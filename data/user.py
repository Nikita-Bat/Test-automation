class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, password={self.password}, role={self.role})"