robots = ["Nomad","Ponginator","Alfred"]
for robot in robots:

        if robot=="Nomad":
                print("This is Nomad")
        else:
                print(robot + " is not Nomad")


myRobot = "Nomad"
if myRobot == "Ponginator":
    print(" false ")
else:
    print("true")

for robot in robots:
        if robot == "Ponginator" or robot == "Alfred":
            print("These aren\'t the droids I\'m looking for.")
