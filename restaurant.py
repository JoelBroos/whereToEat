# Project: Restaurant Selector
# Joel Broos 

# Abbreviations for restaurant names
joes = 'Joe’s Gourmet Burgers'  # vege=no, vegan=no, gFree=no
pizza = 'Main Street Pizza Company'  # vege=yes, vegan=no, gFree=yes
cafe = 'Corner Café'  # vege=yes, vegan=yes, gFree=yes
mamas = 'Mama’s Fine Italian'  # vege=yes, vegan=no, gFree=no
chefs = 'The Chef’s Kitchen'  # vege=yes, vegan=yes, gFree=yes

# Ask if any members of party have an dietary requirements
vege = input('Is anyone in your party vegetarian? ')
vegan = input('Is anyone in your party vegan? ')
gFree = input('Is anyone in your party gluten free? ')

# Turn input all into lower case
vege = vege.lower()
vegan = vegan.lower()
gFree = gFree.lower()

print('Here are your restaurant choices:')

# Conditional statements to print out restaurants that match requirements

# No one has nay restrictions
if vege=='no' and vegan=='no' and gFree=='no':
    print('\t'+joes, pizza, cafe, mamas, chefs, sep='\n\t')
# Someone is vegetarian
elif vege=='yes' and vegan=='no' and gFree=='no':
    print('\t'+pizza, cafe, mamas, chefs, sep='\n\t')
# Someone is vegan
elif vege=='no' and vegan=='yes' and gFree=='no':
    print('\t'+cafe, chefs, sep='\n\t')
# Someone is gluten free
elif vege=='no' and vegan=='no' and gFree=='yes':
    print('\t'+pizza, cafe, chefs, sep='\n\t')
# Someone is vegetarian and vegan
elif vege=='yes' and vegan=='yes' and gFree=='no':
    print('\t'+cafe, chefs, sep='\n\t')
# Someone is vegan and gluten free
elif vege=='no' and vegan=='yes' and gFree=='yes':
    print('\t'+cafe, chefs, sep='\n\t')
# Someone is vegetarian and gluten free
elif vege=='yes' and vegan=='no' and gFree=='yes':
    print('\t'+pizza, cafe, chefs, sep='\n\t')
# Someone is vegetarian, vegan and gluten free and
elif vege=='yes' and vegan=='yes' and gFree=='yes':
    print('\t'+cafe, chefs, sep='\n\t')
else:
    print('Incorrect input')