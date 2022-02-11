# Imports

from sys import argv
import numpy as np
import yaml


# Variables

pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
    
damage_array = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]])

pokemon1 = argv[1]
pokemon2 = argv[2]
pokemon3 = argv[3]

# Open Yaml File

with open('pokemon.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)


# Fonctions

def effective(attType, defType, doubleType):
    if doubleType == None:
        attInd = pokemon_types.index(attType)
        defInd = pokemon_types.index(defType)


        if damage_array[attInd][defInd] == 0:
            multi = 0
            # print("This attack is : x0 Null")
        elif damage_array[attInd][defInd] == 0.5:
            multi = 0.5
            # print("This attack is : x0.5 Not very effective")
        elif damage_array[attInd][defInd] == 1:
            multi = 1
            # print("This attack is : x1 Neutre")
        elif damage_array[attInd][defInd] == 2:
            multi = 2
            # print("This attack is : x2 Super effective")
    else:
        attInd = pokemon_types.index(attType)
        defInd = pokemon_types.index(defType)
        doubleInd = pokemon_types.index(doubleType)

        if damage_array[attInd][defInd] == 0:
            multi = 0
            # print("This attack is : x0 Null")
        elif damage_array[attInd][doubleInd] == 0:
            multi = 0
            # print("This attack is : x0 Null")
        else:
            if damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 1:
                multi = 0.25
                # print("This attack is : x0.25 Not very very effective")
            elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 1.5:
                multi = 0.5
                # print("This attack is : x0.5 Not very effective")
            elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 2:
                multi = 1
                # print("This attack is : x1 Neutre")
            elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 2.5:
                multi = 1
                # print("This attack is : x1 Neutre")
            elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 3:
                multi = 2
                # print("This attack is : x2 Super effective")
            elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 4:
                multi = 4
                # print("This attack is : x4 Super super effective")
    return multi

def weakless(pokemon):
    weak = []
    strong = []
    compter = 0
    for x in damage_array:
        # print(pokemon_types[compter], x[ind])
        # print(pokemon_types[compter])
        multi = effective(pokemon_types[compter], data[pokemon][0], data[pokemon][1])
        # print(multi)
        if multi > 1:
            weak.append(pokemon_types[compter])
        elif multi < 1:
            strong.append(pokemon_types[compter])
        compter += 1

    print("=======================================================")
    print("{}".format(pokemon))
    print("         Weak to :")
    print(weak)
    print()
    print("         Strong to :")
    print(strong)


# Code

weakless(pokemon1)
weakless(pokemon2)
weakless(pokemon3)
