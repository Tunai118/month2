class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

admin = User("Tunai", "admin")
user = User("Ardager", "user")

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func(user)
        else:
            print("У вас нет доступа!")
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

delete_video(admin)
delete_video(user)

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        result = end - start
        print("Время загрузки:", result)
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Загружено")
download_video()
