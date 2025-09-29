def play_mystery_game():
    name = input("Enter your detective name: ")
    print(f"\nWelcome, Detective {name}. A priceless ruby, 'The Crimson Star,' has been stolen.")
    print("Your suspects are the three people who had access to the vault last night:")
    print("- Ms. Thorne, the curator")
    print("- Mr. Finch, the security guard")
    print("- Dr. Vance, the expert")
    
    clues_found = {}
    
    while True:
        print("\nChoose a location to investigate:")
        print("1. The Curator's Office")
        print("2. The Security Booth")
        print("3. The Ruby's Display Case")
        print("Type 'solve' if you think you have enough information.")
        print("Type 'quit' to exit the game.")
        
        choice = input("Your choice: ").lower()

        if choice == '1':
            if 'office_clue' not in clues_found:
                print("\nYou find a handwritten note from the museum owner, threatening to fire the curator if she didn't get rid of the ruby.")
                clues_found['office_clue'] = "note"
                print("Clue found: A note from the owner.")
            else:
                print("You've already investigated this location. Try another one.")
        
        elif choice == '2':
            if 'booth_clue' not in clues_found:
                print("\nInside the security booth, you find a small, coded keycard hidden under the desk.")
                clues_found['booth_clue'] = "keycard"
                print("Clue found: A coded keycard.")
            else:
                print("You've already investigated this location. Try another one.")

        elif choice == '3':
            if 'display_clue' not in clues_found:
                print("\nAt the display case, you find faint red residue on the inside of the glass. It smells like a specific type of cleaning solution.")
                clues_found['display_clue'] = "residue"
                print("Clue found: Red residue on the glass.")
            else:
                print("You've already investigated this location. Try another one.")

        elif choice == 'solve':
            print("\n--- Time to make your final accusation. ---")
            print("Based on your investigation, who do you believe is the thief?")
            print("1. Ms. Thorne")
            print("2. Mr. Finch")
            print("3. Dr. Vance")
            print("4. All three worked together")
            
            final_guess = input("Enter your final guess (1, 2, 3, or 4): ")

            if final_guess == '4':
                print("\nYour deduction is correct! You realize the clues point to a conspiracy. The keycard let Finch bypass security, Vance's residue covered their tracks, and Thorne's motive was a threat from her boss. All three are arrested.")
                print("--- YOU WIN! You have solved the case! ---")
            else:
                print("\nYour accusation is incorrect. The real culprits go free, and the ruby is lost forever.")
                print("--- YOU LOSE. ---")
            break 
        elif choice == 'quit':
            print("Thanks for playing. The investigation is over.")
            break
            
        else:
            print("Invalid input. Please choose a valid option.")

    print(f"\nThanks for playing, {name}.")

play_mystery_game()