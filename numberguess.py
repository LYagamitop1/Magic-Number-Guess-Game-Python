

def playagain():
    import random

    magicnumber = random.randint(1,100)

    userinpt = int(input("Guess the magic number: "))
    tries = 0

    while userinpt!=magicnumber:
        if userinpt>magicnumber:
            print(f"The Magic number is less than {userinpt}")
        else:
            print(f"The Magic number is greater than {userinpt}")
        
        
        tries +=1
    
    
        userinpt=int(input("Guess again: "))
    
    
    
    print(f"""Hurray! You finally got it after {tries} tries.
The Magic number is {magicnumber}""")
    
    x = input("If you want to play again then enter 'a', if you want to exit then enter anything else : ")
    if x =="a":
        playagain()
    else:
        return

    
    

playagain()
    
