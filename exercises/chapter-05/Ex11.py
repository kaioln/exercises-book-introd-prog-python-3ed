points = 0
question = 1

while question <= 3:
    response = input(f"Question response {question}: ")
    if question == 1 and response == "b" or response == "B":
        points = points + 1
    if question == 2 and response == "c" or response == "C":
        points = points + 1
    if question == 3 and response == "d" or response == "D":
        points = points + 1
    question = question + 1
print(f"The student scored {points} points")