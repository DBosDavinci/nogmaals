from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

for x in range(5):
    robotArm.grab()
    for x in range(9-2*x):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(9-2*x):
        robotArm.moveLeft()
    robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()