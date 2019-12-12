#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    needed = list(recipe.values())
    have = list(ingredients.values())
    total_batches = []
    if len(have) != len(needed):
        return 0
    for amount in range(len(needed)):
        if needed[amount] > have[amount]:
            return 0
        else:
            batches = have[amount] // needed[amount]
            print(batches)
        total_batches.append(batches)
    return min(total_batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
