from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
move = 1

for x in range(7):
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        break
    else:
        for x in range(move):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(move):
            robotArm.moveLeft()
    move+=1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()