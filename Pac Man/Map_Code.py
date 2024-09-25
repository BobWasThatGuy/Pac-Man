import math


def Map(Game_Object):


    print("HERE")
    print("HERE")
    print("HERE")
    print("HERE")
    print("HERE")
    print("HERE")
    print("HERE")
    print("HERE")
    print("HERE")

    

    class Map_Class():
        def __init__(self):
            self.Map_Array = [[1,0,0,1], [1,0,1,0], [1,0,0,0], [1,0,0,0], [1,0,1,0], [1,0,1,0], [1,0,1,0], [1,0,0,0], [1,0,1,0], [1,0,1,0], [1,0,0,0], [1,0,1,0], [1,0,1,0], [1,1,0,0],
                              [0,1,0,1], [1,1,0,1], [0,0,1,1], [0,1,0,0], [1,0,0,1], [1,0,1,0], [1,1,0,0], [0,1,0,1], [1,0,0,1], [1,1,0,0], [0,1,0,1], [1,0,1,1], [1,1,0,0], [0,1,0,1],
                              [0,1,0,1], [0,0,0,1], [1,1,1,0], [0,1,0,1], [0,1,0,1], [1,0,0,1], [0,1,1,1], [0,1,0,1], [0,0,0,1], [0,1,0,0], [0,0,1,1], [1,1,0,0], [0,1,0,1], [0,1,0,1],
                              [0,1,0,1], [0,1,0,1], [1,0,1,1], [0,1,0,0], [0,1,0,1], [0,0,1,1], [1,0,1,0], [0,1,1,0], [0,0,0,1], [0,0,1,0], [1,1,1,0], [0,1,0,1], [0,1,1,1], [0,1,0,1],
                              [0,1,0,1], [0,0,1,1], [1,1,1,0], [0,1,0,1], [0,0,1,1], [1,0,0,0], [1,0,1,0], [1,0,1,0], [0,1,1,0], [1,0,0,1], [1,0,1,0], [0,0,1,0], [1,0,1,0], [0,1,0,0],
                              [0,0,0,1], [1,0,1,0], [1,0,1,0], [0,0,1,0], [1,1,0,0], [0,1,1,1], [1,0,0,1], [1,0,1,0], [1,0,1,0], [0,1,0,0], [1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,1],
                              [0,1,0,1], [1,0,1,1], [1,0,1,0], [1,1,0,0], [0,0,0,1], [1,0,1,0], [0,1,0,0], [1,0,0,1], [1,1,0,0], [0,1,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], [0,1,0,1],
                              [0,0,0,1], [0,0,1,0], [1,1,0,0], [0,1,0,1], [0,1,0,1], [1,1,0,1], [0,1,0,1], [0,0,0,0], [0,1,0,0], [0,0,0,1], [1,0,1,0], [1,0,1,0], [1,0,1,0], [0,1,0,0],
                              [0,1,0,1], [1,1,1,0], [0,1,0,1], [0,1,1,1], [0,1,0,1], [0,1,1,1], [0,0,0,1], [0,0,1,1], [0,1,1,0], [0,1,0,1], [1,0,1,1], [1,0,1,0], [1,1,1,0], [0,1,0,1],
                              [0,0,1,1], [1,0,1,0], [0,0,1,0], [1,0,1,0], [0,0,1,0], [1,0,1,0], [0,0,1,0], [1,0,1,0], [0,0,1,0], [0,0,1,0], [1,0,1,0], [1,0,1,0], [1,0,1,0], [0,1,1,0]]
            
            self.Map_Array_Coords = []

            for i in range(0,10):
                for j in range(0,14):
                    self.Map_Array_Coords.append([j * 106 + 73, i * 106 + 73])

            print(self.Map_Array_Coords)


            for i in range(0, len(self.Map_Array)):
                if self.Map_Array[i][0] == 1:
                    self.Vertical_Column = ((i + 1) // 14.00000001) 
                    if i % 14 != 0:
                        self.Horizontal_Row = math.ceil((i) % 14.00000001)
                    else:
                        self.Horizontal_Row = 0
                    Game_Object.game_canvas.create_line(((self.Horizontal_Row) * 106 + 10), (self.Vertical_Column * 106 + 10), ((self.Horizontal_Row + 1) * 106 + 10), ((self.Vertical_Column) * 106 + 10), width = 5, fill = "blue")

                if self.Map_Array[i][1] == 1:
                    self.Vertical_Column = ((i + 1 ) // 14.00000001) 
                    self.Horizontal_Row = math.ceil((i + 1) % 14.00000001)
                    Game_Object.game_canvas.create_line((self.Horizontal_Row * 106 + 10), ((self.Vertical_Column ) * 106 + 10), ((self.Horizontal_Row ) * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), width = 5, fill = "blue")

                if self.Map_Array[i][2] == 1:
                    self.Vertical_Column = ((i + 1) // 14.00000001) 
                    if i % 14 != 0:
                        self.Horizontal_Row = math.ceil((i) % 14.00000001)
                    else:
                        self.Horizontal_Row = 0
                    Game_Object.game_canvas.create_line((self.Horizontal_Row * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), ((self.Horizontal_Row + 1) * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), width = 5, fill = "blue")

                if self.Map_Array[i][3] == 1:
                    self.Vertical_Column = ((i + 1) // 14.00000001) 
                    self.Horizontal_Row = math.ceil((i + 1) % 14.00000001) - 1
                    Game_Object.game_canvas.create_line((self.Horizontal_Row * 106 + 10), ((self.Vertical_Column ) * 106 + 10), ((self.Horizontal_Row ) * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), width = 5, fill = "blue")



            #self.Map_Outline_West = Game_Object.game_canvas.create_line(20, 20, 20, 1060, width = 5, fill = "navy")
            #self.Map_Outline_North = Game_Object.game_canvas.create_line(20, 20, 1483, 20, width = 5, fill = "navy")
            #self.Map_Outline_East = Game_Object.game_canvas.create_line(1483, 20, 1483, 1060, width = 5, fill = "navy")
            #self.Map_Outline_South = Game_Object.game_canvas.create_line(20, 1060, 1483, 1060, width = 5, fill = "navy")

            self.Scoreboard_Outline_North = Game_Object.game_canvas.create_line(1586, 20, 1900, 20, width = 5, fill = "navy")
            self.Scoreboard_Outline_South = Game_Object.game_canvas.create_line(1586, 1060, 1900, 1060, width = 5, fill = "navy")
            self.Scoreboard_Outline_West = Game_Object.game_canvas.create_line(1586, 20, 1586, 1060, width = 5, fill = "navy")
            self.Scoreboard_Outline_East = Game_Object.game_canvas.create_line(1900, 20, 1900, 1060, width = 5, fill = "navy")


            
    Map_Object = Map_Class()

    return Map_Object


    