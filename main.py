from pprint import pprint

cook_book = {}


def read_recipe(filepath):
    meal = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.find('|') < 0 and not line.isspace() and not line.isdigit() and not line == '':
                dish_name = line
                cook_book.update({dish_name : None})
            elif line.find('|') > 0:
                ingredient = line.split(' | ')
                ingr = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                meal.append(ingr)
                cook_book.update({dish_name : meal})
            elif line == '':
                meal = []
    pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if shop_list.get(ingr['ingredient_name']):
                sum = int(shop_list[ingr['ingredient_name']]['quantity']) + int(ingr['quantity'])
                shop_list[ingr['ingredient_name']]['quantity'] = sum
            else:
                shop_list.update({ingr['ingredient_name'] : {'quantity': ingr['quantity'], 'measure': ingr['measure']}})
    for item in shop_list:
        shop_list[item]['quantity'] = int(shop_list[item]['quantity']) * int(person_count)
    pprint(shop_list)


if __name__ == '__main__':
    read_recipe('recipes.txt')
    get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос', 'Омлет'], 8)
