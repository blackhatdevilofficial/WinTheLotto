import random

# Functie om 'hoog kans' nummers te genereren
def generate_lotto_numbers():
    # Stel de lotto nummers van 1 t/m 49 voor, kies 6
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return numbers

# Functie om een leuke boodschap te geven
def cheerful_message():
    messages = [
        "Hiep hiep hoera! Kijk eens naar deze geluksnummers 🎉",
        "Wow! Deze nummers stralen geluk uit ✨",
        "Voel de magie! Hier zijn jouw winnende kansen 🍀",
        "Tadaaa! Klaar voor de jackpot met deze nummers 💰",
        "Spring van blijdschap! Jouw lot-nummers zijn hier 😄",
        "Laat het geluk beginnen! Hier zijn ze 🌟"
    ]
    return random.choice(messages)

# Hoofdprogramma
if __name__ == "__main__":
    print("\n🎲 Welkom bij WinTheLotto! 🎲\n")
    lotto_numbers = generate_lotto_numbers()
    print(cheerful_message())
    print("Jouw lotto-nummers zijn:", lotto_numbers)
    print("\nSucces! Moge het geluk aan jouw zijde staan! 🍀\n")
