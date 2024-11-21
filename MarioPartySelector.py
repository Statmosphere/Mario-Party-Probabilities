from graphics import *

def factor(number):
    factors = [number, 1]
    i = 2
    while i < factors[0]:
        if number % i == 0:
            factors[0] = number/i
            factors[1] = i
        i += 1
    if factors[1] == 1:
        factors = factor(number + 1)
    factors[0] = int(factors[0])
    return factors

def main():
    games = ["Mario Party 1", "Mario Party 2", "Mario Party 3", "Mario Party 4", "Mario Party 5", "Mario Party 6", "Mario Party 7", "Mario Party 8",
             "Mario Party 9", "Mario Party 10", "Super Mario Party", "Mario Party Superstars", "Super Mario Party Jamboree", "Mario Party Advance",
             "Mario Party DS", "Mario Party: Island Tour", "Mario Party: Star Rush", "Mario Party: The Top 100"]
    axis = factor(len(games))
    win = GraphWin("Games Selection", axis[0]*100, axis[1]*100)
    win.setCoords(-0.5, -0.5, axis[0]-0.5, axis[1]-0.5)
    for x in range(axis[0]):
        line = Line(Point(x+0.5, -0.5), Point(x+0.5, axis[1]-0.5))
        line.draw(win)
    for y in range(axis[1]):
        line = Line(Point(-0.5, y+0.5), Point(axis[0]-0.5, y+0.5))
        line.draw(win)
    for i in range(len(games)):
        text = games[i].split(" ")
        for j in range(len(text)):
            title = Text(Point(i%axis[0], axis[1]-int(i/axis[0])-(j+1)/(len(text)+1)-0.5), text[j])
            title.draw(win)
    choice = win.getMouse()
    x = round(choice.x)
    y = axis[1]-round(choice.y)-1
    print(str(x) + " " + str(y) + " " + games[x+y*axis[0]])

main()