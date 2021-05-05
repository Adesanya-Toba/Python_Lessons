i = 1
while i <= 5:
    print('*' * i)  # multiplying string
    i += 1
print("Done\n")

# Guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
print("Welcome to the Guessing Game!")

while guess_count < guess_limit:
    guess = int(input('Enter your guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Correct, You won!\n')
        break
    else:
        tries = guess_limit - guess_count
        if tries < 2:
            print(f"Wrong guess. You have {tries} try left.\n")
        else:
            print(f"Wrong guess. You have {tries} tries left.\n")
else:
    print("Sorry, you lost!")