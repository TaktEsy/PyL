team1 = 'Мастера кода'
team2 = "Волшебники данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 17015.2

print('В команде Мастера кода участников: %s' % team1_num)
print('В команде Волшебники данных участников: %s' % team2_num)
print('Итого сегодня в командах участников: %s и %s \n' % (team1_num, team2_num))


print("Команда {} решила задач: {} !".format(team1, score_1))
print("Команда {} решила задач: {} !".format(team2, score_2))
print("{} решили задачи за {} cек".format(team1, team1_time))
print("{} решили задачи за {} сек".format(team2, team2_time))

print(f"Всего решили:\n{team1}:{score_1}\n{team2}:{score_2}\nВсего затрачено, (сек)\n{team1}:{team1_time}\n{team2}:{team2_time}\nСр. время на задачу:\n{team1}:{team1_time/score_1}\n{team2}:{team2_time/score_2}\n")