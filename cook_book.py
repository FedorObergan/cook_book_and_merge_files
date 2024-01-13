from pprint import pprint

with open('recipes.txt', encoding = 'utf-8') as f:
    cook_book = {}
    while True:
        dish = f.readline().strip()
        if not dish:
            break

        ingredients_amount = int(f.readline().strip())
        ingredients = []
        for i in range(ingredients_amount):
            ingredient_info = f.readline().strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_info[0],
                'quantity': ingredient_info[1],
                'measure': ingredient_info[2]
            }
            ingredients.append(ingredient)
        f.readline()
        cook_book[dish] = ingredients

pprint(cook_book)
print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list.keys():
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': person_count*int(ingredient['quantity'])
                }
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] +=\
                    person_count*int(ingredient['quantity'])
    return shop_list


print('Cписок ингредиентов для 3 порций каждого из блюд: Фахитос, Омлет.')
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))