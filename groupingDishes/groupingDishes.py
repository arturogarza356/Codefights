def groupingDishes(dishes):
    ingredientsDictionary = {}
    i = 0
    while i < len(dishes):
        for ingredient in dishes[i][1::]:
            if ingredient in ingredientsDictionary:
                ingredientsDictionary[ingredient].append(dishes[i][0])
                ingredientsDictionary[ingredient]= ingredientsDictionary[ingredient][:1]+ sorted(ingredientsDictionary[ingredient][1:])
            else:
                ingredientsDictionary[ingredient] = [ingredient, dishes[i][0]]
        i+=1
    ingredientsWithTwoOrMoreDishes = []
    orederedKeys = sorted(ingredientsDictionary.keys())
    for key in orederedKeys:
        if len(ingredientsDictionary[key]) >= 3:
            ingredientsWithTwoOrMoreDishes.append(ingredientsDictionary[key])
    return ingredientsWithTwoOrMoreDishes
