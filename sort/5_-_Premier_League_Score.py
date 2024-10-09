'''
สร้างฟังก์ชันที่นำชุดข้อมูล(list)ของ football clubs ที่มีคุณสมบัติดังนี้ name, wins, loss, draws, scored, conceded และทำการ return list ของ team name โดยเรียงลำดับทีมที่มีคะแนน(total point)มากที่สุด โดยถ้าหากมีทีมที่คะแนนเท่ากัน ให้นำผลต่างของจำนวนประตูที่ทำได้(scored)กับจำนวนประตูที่เสีย(conceded) มาคิด

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

[ชนะได้ 3 คะแนน, เสมอได้ 1 คะแนน, แพ้ได้ 0 คะแนน]

ตัวอย่าง

team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68

Testcase student: #1/7
Enter Input : Manchester United,30,3,5,88,20/Arsenal,24,6,8,98,29/Chelsea,22,8,8,98,29
== results ==
['Manchester United', {'points': 95}, {'gd': 68}]
['Arsenal', {'points': 80}, {'gd': 69}]
['Chelsea', {'points': 74}, {'gd': 69}]

Testcase student: #2/7 2
Enter Input : Manchester City,30,8,0,67,20/Liverpool,34,2,2,118,29/Leicester City,22,8,8,98,29
== results ==
['Liverpool', {'points': 104}, {'gd': 89}]
['Manchester City', {'points': 90}, {'gd': 47}]
['Leicester City', {'points': 74}, {'gd': 69}]

Testcase student: #3/7
Enter Input : Manchester City,30,6,2,102,20/Liverpool,24,6,8,118,29/Arsenal,30,0,8,87,39
== results ==
['Arsenal', {'points': 98}, {'gd': 48}]
['Manchester City', {'points': 92}, {'gd': 82}]
['Liverpool', {'points': 80}, {'gd': 89}]

Testcase student: #4/7
Enter Input : Manchester United,30,8,0,67,20/New Castle United,34,2,2,118,36/Leicester City,34,2,2,108,21
== results ==
['Leicester City', {'points': 104}, {'gd': 87}]
['New Castle United', {'points': 104}, {'gd': 82}]
['Manchester United', {'points': 90}, {'gd': 47}]

Testcase student: #5/7
Enter Input : Manchester City,30,6,2,102,20/Liverpool,24,6,8,118,29/Arsenal,28,2,8,87,39
== results ==
['Manchester City', {'points': 92}, {'gd': 82}]
['Arsenal', {'points': 92}, {'gd': 48}]
['Liverpool', {'points': 80}, {'gd': 89}]

Testcase student: #6/7 6
Enter Input : Chelsea,35,3,0,102,20/Manchester City,30,6,2,102,20/Liverpool,24,6,8,118,29/Arsenal,28,2,8,87,39
== results ==
['Chelsea', {'points': 105}, {'gd': 82}]
['Manchester City', {'points': 92}, {'gd': 82}]
['Arsenal', {'points': 92}, {'gd': 48}]
['Liverpool', {'points': 80}, {'gd': 89}]

Testcase student: #7/7
Enter Input : Wolverhampton,4,2,1,8,8/Liverpool,5,1,1,17,15/Chelsea,3,1,3,16,9/Leicester City,5,2,0,17,9/Arsenal,4,3,0,9,7/Manchester City,3,1,2,9,8/Manchester United,2,3,1,9,13/Souththampton,4,2,1,14,12/Tottenham Hotspur,4,1,2,18,9/Everton,4,2,1,15,11/Aston Villa,4,2,0,15,9
== results ==
['Liverpool', {'points': 16}, {'gd': 2}]
['Leicester City', {'points': 15}, {'gd': 8}]
['Tottenham Hotspur', {'points': 14}, {'gd': 9}]
['Everton', {'points': 13}, {'gd': 4}]
['Souththampton', {'points': 13}, {'gd': 2}]
['Wolverhampton', {'points': 13}, {'gd': 0}]
['Chelsea', {'points': 12}, {'gd': 7}]
['Aston Villa', {'points': 12}, {'gd': 6}]
['Arsenal', {'points': 12}, {'gd': 2}]
['Manchester City', {'points': 11}, {'gd': 1}]
['Manchester United', {'points': 7}, {'gd': -4}]
'''

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