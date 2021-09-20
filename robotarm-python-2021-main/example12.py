from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

move = 9

for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for x in range(move):
            robotArm.moveRight()
        robotArm.drop()
        for x in range((move-1)):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    move-=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()