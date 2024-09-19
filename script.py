import random

def get_computer_choice():
    """Функція для вибору комп'ютера: камінь, ножиці або папір."""
    choices = ["камінь", "ножиці", "папір"]
    return random.choice(choices)

def get_user_choice():
    """Функція для введення вибору користувача."""
    while True:
        choice = input("Виберіть: камінь, ножиці або папір: ").lower()
        if choice in ["камінь", "ножиці", "папір"]:
            return choice
        print("Невірний вибір, спробуйте ще раз.")

def determine_winner(user_choice, computer_choice):
    """Функція для визначення переможця раунду."""
    if user_choice == computer_choice:
        return "нічия"
    elif (user_choice == "камінь" and computer_choice == "ножиці") or \
         (user_choice == "ножиці" and computer_choice == "папір") or \
         (user_choice == "папір" and computer_choice == "камінь"):
        return "користувач"
    else:
        return "комп'ютер"

def play_round():
    """Один раунд гри."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Комп'ютер вибрав: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "нічия":
        print("Це нічия!")
    elif winner == "користувач":
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")
    
    return winner

def play_game():
    """Основна функція для запуску гри."""
    user_score = 0
    computer_score = 0
    rounds_played = 0
    
    while True:
        print("\nРаунд", rounds_played + 1)
        winner = play_round()
        
        if winner == "користувач":
            user_score += 1
        elif winner == "комп'ютер":
            computer_score += 1
        
        rounds_played += 1
        
        print(f"\nРахунок: Користувач {user_score} - {computer_score} Комп'ютер")
        
        # Запитуємо, чи хоче користувач грати ще
        play_again = input("Хочете зіграти ще раз? (так/ні): ").lower()
        if play_again != "так":
            break
    
    print("\nГра завершена!")
    print(f"Загальний рахунок: Користувач {user_score} - {computer_score} Комп'ютер")
    print(f"Зіграно раундів: {rounds_played}")

# Запускаємо гру
play_game()
