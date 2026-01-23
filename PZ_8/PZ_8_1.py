#Переименуйте 'city' в 'location'

sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}
print(sample_dict)
sample_dict.pop("city")
sample_dict.update({"location":"New York"})
print(sample_dict)