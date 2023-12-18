import logging
import random
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

N = random.randint(1, int(input('Введите верхнюю границу числа: ')))
logging.info(f'Число N = {N}')
k = int(input('Введите количество попыток: '))
logging.info(f'Число k = {k}')

atmpt = 0

while atmpt <= k:
    atmpt += 1
    logging.info(f'Попытка номер {atmpt}')
    try:
        guess = int(input('Введите число: '))
    except ValueError:
        print('Неверный ввод, попробуйте снова!')
        continue
    logging.info(f'Пользователь выбрал число {atmpt}')
    
    if guess == N:
        print(f'Вы угадали за {atmpt} раз')
        logging.info(f'Вы угадали за {atmpt} раз')
        break
    
    elif guess < N:
        print('Заданное число больше, попробуйти снова!')
        logging.info('Заданное число больше, попробуйти снова!')
    elif guess > N:
        print('Заданное число меньше, попробуйте снова!')
        logging.info('Заданное число меньше, попробуйти снова!')
    