def play_game():
    # Define a set of possible secret numbers
    possible_numbers = {6, 7, 5,8, 9}
    
    # Initialize points
    points = 0
    
    # Number of guesses allowed
    max_guesses = 3
    
    # Pop a number from the set for this game
    
    # Loop for the number of guesses allowed
    for _ in range(max_guesses):
        secret_number = possible_numbers.pop()
        print(secret_number)
        guess = int(input("Guess a number between 1 and 9: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            points += 10
            print("Congratulations! You guessed the correct number.")
            
        else:
            print("Incorrect guess. Try again.")
    
    


    
    # Display points earned
    if points==30:
        print("maximum Points earned:", points)
    elif points==20:
        print("not maximum Points earned:", points)
    else:
        print("minimum Points earned:", points)



# Play the game
play_game()
