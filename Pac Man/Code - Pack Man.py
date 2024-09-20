
from tkinter import * 
import tkinter as tk
import time
import random






def main():

    
    def key_handler(event):
        if event.keycode == 27:
            root.destroy()
            exit()        


    def begin():

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


        

        start_canvas.destroy()
        game_canvas.pack(fill = "both", expand = True)

        root.update()

        tick = -2

        temp1 = time.time()



        while True:

            root.update()
            
            temp2 = time.time()
            if temp2 - temp1 > 0.02:
                print(game_canvas.coords(red))
                print(tick)
                root.update()
                tick = tick + 1

                temp1 = time.time()

                
                

                print(3)
                

                if tick % 200 == 0:
                    coords = game_canvas.coords(red)
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

                game_canvas.move(red , e[0], e[1])


                root.update()



                



    def quitter():
        root.destroy()
        exit()

    def settings():
        start_canvas.destroy()
        settings_canvas.pack(fill = "both", expand = True)


    root = tk.Tk()
    root.title("Pac Man")
    root.attributes("-fullscreen", True)
    root.minsize(1920, 1080)
    root.maxsize(1920, 1080)
    root.configure(bg = "white")

    game_canvas = Canvas(root)
    game_canvas.configure(bg = "black", width = 1920, height = 1080, highlightbackground = "black")

    settings_canvas = Canvas(root)
    settings_canvas.configure(bg = "grey", width = 1920, height = 1080)


    start_canvas = tk.Canvas(root)
    start_canvas.configure(bg = "black", width = 1920, height = 1080)
    start_canvas.pack(fill = "both", expand = True)

    start_frame = Frame(start_canvas, width = 1920, height = 1080, bg = "black")
    start_frame.pack()

    start_button = Button(start_frame, anchor = CENTER, text = "START", command = begin )
    start_button.place(x = 960, y = 500, height = 80, width = 320, anchor = CENTER)

    quit_button = Button(start_frame, anchor = CENTER, text = "QUIT", command = quitter)
    quit_button.place(x = 960, y = 700, height = 40, width = 240, anchor = CENTER)

    settings_button = Button(start_frame, anchor = CENTER, text = "SETTINGS", command = settings)
    settings_button.place(x = 960, y = 640, height = 40, width = 240, anchor = CENTER)

    red_img = tk.PhotoImage(file = "Red.gif")
    red = game_canvas.create_image(1760, 940, image = red_img, anchor = CENTER)

    pac_img = tk.PhotoImage(file = "Pac Man.gif")
    pac_man = game_canvas.create_image(160, 540, image = pac_img)    

    root.bind("<Key>", key_handler)




    root.mainloop()


main()