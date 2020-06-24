def replace(calc):
    return calc.replace("^", "**")
def calculator():
    calc = input('What would you like to calculate? ')
    old_calc = calc
    calc = replace(calc)
    a = eval(calc)
    print('The answer to ' + old_calc + ' is ' + str(a))
while True:
    calculator()