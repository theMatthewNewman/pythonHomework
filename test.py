from pyamaze import maze

m=maze()

m.CreateMaze(loadMaze="./out.csv")
m.run()