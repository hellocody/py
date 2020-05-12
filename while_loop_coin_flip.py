while (computer_score < 5):
    while (player_score < 5):
        print('Choose: Heads or Tails')
        player_coin = input()
        print('You chose: ' + player_coin)
        print('Flipping the coin. . .')
        coin_face = random.randint(0, 1)
        if(coin_face == 0):
            coin_face = 'Heads'
        else:
            coin_face = 'Tails'
        print("It's " + coin_face + "!")
        if(coin_face == player_coin):
            player_score = player_score + 1
        else:
            computer_score = computer_score + 1
        print(f'You have a score of {player_score}. The Computer has a score of {computer_score}.')
        if(player_score == 5):
            print('You win! Congrats!')
            print('Would you like to play again? Y or N?')
            play_again = input()
            if(play_again == 'Y'):
                print('Reloading. . .')
                computer_score = 0
                player_score = 0
                continue
            else:
                print('Thanks for playing.')
                break
        elif(computer_score == 5):
            print('You lose. Sorry!')
            print('Would you like to play again? Y or N?')
            play_again = input()
            if(play_again == 'Y'):
                print('Reloading. . .')
                computer_score = 0
                player_score = 0
                continue
            else:
                print('Thanks for playing.')
                break
    break
