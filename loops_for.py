robots = ["nomad","Ponginator","Alfred"]
Nomad = {'type':'wheeled','color':'black'}
for robot in robots:
        print(robot)

for name,data in Nomad.items():
        print(name + ': ' + data)

for num,robot in enumerate(robots):
        print(num,robot)
