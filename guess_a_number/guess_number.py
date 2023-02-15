"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1)-> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    start_number = 1
    end_number = 101
    count = 0
    
    while True:
        count += 1
        predict_number =  (start_number + end_number) // 2 # сужаем диапазон поиска
        if number > predict_number:
            start_number = predict_number
        elif number < predict_number:
            end_number = predict_number
        else:
            break # число угадано
        
    return count

def score_game(random_predict) -> int:
    """Среднее количество попыток, за которое программа угадывает число

    Args:
        random_predict (number): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_list = [] # список кол-ва попыток
    np.random.seed(1)  # фиксируем последовательность
    random_array = np.random.randint(1, 101, size=(1000))  
    
    for number in random_array:
        count_list.append(random_predict(number))
        score = int(np.mean(count_list)) # вычисляем среднее кол-во попыток
        print(f'Программа угадывает число в среднем за {score} попытки')
        break
    
    return score 

if __name__ == "__main__":
    # RUN
    score_game(random_predict)