"""marksheet = []
for _ in range(0, int(input())):
    marksheet.append([input(), float(input())])
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))"""

"""n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total_marks = sum(student_marks[query_name])
average_marks = total_marks/3
print("%.2f"%(average_marks))"""

"""n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()
query_scores = student_marks[query_name]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))"""

"""meal_cost = float(input())
tip = int(input())
tax = int(input())

total_tip = (meal_cost/100)*tip
total_tax = (tax/100*tip)
total_cost = meal_cost+total_tip+total_tax
total_cost2 = int(round(meal_cost + (meal_cost/100*tip) + (tax/100*tip)))
print(total_tip)
print(total_tax)
print(total_cost)
print(round(total_cost2))"""

"""first = int(input())
second = float(input())
third = input()
text = "Hacker Rank"
result1 = int(first+second)
result2 = float(second+second)
result3 = (text+third)
print(result1)
print(result2)
print(result3)"""

i = 4
d = 4.0
s = 'Hacker Rank'
st = input()
print(int(i+d))
print(d+d)
print(s+st)
