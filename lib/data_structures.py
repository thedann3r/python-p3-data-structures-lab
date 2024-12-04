spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu", 
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [x["name"] for x in spicy_foods] 

def get_spiciest_foods(spicy_foods):
    return [x for x in spicy_foods if x["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        emoji = '🌶' * x['heat_level']
        print(f"{x['name']} ({x['cuisine']}) | Heat Level: {emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for x in spicy_foods:
        if x ["cuisine"] == cuisine:
            return x
        
def print_spiciest_foods(spicy_foods):
    for x in spicy_foods:
        if x["heat_level"] > 5:
            heat = "🌶" * x["heat_level"]
            print(f"{x['name']} ({x['cuisine']}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods):
    total = 0 
    for x in spicy_foods:
        total += x['heat_level']
    return total / len(spicy_foods)    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
