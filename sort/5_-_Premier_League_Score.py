class FootBall:
    def __init__(self, name, win, loss, draws, scored, conceded):
        self.name = name
        self.win = int(win)
        self.loss = int(loss)
        self.draws = int(draws)
        self.scored = int(scored)
        self.conceded = int(conceded)
        self.points = 3 * self.win + 0 * self.loss + 1 * self.draws
        self.goal_difference = self.scored - self.conceded

    def __str__(self):
        return "['{0}', {{'points': {1}}}, {{'gd': {2}}}]".format(self.name, self.points, self.goal_difference)
    
def merge_sort(lst, left, right):
    if(left < right):
        center = (left + right) // 2
        merge_sort(lst, left, center)
        merge_sort(lst, center+1, right)
        merge(lst, left, center+1, right)

def merge(lst, left, right, right_end):
    start = left
    left_end = right - 1
    result = []
    while left <= left_end and right <= right_end:
        if lst[left].points > lst[right].points:
            result.append(lst[left])
            left += 1
        elif lst[left].points == lst[right].points:
            if lst[left].goal_difference >= lst[right].goal_difference:
                result.append(lst[left])
                left += 1
            else:
                result.append(lst[right])
                right += 1
        else:
            result.append(lst[right])
            right += 1
    while left <= left_end:
        result.append(lst[left])
        left += 1
    while right <= right_end:
        result.append(lst[right])
        right += 1
    for value in result:
        lst[start] = value
        start += 1
        if start > right_end:
            break

football_teams = input("Enter Input : ").split("/")
teams = []
for group in football_teams:
    team = group.split(",")
    football = FootBall(team[0], team[1], team[2], team[3], team[4], team[5])
    teams.append(football)
print("== results ==")
merge_sort(teams, 0, len(teams) - 1)
for team in teams:
    print(team)