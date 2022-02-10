# Detect the element of ennemy and show you the better Pokémon
# 
#  

from sys import argv
import numpy as np


pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]


# A 2 Dimenstional Numpy Array Of Damage Multipliers For Attacking Pokemon:
    
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

# x / 0     = -3
# 0.5 / 0.5 = -2
# 1 / 0.5   = -1
# 1 / 1     = 0
# 1 / 2     = +1
# 2 / 2     = +2



# x + 0     <= 
# 0 + 0 = 0
# 0 + 0.5 = 0.5
# 0 + 1 = 1

# 0.5 + 0.5 = 1

# 1 / 0.5   = 1.5

# 1 / 1     = 2
# 2 / 0.5   = 2.5

# 1 / 2     = 3

# 2 / 2     = 4


attType = argv[1]
defType = argv[2]
doubleType = argv[3]

print(attType, defType, doubleType)

if doubleType == "m":
    attInd = pokemon_types.index(attType)
    defInd = pokemon_types.index(defType)


    if damage_array[attInd][defInd] == 0:
        print("This attack is : x0 Null")
    elif damage_array[attInd][defInd] == 0.5:
        print("This attack is : x0.5 Not very effective")
    elif damage_array[attInd][defInd] == 1:
        print("This attack is : x1 Neutre")
    elif damage_array[attInd][defInd] == 2:
        print("This attack is : x2 Super effective")
else:
    attInd = pokemon_types.index(attType)
    defInd = pokemon_types.index(defType)
    doubleInd = pokemon_types.index(doubleType)

    if damage_array[attInd][defInd] == 0:
        print("This attack is : x0 Null")
    elif damage_array[attInd][doubleInd] == 0:
        print("This attack is : x0 Null")
    else:
        if damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 1:
            print("This attack is : x0.25 Not very very effective")
        elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 1.5:
            print("This attack is : x0.5 Not very effective")
        elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 2:
            print("This attack is : x1 Neutre")
        elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 2.5:
            print("This attack is : x1 Neutre")
        elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 3:
            print("This attack is : x2 Super effective")
        elif damage_array[attInd][defInd] + damage_array[attInd][doubleInd] == 4:
            print("This attack is : x4 Super super effective")

