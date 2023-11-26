import customtkinter
from grid import Grid

class GridGUI(customtkinter.CTk):
    def __init__(self, grid: Grid):
        super().__init__()
        self.grid = grid
        self.state = grid.initial
        self.height = len(grid.initial)
        self.width = len(grid.initial[0])
        self.geometry(f"{self.width*50}x{self.height*50+50}")
        self.createGrid()
        self.createButtons()

    
    def createGrid(self):
        self.frames = []
        for row in range(self.height):
            self.frames.append([])
            for col in range(self.width):
                color = "gray20"
                if self.state[row][col] == 1: color = "cornflowerblue"
                if (col, row) == self.grid.goal: color = "palevioletred"
                

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
        print("Start search Algorithm !!!")