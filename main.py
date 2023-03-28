import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def login(self):
        pass

    def savetoFile(self):

        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                print("users")

repository = UserRepository()

while True:
    print("Menü".center(50, "*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            username = input("username:")
            password = input("password: ")
            mail = input("mail: ")
            user = User(username=username, password=password, email=email)
            repository.register(user)
        elif secim == "2":
            pass
        elif secim == "3":
            pass
        elif secim == "4":
            pass
        elif secim == "5":
            break
