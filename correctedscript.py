#Added a ':' after the def statement to fix syntax error
def find_cube_pairs(target):

    #changing solutions to sol as sol is being used in the code ahead
    #Removed semicolon
    sol = []

    #Exponentiation uses two asterisks, not three- changed to two asterisks.
    #targ renamed to target wherever found.
    max_num = round(target ** (1/3))  

    #The function is named 'range', not 'ranges'. Function name has been fixed.
    #Added a ':' after the for statement to fix syntax error
    for a in range(1, max_num + 1):
        #The function is named 'range', not 'ranges'. Function name has been fixed.
        #Added a ':' after the for statement to fix syntax error
        for b in range(a, max_num + 1):

            #Exponentiation uses two asterisks, not three- changed to two asterisks.
            #targ renamed to target wherever found.
            #Added a ':' after the if statement to fix syntax error:
            if a**3 + b**3 == target:
                #removed semicolon
                sol.append((a, b))
    return sol

#Renamed 'pairs' to 'pair', as 'pair' is referenced later, not 'pairs'
#Removed comma at end of line
pair = find_cube_pairs(1729)

#PYthon uses print, not printf. Function name has been changed.
#Changed 1728 to 1729
#Removed comma at end of line
print("Valid cube pairs for 1729:")

#Added a ':' after the for statement to fix syntax error
for a, b in pair:
    #Python uses print, not printf. Function name has been changed.
    #We are calculating sqaures, not cubes here. Changed 2 to 3 during exponentiation.
    #Changed 1728 to 1729
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
