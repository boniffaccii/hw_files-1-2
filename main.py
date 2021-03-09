from pprint import pprint

def read_recipe(filepath):

    meal = []
    with open(filepath, 'r') as f:
        dish_names = []
        cook_book = {}
        for line in f:
            line = line.strip('\n')
            if line.find('|') < 0 and not line.isspace() and not line.isdigit():
                dish_name = line.strip('\n')
                print(dish_name)
                dish_names.append(dish_name)
                print(dish_names)
                cook_book.fromkeys(dish_names, None)
            elif line.find('|') > 0:
                ingredient = line.split(' | ')
                ingr = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                meal.append(ingr)
        cook_book.fromkeys(dish_names)
    pprint(cook_book)

if __name__ == '__main__':
    read_recipe('recipes.txt')