from Map_Code import *
import time
import keyboard
from tkinter import *
import tkinter as tk
import random
import math
from Player_Movement import *

def Game(Game_Object):

        #1760 940
        # 4 5 6
        # 3 2 1

        last_coords = 1 
        e = [0, 0]

        a = [[[0, -4, 6], [-4, 0, 2], 1],
              [[4, 0, 1], [0, -4, 5], [-4, 0, 3], 2],
              [[0, -4, 4], [4, 0, 2], 3],
              [[4, 0, 5], [0, 4, 3], 4],
              [[4, 0, 6], [0, 4, 2], [-4, 0, 4], 5],
              [[0, 4, 1], [-4, 0, 5], 6]]
        
        b = [[1760, 940], [960, 940], [160, 940], [160, 140], [960, 140], [1760, 140]]


        

        Game_Object.start_canvas.destroy()
        Game_Object.game_canvas.pack(fill = "both", expand = True)
        Map_Object = Map(Game_Object)

        Game_Object.root.update()

        tick = -2

        temp1 = time.time()



        while True:

            Game_Object.root.update()
            
            temp2 = time.time()
            if temp2 - temp1 > 0.02:
                print(Game_Object.game_canvas.coords(Game_Object.pac_man))
                print(tick)
                Game_Object.root.update()
                tick = tick + 1

                temp1 = time.time()

                
                Movement_Player(Game_Object, Map_Object)

                print(3)
                

                if tick % 200 == 0:
                    coords = Game_Object.game_canvas.coords(Game_Object.red)
                    no_list = b.index(coords)
                    length = len(a[no_list])
                    d = random.randint(0, length - 2)
                    while True:
                        print(no_list, d, length)
                        if a[no_list][d][2] == last_coords:
                            d = random.randint(0, length - 2)
                            
                        else:
                            
                            e = a[no_list][d]
                            break
                    
                    last_coords = no_list + 1

                Game_Object.game_canvas.move(Game_Object.red , e[0], e[1])


                Game_Object.root.update()

                

                
                         
                     


                total_diff = 0

                for i in range(0,2):

                    p = Game_Object.game_canvas.coords(Game_Object.pac_man)
                    q = Game_Object.game_canvas.coords(Game_Object.red)
                    diff = p[i] - q[i]
                    diff = diff * diff
                    diff = math.sqrt(diff)
                    total_diff += diff
                
                if total_diff <= 170:
                        Game_Object.game_canvas.destroy()
                        Game_Object.start_canvas.pack(fill = "both", expand = True)

                #if tick % 2 == 0:
                     #Game_Object.pac_img = tk.PhotoImage(file = "pac man2.gif")
                     #temp_coords = Game_Object.game_canvas.coords(Game_Object.pac_man)
                     #Game_Object.pac_man.delete()
                     #Game_Object.pac_man = Game_Object.game_canvas.create_image(temp_coords[0], temp_coords[1], image = Game_Object.pac_img)
                #elif tick % 2 == 1:
                     #Game_Object.pac_img = tk.PhotoImage(file = "pac man.gif")
                     #temp_coords = Game_Object.game_canvas.coords(Game_Object.pac_man)
                     #Game_Object.pac_man.delete()
                     #Game_Object.pac_man = Game_Object.game_canvas.create_image(temp_coords[0], temp_coords[1], image = Game_Object.pac_img)

            else:
                 Time_Diff = temp2 - temp1
                 time.sleep(Time_Diff)