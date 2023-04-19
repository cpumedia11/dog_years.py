dog_age = int(input("Введите возраст вашей собаки: "))

if dog_age == 1:
    human_age = 13
elif dog_age == 2:
    human_age = 24
elif dog_age > 2:
    human_age = 24 + (dog_age - 2) * 5

print("Возраст вашей собаки в человеческих годах:", human_age)
