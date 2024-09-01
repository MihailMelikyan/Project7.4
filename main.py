team_1 = 'Мастера кода участников'
team_2 = 'Волшебники данных'
#изпользование %

team1_num = 5
print('В команде Мастера кода участников:%s!' % 5 )
team1_num = 6
print('Итого сегодня в командах участников: %s и %s!' %(5,6))

#Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач: {} !'.format(42))
team1_time = 18015.2
print('Волшебники данных решили задачи за {} с !'.format(18015.2))
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')


def chaleng_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result =  f'Победа команды {team_1}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f'Победа команды {team_2}!'
    else:
        result = f'Ничья'

# def tasks_total():



