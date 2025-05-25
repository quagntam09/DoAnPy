import json
import bcrypt

class User:
    def __init__(self, Id, Ten, Tien, Vip, Email, Sdt, Account, Role):
        self.Id = Id
        self.Ten = Ten
        self.Tien = Tien
        self.Vip = Vip
        self.Email = Email
        self.Sdt = Sdt
        self.Account = Account
        self.Role = Role

    def to_dict(self):
        return {
            "Id": self.Id,
            "Ten": self.Ten,
            "Tien": self.Tien,
            "Vip": self.Vip,
            "Email": self.Email,
            "Sdt": self.Sdt,
            "Account": self.Account,
            "Role": self.Role
        }

class UserManager:
    def __init__(self):
        self.Users = []
        self.DocFileJson()
    
    def DocFileJson(self):
        with open("user/users.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                user = User(item["Id"], item["Ten"], item["Tien"], item["Vip"], item["Email"], item["Sdt"], item["Account"], item["Role"])
                self.Users.append(user)


    def ThemUser(self, AccountId, password, Email, Sdt, Role):
        Id = "0" + str(len(self.Users) + 1) 
        Tien = 0
        Vip = False
        Ten = "usernew" + "0" + str(len(self.Users) + 1)

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        Account = {"AccountId": AccountId, "Password": hashed}
        user = User(Id, Ten, Tien, Vip, Email, Sdt, Account, Role)
        self.Users.append(user)
        self.GhiFileJson()

    def GhiFileJson(self):
        with open("user/users.json", "w", encoding="utf-8") as f:
            data = [user.to_dict() for user in self.Users]
            json.dump(data, f, indent=4, ensure_ascii=False)
