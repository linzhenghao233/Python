alien_color = ['green', 'yellow', 'red']
if alien_color[0] == 'green':
    print("+5")
if alien_color[1] == 'green':
    print(' ')

if alien_color[0] == 'green':
    print('+5')
else:
    print('+10')

if alien_color[1] == 'green':
    print('+5')
else:
    print('+10')

for color in alien_color:
    if color == 'green':
        print('+5')
    elif color == 'yellow':
        print('+10')
    elif color == 'red':
        print('+15')