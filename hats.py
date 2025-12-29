from utils import int

ALL_HATS = [
    Hats.Brown_Hat,
    Hats.Cactus_Hat,
    Hats.Carrot_Hat,
    Hats.Dinosaur_Hat,
    # Hats.Gold_Hat,
    # Hats.Gold_Trophy_Hat,
    # Hats.Golden_Cactus_Hat,
    # Hats.Golden_Carrot_Hat,
    # Hats.Golden_Gold_Hat,
    # Hats.Golden_Pumpkin_Hat,
    # Hats.Golden_Sunflower_Hat,
    # Hats.Golden_Tree_Hat,
    Hats.Gray_Hat,
    Hats.Green_Hat,
    Hats.Pumpkin_Hat,
    Hats.Purple_Hat,
    # Hats.Silver_Trophy_Hat,
    Hats.Straw_Hat,
    Hats.Sunflower_Hat,
    # Hats.The_Farmers_Remains,
    Hats.Top_Hat,
    # Hats.Traffic_Cone,
    # Hats.Traffic_Cone_Stack,
    Hats.Tree_Hat,
    Hats.Wizard_Hat,
    # Hats.Wood_Trophy_Hat,
]

def put_on_random_hat():
    hat = pick_hat()
    quick_print("Putting on hat:", hat)
    change_hat(hat)

def pick_hat():
    num_hats = len(ALL_HATS)
    x = random() * num_hats
    i = int(x)
    if num_hats <= i:
        i = num_hats - 1

    return ALL_HATS[i]