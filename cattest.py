from catfunc import Cat

pets = [
{
     "name": "Феликс",
     "gender": "Мальчик",
     "age": "2",
    },
{
     "name": "Гоша",
     "gender": "Мальчик",
     "age": "1",
    },
{
     "name": "Барон",
     "gender": "Мальчик",
     "age": "2",
    },
{
     "name": "Мухтар",
     "gender": "Мальчик",
     "age": "0.5",
    },
{
     "name": "Линда",
     "gender": "Девочка",
     "age": "2",
    },
{
     "name": "Сэм",
     "gender": "Мальчик",
     "age": "2",
    },
]
print("-----------------------------")
for curr_pet in pets:
    pet = Cat(name = curr_pet.get("name"),gender = curr_pet.get("gender"), age = curr_pet.get("age"))
    print(pet.name)
    print(pet.gender)
    print(pet.age)
    print("-----------------------------")