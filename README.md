# ClassActivity-2
Submission for Class activity 2 of ISS

Errors I found : 
1. There should be an ':' at the end of the function definition, before we start describing the function i.e. 
    def find_cube_pairs(target) **:**

2. The list 'solutions' was renamed to 'sol', as sol list is referenced ahead in the code, not solutions.

3. Exponentiation syntax was fixed, as the syntax uses two asterisks, not three. 

4. variable 'targ' was renamed to 'target', as the variable name given as input for the function is 'target', not 'targ'.

5. The code called a function 'ranges', which is wrong. The function to be called is 'range', therefore ranges has been renamed to 'range' wherever found.

6. The for loops missed ':' after the for statement, which i have added.

7. The if condition : "if a**3 + b**3 == target" missed a ':' after the if statement, which I have added.

8. 'printf' function was called instead of 'print', which is the function to print in python. I have changed the function name wherever applicable.

9. Changed variable name 'pairs' to 'pair', as 'pair' is referenced later in the code, not 'pairs'

10. Removed extra commas and semicolons that were placed

11. Changed 1728 to 1729, as we called function for 1729, not 1728
