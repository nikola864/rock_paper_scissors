import random

# создаём класс для подсчёта очков
class ScoreBoard:
    def init(self):
        self.user_point = 0
        self.comp_point = 0

    # определяем кому давать очко
    def update_score(self, winner):
        if winner == 'user':
            self.user_point += 1
        if winner == 'comp':
            self.comp_point += 1
    def display_score(self): # показываем после каждого раунда счёт
        print(f"\nТекущий счёт:")
        print(f"Игрок: {self.user_point}  |  Компьютер: {self.comp_point}")
        print("------------------------")



def play_game(): # основная функция
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'")
    print("Правила игры: камень побеждает ножницы, ножницы побеждает бумагу, бумага побеждает камень")

    options = ["камень","ножницы","бумага"]# список из которого компьютер делает выбор
    score_board = ScoreBoard()
    while True:
        user_choice = input("Выберите камень,ножницы или бумагу(для оканчания игры напишите 'выход'):")
        # условия если юзер захочет закончить игру
        if user_choice == "выход":
            print("Спасибо за игру! До новых встреч!!!")
            break
        # условие если юзер ввёл что-то другое(не камень, ножницы, бумага)
        if user_choice not in options:
            print("Некорректный ввод данных! Посмотрите правила игры и попробуйте ещё раз!")
            continue
        # чтоб ввод был красивым и понятным пользователю
        comp_choice = random.choice(options)
        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор_компьютера: {comp_choice}")
        # условие если ничья
        if comp_choice == user_choice:
            print("Ничья")

        # условия определения победителя
        if user_choice == "камень" and comp_choice == "ножницы":
            print("Ты победил")
            score_board.update_score('user')
        if user_choice == "камень" and comp_choice == "бумага":
            print("Компьютер победил")
            score_board.update_score('comp')
        if user_choice == "ножницы" and comp_choice == "камень":
            print("Компьютер победил")
            score_board.update_score('comp')
        if user_choice == "ножницы" and comp_choice == "бумага":
            print("Ты победил")
            score_board.update_score('user')
        if user_choice == "бумага" and comp_choice == "камень":
            print("Ты победил")
            score_board.update_score('user')
        if user_choice == "бумага" and comp_choice == "ножницы":
            print("Компьютер победил")
            score_board.update_score('comp')

        score_board.display_score()


if name == 'main':
    play_game()