from graphics import *
import math

def Mathlete():
    results = []
    attempts = 0
    for i in range(37):
        results.append(0)
    for x in range(1, 7):
        for y in range(1, 7):
            for op in range(3):
                if op == 0:
                    answer = x + y
                elif op == 1:
                    answer = x - y
                else:
                    answer = x * y
                if answer < 0:
                    results[0] += 1
                else:
                    results[answer] += 1
                attempts += 1
    graph = GraphWin("Bar Graph", 1400, 200)
    graph.setCoords(-1.5, -1.5, 37, 24)
    counter = 3
    while counter <= 21:
        number = Text(Point(-1, counter), str(counter))
        number.draw(graph)
        line = Line(Point(-0.7, counter), Point(37, counter))
        line.draw(graph)
        counter += 3
    for i in range(len(results)):
        number = Text(Point(i, -1), str(i))
        number.draw(graph)
        if i % 2 == 0:
            height = results[i]+2
        else:
            height = results[i]+1
        percentage = Text(Point(i, height), str(round(results[i]/attempts*100, 4))+"%")
        percentage.draw(graph)
        box = Rectangle(Point(i-.25, 0), Point(i+.25, results[i]))
        if i % 3 == 0:
            box.setFill(color_rgb(255, 0, 0))
        elif i % 3 == 1:
            box.setFill(color_rgb(0, 255, 0))
        else:
            box.setFill(color_rgb(0, 0, 255))
        box.draw(graph)
    graph.getMouse()

def FightCards():
    player1Wins = 0
    player3Wins = 0
    remaining1 = 3
    while remaining1 >= 0:
        chance1 = math.factorial(3)/(math.factorial(remaining1)*math.factorial(3-remaining1))*(1/3)**remaining1*(2/3)**(3-remaining1)
        remaining2 = remaining1
        while remaining2 >= 0 and remaining1 > 0:
            chance2 = chance1 * math.factorial(remaining1)/(math.factorial(remaining2)*math.factorial(remaining1-remaining2))*(1/3)**remaining2*(2/3)**(remaining1-remaining2)
            remaining3 = remaining2
            while remaining3 >= 0 and remaining2 > 0:
                chance3 = chance2 * math.factorial(remaining2)/(math.factorial(remaining3)*math.factorial(remaining2-remaining3))*(1/3)**remaining3*(2/3)**(remaining2-remaining3)
                remaining4 = remaining3
                while remaining4 >= 0 and remaining3 > 0:
                    chance4 = chance3 * math.factorial(remaining3)/(math.factorial(remaining4)*math.factorial(remaining3-remaining4))*(1/3)**remaining4*(2/3)**(remaining3-remaining4)
                    remaining5 = remaining4
                    while remaining5 >= 0 and remaining4 > 0:
                        chance5 = chance4 * math.factorial(remaining4)/(math.factorial(remaining5)*math.factorial(remaining4-remaining5))*(1/3)**remaining5*(2/3)**(remaining4-remaining5)
                        if remaining5 == 0:
                            player1Wins += chance5
                        else:
                            player3Wins += chance5
                        remaining5 -= 1
                    if remaining4 == 0:
                        player1Wins += chance4
                    remaining4 -= 1
                if remaining3 == 0:
                    player1Wins += chance3
                remaining3 -= 1
            if remaining2 == 0:
                player1Wins += chance2
            remaining2 -= 1
        if remaining1 == 0:
            player1Wins += chance1
        remaining1 -= 1
    print("The solo player wins " + str(round(player1Wins, 4)) + "% of the time.")
    print("The team of 3 wins " + str(round(player3Wins, 4)) + "% of the time.")

def main():
    games = GraphWin("Minigames", 400, 200)
    games.setCoords(0, 0, 1, 1)
    divider = Line(Point(0.5, 0), Point(0.5, 1))
    divider.draw(games)
    text1 = Text(Point(0.25, 0.5), "Mathletes")
    text1.draw(games)
    text2 = Text(Point(0.75, 0.5), "Fight Cards")
    text2.draw(games)
    choice = games.getMouse()
    if choice.x < 0.5:
        Mathlete()
    else:
        FightCards()

main()