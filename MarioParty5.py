from graphics import *

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