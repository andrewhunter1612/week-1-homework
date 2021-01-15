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
    for item in pet_shop["pets"]:
        if breed == item["breed"]:
            searched_breeds.append(item)
    return searched_breeds

def find_pet_by_name(pet_shop, pet_name):
    pet_shop_index = None
    for index, dog_name in enumerate(pet_shop["pets"]):
        if dog_name["name"] == pet_name:
            pet_shop_index = pet_shop["pets"][index]
        # else:
            # print("not found" + dog_name["name"])
    return pet_shop_index
        

# def remove_pet_by_name(pet_shop_name, dog_name):
#     for dog in pet_shop_name["pets"]:
#         if  dog["name"] == dog_name:
#             del(dog["name"])
#             print("delete completed")
        

def add_pet_to_stock(pet_shop_name, new_dog_dict):
    pet_shop_name["pets"].append(new_dog_dict)


def get_customer_cash(customer_info_dict):
    return customer_info_dict["cash"]

def remove_customer_cash(customer_name, cash_deduction):
    customer_name["cash"] = get_customer_cash(customer_name) - cash_deduction
    
def get_customer_pet_count(customer_name):
    return len(customer_name["pets"])

def add_pet_to_customer(customer_name, new_pet):
    customer_name["pets"].append(new_pet)

def customer_can_afford_pet(customer_list, new_pet_dict):
    customer_cash = customer_list["cash"]
    new_pet_price = new_pet_dict["price"]

    return customer_cash>=new_pet_price

def  sell_pet_to_customer(pet_shop_list, pet_name, customer):

    if pet_name
     
    if customer_can_afford_pet:
        pet_shop_list["pets"].remove(pet_name)
        customer["pets"].append(pet_name)
        pet_shop_list["admin"]["pets_sold"] += 1

        pet_price = pet_name["price"]
        pet_shop_list["admin"]["total_cash"] += pet_price
        customer["cash"] -= pet_price
        

