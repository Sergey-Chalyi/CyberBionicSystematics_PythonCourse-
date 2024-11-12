# Task1
# Створіть три класи User, Moderator, Admin. Клас User має мати наступні властивості: логін та пароль. Має мати методи авторизації та логаут. Модератор успадковано від юзера та має мати додатковий метод mute. Admin успадковується від модератору та має додатковий метод бан. Для адміністратора перевизначте метод авторизації з двохфакторною авторизацію

class User():
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password
        self.is_logged_in = False

    def login(self, login: str, password: str) -> bool:
        """if login and password are correct user logs in the sustem and returns True"""
        if self.login == login and self.password == password:
            self.is_logged_in = True
            return True
        return False
    
    def logout(self) -> bool:
        """if user was logged in he/she would be logged out and returns True"""
        if self.is_logged_in == True:
            self.is_logged_in = False
            return True
        return False

class Moderator(User):
    def mute(self) -> None:
        print("Moderator mute")
        pass

class Admin(Moderator):
    def bun(self) -> None:
        print("Admin bun")
        pass

    def login(str, login: str, password: str) -> bool:
        print("Armin login")
        pass