import json
#str+shit+b
# Open and read the JSON file
with open('recipes.json', 'r') as file:
    data = json.load(file)


#for recipe in data["recipes"]:
    #print(recipe)






import random
num_to_select = 5                           # set the number to select here.
list_of_random_items = random.sample(data["recipes"], num_to_select)
first_random_item = list_of_random_items[0]
second_random_item = list_of_random_items[1]
print(list_of_random_items)
print("Rezepte für diese Woche:")
for recipe in list_of_random_items:
    print(recipe["name"])
