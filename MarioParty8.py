from graphics import *
from random import *

def CutFromtheTeam(wires, cut, placements, cutting, results):
    while placements[cutting] != "":
        cutting = (cutting + 1) % 4
    for i in range(10):
        if not cut[i]:
            cut[i] = True
            if wires[i]:
                placements[cutting] = placements.count("")
            if cut.count(False) > 0:
                results = CutFromtheTeam(wires, cut, placements, (cutting + 1) % 4, results)
            else:
                game = []
                for j in range(len(placements)):
                    if placements[j] == "":
                        game.append(1)
                    else:
                        game.append(placements[j])
                results.append(game)
            cut[i] = False
            placements[cutting] = ""
    return results

def main():
    temp = True
    if temp:
        graph = GraphWin("Bar Graph", 1250, 500)
        graph.setCoords(0, 0, 4, 1500000)
        wires = []
        cut = []
        for i in range(10):
            wires.append(False)
            cut.append(False)
        bad = []
        counter = 0
        while counter < 3:
            number = randrange(0, 10)
            inList = False
            for i in range(len(bad)):
                if bad[i] == number:
                    inList = True
            if not inList:
                bad.append(number)
                counter += 1
        bad.sort()
        counter = 0
        for i in range(len(wires)):
            if i == bad[counter]:
                wires[i] = True
                counter += 1
                if counter == 3:
                    break
        placements = ["", "", "", ""]
        results = []
        results = CutFromtheTeam(wires, cut, placements, 0, results)
        text = []
        for i in range(1, 5):
            placements = [0, 0, 0, 0]
            for j in range(len(results)):
                for k in range(len(results[j])):
                    if results[j][k] == i:
                        placements[k] += 1
            for j in range(4):
                box = Rectangle(Point(j+i*0.2-0.1, 0), Point(j+i*0.2+0.1, placements[j]))
                if j == 0:
                    box.setFill(color_rgb(0, 0, 255))
                elif j == 1:
                    box.setFill(color_rgb(255, 0, 0))
                elif j == 2:
                    box.setFill(color_rgb(0, 255, 0))
                else:
                    box.setFill(color_rgb(255, 255, 0))
                box.draw(graph)
                text.append(Text(Point(j+i*0.2, placements[j]+20000), str(round(placements[j]/len(results)*100, 3)) + "%"))
        for i in range(len(text)):
            text[i].draw(graph)
        graph.getMouse()

main()