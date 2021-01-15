# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(pet_shop_name):
    return pet_shop_name["admin"]["total_cash"]

def add_or_remove_cash(pet_shop_name, cash):
    pet_shop_name["admin"]["total_cash"] = pet_shop_name["admin"]["total_cash"] +cash
    return pet_shop_name["admin"]["total_cash"]

def get_pets_sold(pet_shop_name):
    return pet_shop_name["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number_increase):
    pet_shop["admin"]["pets_sold"] += 2
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    searched_breeds = []
    for index, item in enumerate(pet_shop["pets"]):
        if breed == item["breed"]:
            searched_breeds.append(item)
    return searched_breeds

def find_pet_by_name(pet_shop, pet_name):

    for item in pet_shop:
        

    return pet_shop["pets"][index]