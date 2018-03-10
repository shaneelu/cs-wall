from Parser import Parser


class systemControl():

    SOUTH = 0
    EAST = 1
    NORTH = 2
    WEST = 3

    def __init__(self):
        global direction, robotX, robotY, GoalX, GoalY, dimX, dimY
        direction = 1
        robotX = 3
        robotY = 1
        GoalX = 3
        GoalY = 4
        dimX = 5
        dimY = 5

    # returns one line of the SCRIPT string and a boolean representing whether the target goal is reached
    def moveRobot(self, code):
        goal_reached = False
        global direction, robotX, robotY, GoalX, GoalY
        out = False
        if code == "Forward":
            if direction == self.SOUTH:
                robotX += 1
            elif direction == self.EAST:
                robotY += 1;
            elif direction == self.NORTH:
                robotX -= 1;
            elif direction == self.WEST:
                robotY -= 1
            if self.checkBounds():
                out = True
                goal_reached = False
                return goal_reached, out
            # TODO method moveForward
        if code == "Backward":
            if direction == self.SOUTH:
                robotX -= 1
            elif direction == self.EAST:
                robotY -= 1;
            elif direction == self.NORTH:
                robotX += 1;
            elif direction == self.WEST:
                robotY += 1
            if self.checkBounds():
                out = True
                goal_reached = False
                return goal_reached, out
            # TODO method moveBackward
        if code == "TurnLeft":
            direction = (direction + 1) % 4
            # TODO method turnLeft
        if code == "TurnRight":
            direction = (direction + 3) % 4
            # TODO method turnRight
        if robotX == GoalX and robotY == GoalY:
            goal_reached = True
        return goal_reached, out

    # checks whether the current position of the robot is out of bounds in the map/maze
    # if the robot is out of bounds, then it resets the position of the robot at its last position in bound
    # returns True if the robot is out of bounds, and False if it is not.
    def checkBounds(self):
        out_of_bounds = False
        global robotX, robotY, dimX, dimY, direction
        if robotX >= dimX:
            out_of_bounds = True
            robotX = dimX - 1
        elif robotX < 0:
            out_of_bounds = True
            robotX = 0
        if robotY >= dimY:
            out_of_bounds = True
            robotY = dimY - 1
        elif robotY < 0:
            out_of_bounds = True
            robotY = 0
        return out_of_bounds

    # runs the actions on the 2D system
    def run(self, code):
        global robotX, robotY
        action_list = code.split("\n")
        length = len(action_list)
        goal = False
        for i in range(0, length):
            code = action_list[i]
            goal, out = self.moveRobot(code)
            if out:
                print "OUT OF BOUNDS"
                return False
        return goal


p = Parser()
codeblock = p.runCode(p.translateRFID("rfidFOR.txt"))
sc = systemControl()
if sc.run(codeblock):
    print "GOAL REACHED!!! CONGRATS!!!"