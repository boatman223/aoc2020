import re

with open('input') as f:
    data = f.read().splitlines()

all_allergens = set()
recipes = []
for line in data:
    ingredients = set(re.findall('(\w+)', line.split('contains')[0]))
    allergens = set(re.findall('(\w+)', line.split('contains')[1]))
    all_allergens.update(allergens)
    recipes.append([ingredients, allergens])

identified = {0:0}
solution = []
while identified:
    for allergen, ingredient in list(identified.items()):
        for ingredients, allergens in recipes:
            ingredients.discard(ingredient)
            allergens.discard(allergen)
            all_allergens.discard(allergen)
        del identified[allergen]

    for allergen in all_allergens:
        poss = []
        for ingredients, allergens in recipes:
            if allergen in allergens:
                poss.append(ingredients)

        poss = set.intersection(*poss)
        if len(poss) == 1:
            ingredient = ''.join(poss)
            identified[allergen] = ingredient
            solution.append((allergen, ingredient))

solution = [x[1] for x in sorted(solution, key=lambda x: x[0])]
print(','.join(solution))