import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")  # Oyuna hoşgeldiniz mesajı
    print("I have picked a number between 1 and 100. Try to guess it.")  # Bilgisayarın 1 ile 100 arasında bir sayı seçtiğini bildir

    # Computer selects a random number
    secret_number = random.randint(1, 100)  # Bilgisayar rastgele bir sayı seçer
    guess_count = 0  # Tahmin sayısını başlat

    while True:
        # Get a guess from the user
        guess = int(input("Your guess: "))  # Kullanıcıdan bir tahmin al
        guess_count += 1  # Tahmin sayısını bir arttır

        # Check if the guess is correct
        if guess < secret_number:
            print("Try a higher number.")  # Daha yüksek bir sayı denemesi gerektiğini bildir
        elif guess > secret_number:
            print("Try a lower number.")  # Daha düşük bir sayı denemesi gerektiğini bildir
        else:
            print(f"Congratulations! You found the secret number {secret_number} in {guess_count} guesses.")  # Doğru tahmin edildiğinde tebrik mesajı
            break  # Döngüyü sonlandır

# Start the game
number_guessing_game()  # Oyunu başlat
