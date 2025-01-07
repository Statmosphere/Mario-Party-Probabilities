from graphics import *
import math

def HideAndGoBoom():
    player1Wins = 0
    player3Wins = 0
    buttons = ["B", "A", "Y", "X"]
    hidingPlaces = ["", "", ""]
    for x in range(4):
        hidingPlaces[0] = buttons[x]
        for y in range(4):
            hidingPlaces[1] = buttons[y]
            for z in range(4):
                hidingPlaces[2] = buttons[z]
                unique = set(hidingPlaces)
                player3Wins += len(unique)/4/64
                player1Wins += (4-len(unique))/4/64
    pieChart = GraphWin("Hide and Go Boom", 350, 350)
    pieChart.setCoords(-1.01, -1.01, 1.01, 1.01)
    circle = Circle(Point(0, 0), 1)
    circle.draw(pieChart)
    line1 = Line(Point(0, 0), Point(0, 1))
    line1.draw(pieChart)
    line2 = Line(Point(0, 0), Point(math.cos(2*math.pi*player1Wins+math.pi/2), math.sin(2*math.pi*player1Wins+math.pi/2)))
    line2.draw(pieChart)
    text1 = Text(Point(math.cos(math.pi*player1Wins+math.pi/2)*0.5, math.sin(math.pi*player1Wins+math.pi/2)*0.5), str(player1Wins*100)+"%")
    text1.draw(pieChart)
    text2 = Text(Point(-math.cos(math.pi*player1Wins+math.pi/2)*0.5, -math.sin(math.pi*player1Wins+math.pi/2)*0.5), str(player3Wins*100)+"%")
    text2.draw(pieChart)
    text3 = Text(Point(-0.75, 0.9), "Solo Player")
    text3.draw(pieChart)
    text4 = Text(Point(0.75, 0.9), "Team of 3")
    text4.draw(pieChart)
    pieChart.getMouse()

HideAndGoBoom()