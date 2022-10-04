from pyamaze import maze

m=maze()
file = input("maze file: ")
m.CreateMaze(loadMaze=file)
m.run()