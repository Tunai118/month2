#Это библиотека нужна для генерации фейк имен, почт, паролей и тд
#Используется для разных задач, для дудоса)

from faker import Faker

fake = Faker()

print(f"Имя Фамилия:", fake.name())
print(f"Почта:", fake.email())
print(f"Пароль:", fake.password())
print(f"Страна:", fake.country())
