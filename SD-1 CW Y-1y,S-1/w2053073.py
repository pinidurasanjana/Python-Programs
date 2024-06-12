from graphics import *

t = 0  # total outcomes
j = 0  # Progress
k = 0  # Progress(module trailer)
p = 0  # Do not progress – module retriever
m = 0  # Exclude

output_list = []
Pass_list = []
Defer_list = []
Fail_list = []


def outcome_progression():
    global t, j, k, p, m, maximum_number, output_list, Pass_list, Defer_list, Fail_list

    while True:
        try:
            Pass = int(input("Please enter your credits at pass: "))
            while True:
                if Pass in [0, 20, 40, 60, 80, 100, 120]:
                    break
                else:
                    print('Out of range.')
                    Pass = int(input("Please enter your credits at pass: "))
            Pass_list.append(Pass)
            break
        except ValueError:
            print('Integer required')
    while True:
        try:
            Defer = int(input("Please enter your credits at defer: "))
            while True:
                if Defer in [0, 20, 40, 60, 80, 100, 120]:
                    break
                else:
                    print('Out of range.')
                    Defer = int(input("Please enter your credits at defer: "))
            Defer_list.append(Defer)
            break
        except ValueError:
            print('Integer required')
    while True:
        try:
            Fail = int(input("Please enter your credits at fail: "))
            while True:
                if Fail in [0, 20, 40, 60, 80, 100, 120]:
                    break
                else:
                    print('Out of range.')
                    Fail = int(input("Please enter your credits at fail: "))
            Fail_list.append(Fail)
            break
        except ValueError:
            print('Integer required')
    total = Pass + Defer + Fail
    if total > 120:
        print('Total incorrect')
    elif Pass == 120:
        print('Progress')
        j += 1
        output_list.append('Progress')
    elif Pass == 100:
        if Defer == 20:
            print('Progress(module trailer)')
        elif Fail == 20:
            print('Progress(module trailer)')
        k += 1
        output_list.append('Progress(module trailer)')
    elif 0 <= Pass <= 80:
        if 0 <= Defer <= 120:
            if 0 <= Fail <= 60:
                print('Do not progress – module retriever')
                p += 1
                output_list.append('Do not progress – module retriever')
            else:
                print('Exclude')
                m += 1
                output_list.append('Exclude')
    maximum_number = int(max(j, k, p, m))

    t = j+k+p+m

def another_data():
    while True:
        print('Would you like to enter another set of data?')
        selection = input('Enter \'y\' for yes or \'q\' to quit and view results: ')
        if selection == 'y':
            outcome_progression()
        elif selection == 'q':
            break
        else:
            print("invalid input")


def main():
    win = GraphWin("Histogram", 800, 600)  # open a window object called "win" with size and title
    win.setBackground("Mint cream")  # Set the background colour of the window

    aL = Line(Point(100, 500), Point(700, 500))
    aL.draw(win)

    aR = Rectangle(Point(250, 500), Point(125, (500 - ((400 / maximum_number) * j))))
    aR.setOutline("black")
    aR.draw(win)
    message = Text(Point(187.5, (500 - ((400 / maximum_number) * j) - 10)), j)
    message.draw(win)
    message = Text(Point(187.5, 515), "Progress")
    message.draw(win)
    aR.setFill("palegreen")

    aR = Rectangle(Point(385, 500), Point(260, (500 - ((400 / maximum_number) * k))))
    aR.draw(win)
    message = Text(Point(322.5, (500 - ((400 / maximum_number) * k) - 10)), k)
    message.draw(win)
    message = Text(Point(322.5, 515), "Trailer")
    message.draw(win)
    aR.setFill("darkseagreen")

    aR = Rectangle(Point(520, 500), Point(395, (500 - ((400 / maximum_number) * p))))
    aR.draw(win)
    message = Text(Point(457.5, (500 - ((400 / maximum_number) * p) - 10)), p)
    message.draw(win)
    message = Text(Point(457.5, 515), "Retriever")
    message.draw(win)
    aR.setFill("darkkhaki")

    aR = Rectangle(Point(655, 500), Point(530, (500 - ((400 / maximum_number) * m))))
    aR.draw(win)
    message = Text(Point(592.5, (500 - ((400 / maximum_number) * m) - 10)), m)
    message.draw(win)
    message = Text(Point(592.5, 515), "Excluded")
    message.draw(win)
    aR.setFill("thistle")

    message = Text(Point(200, 540), str(t) + " outcomes in total.")
    message.draw(win)

    message = Text(Point(187.5, 25), "Histogram Results.")
    message.draw(win)

    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


# part 2
def display_list():
    print("\nPart 2:")
    for i in range(len(output_list)):
        print(f"{output_list[i]}- {Pass_list[i], Defer_list[i], Fail_list[i]}\n")


# part 3
def save_to_file():
    with open("Inputs.txt", "w") as file:
        for i in range(len(output_list)):
            file.write(f"{output_list[i]}- {Pass_list[i]}, {Defer_list[i]}, {Fail_list[i]}\n")
    print("\nPart 3: \nData save to 'Inputs.txt'")


user = int(input("Select your identity \n 1-Staff \n 2-Student \n: "))
if user == 1:
    outcome_progression()
    another_data()
    main()
    display_list()
    save_to_file()
elif user == 2:
    outcome_progression()
    another_data()
    display_list()
    save_to_file()
else:
    print("Invalid Input")

print("\nHistogram")
print("Progress " + str(j) + " : " + str("*" * j))
print("Trailer " + str(k) + " : " + str("*" * k))
print("Retriever " + str(p) + " : " + str("*" * p))
print("Exclude " + str(m) + " : " + str("*" * m))

print(str(t)+" outcomes in total.")
