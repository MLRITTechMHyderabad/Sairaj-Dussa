probability = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}


def winner(p1_sum, p2_sum):

    p1_prob = probability[p1_sum]
    p2_prob = probability[p2_sum]
    
    if p1_sum < p2_sum:
        return "Player 1"
    elif p2_sum < p1_sum:
        return "Player 2"
    else:
        return "Draw"

def rare_roll_wins():
    R = int(input("Enter the number of rounds:"))
    if R < 1 or R > 1000:
        print("Please enter the number in between 2 to 1000")
        return

    p1_wins = 0
    p2_wins = 0

    for i in range(R):
        P1_d1, P1_d2, P2_d1, P2_d2 = map(int, input().split())
        p1_sum = P1_d1 + P1_d2
        p2_sum = P2_d1 + P2_d2

        round_winner = winner(p1_sum, p2_sum)
        if round_winner == "Player 1":
            p1_wins += 1
        elif round_winner == "Player 2":
            p2_sum += 1
    if(p1_wins > p2_wins):
        print("Player 1 Wins")
    elif(p2_wins > p1_wins):
        print("Player 2 wins")
    else:
        print("Its a Draw!!")
        
if __name__ == "__main__":
    rare_roll_wins()


