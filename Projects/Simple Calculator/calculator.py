def Calculator():
    while True:
        '''
        Python eval() function is used to 
        parse an expression as an argument 
        and then execute it within the Python 
        program. The Python eval() is a built-in 
        function that allows us to evaluate the 
        Python expression as a 'string' and return 
        the value as an integer.
        '''
        try:
            a = input("Your calculation: ")
            result = eval(a)
            print(result)
        except Exception as e:
            print("Error:", e)
            print("Please enter a valid numerical expression\n")

if __name__ == "__main__":
    Calculator()