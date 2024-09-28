class Command:
    def __init__ (self, name: str, count: int, score: int, time: float):
        self.name = name
        self.count = count
        self.score = score
        self.time = time
        print('В команде %s участников: %s!' % (self.name, self.count))

    def __str__(self):
        return self.name
    
    def get_score(self):
        print('Команда {} решила задач: {} !'.format(self.name, self.score))

    def get_time(self):
        print('{} решили задачи за {} с !'.format(self.name, self.time))

    def __gt__(self, other):
        if isinstance(other, Command):
            return self.score > other.score
        return NotImplemented

def challenge_result(*teams: Command):
    winner = teams[0]
    tasks_total = 0
    time_total = 0
    for team in teams:
        tasks_total += team.score
        time_total += team.time
        if team > winner:
            winner = team
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_total/tasks_total, 2)} секунды на задачу!.')
    return f'Результат битвы: победа команды {winner}!'


team1 = Command('Мастера кода', 5, 43, 18056.05)
team2 = Command('Волшебники данных', 6, 45, 18064.55)
print()
print('Итого сегодня в командах участников: %s и %s !' % (team1.count, team2.count))
team1.get_score()
team2.get_score()
print()
team1.get_time()
team2.get_time()
print()
print(f'Команды решили {team1.score} и {team2.score} задач.')
print()
print(challenge_result(team1, team2))