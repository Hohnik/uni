import customtkinter
from grid import Grid

class GridGUI(customtkinter.CTk):
    def __init__(self, grid: Grid, search_algorithm: callable):
        super().__init__()
        self.puzzle = grid
        self.state = grid.initial
        self.solution = None
        self.search_algorithm = search_algorithm

        self.height = len(grid.initial)
        self.width = len(grid.initial[0])
        self.geometry(f"{self.width*50}x{self.height*50+50}")

        self.frames = []
        self.createGrid()
        self.createButtons()


    
    def createGrid(self):
        for row in range(self.height):
            self.frames.append([])

            for col in range(self.width):
                color = "gray20"
                if self.state[row][col] == 1: color = "cornflowerblue"
                if (col, row) == self.puzzle.goal: color = "palevioletred"
                

                self.grid_columnconfigure(col, weight=1)
                self.grid_rowconfigure(col, weight=1)
                self.frames[row].append(customtkinter.CTkFrame(self, width=50, height=50, fg_color=color))
                self.frames[row][col].grid(column=col, row=row, padx=1, pady=1)


    def createButtons(self):
        self.wallsButton = customtkinter.CTkButton(self, text="Generate Walls", command=self.generateWalls)
        self.wallsButton.grid(row=self.height, column=0, pady=10, padx=10, columnspan=self.width//2)
        self.startButton = customtkinter.CTkButton(self, text="Start", command=self.startSearch)
        self.startButton.grid(row=self.height, column=self.width//2, pady=10, padx=10, columnspan=self.width//2)

    def generateWalls(self):
            print("Generate Walls !!!")
    
    def startSearch(self):
        self.solve()

    def move(self, action):
         x, y = self.find_player(self.state)
         color = "palegreen"
         match action:
            case "TOP":
                self.frames[y-1][x].fg_color = color

            case "RIGHT":
                self.frames[y][x+1].fg_color = color
                
            case "DOWN":
                self.frames[y+1][x].fg_color = color
                
            case "LEFT":
                self.frames[y][x-1].fg_color = color
                


    def solve(self):
        self.solution = self.search_algorithm(self.puzzle).solution()
        for action in self.solution:
            self.state = self.move(action)

    @staticmethod
    def find_player(state:list[list]):
        full_grid = []
        for row in state: 
            full_grid += row

        player_index = full_grid.index(1)
        x = player_index % len(state[0])
        y = player_index // len(state[0])

        return x,y