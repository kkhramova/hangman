def stages(mistakes) -> str:
    if mistakes == 0:
        return '''----------
        ||  
        ||
        ||
        ||
        ||
=========='''
    elif mistakes == 1:
        return '''----------
    |   ||  
        ||
        ||
        ||
        ||
=========='''
    elif mistakes == 2:
        return '''----------
    |   ||  
    0   ||
        ||
        ||
        ||
=========='''
    elif mistakes == 3:
        return '''----------
    |   ||
    0   ||  
    |   ||
        ||
        ||
=========='''
    elif mistakes == 4:
        return '''----------
    |   ||
    0   ||  
   /|   ||
        ||
        ||
=========='''
    elif mistakes == 5:
        return '''----------
    |   ||  
    0   ||
   /|\  ||
        ||
        ||
=========='''
    elif mistakes == 6:
        return '''----------
    |   ||  
    0   ||
   /|\  ||
   /    ||
        ||
=========='''
    elif mistakes == 7:
        return '''----------
    |   ||  
    0   ||
   /|\  ||
   / \  ||
        ||
=========='''
