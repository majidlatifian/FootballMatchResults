wins = 0
draws = 0
losses = 0
count = 0

for _ in range(30):
    result = int(input("Enter the match result (0 for loss, 1 for draw, 3 for win): "))
    if result == 0:
        losses += 1
    elif result == 1:
        draws += 1
        count += result
    elif result == 3:
        wins += 1
        count += result
    else:
        print("Invalid input. Please enter 0, 1, or 3.")

print("Number of Wins:", wins)
print("Number of Draws:", draws)
print("Number of Losses:", losses)
print("Occurrences of 3:", count)