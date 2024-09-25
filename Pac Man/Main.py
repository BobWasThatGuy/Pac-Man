
from Game_Code import Game
from tkinter import * 
import tkinter as tk


def main():

    
    def key_handler(event):
        if event.keycode == 27:
            Game_Object.root.destroy()
            exit()     

    def begin():
        Game(Game_Object)   

    def quitter():
        Game_Object.root.destroy()
        exit()

    def settings():
        Game_Object.start_canvas.destroy()
        Game_Object.settings_canvas.pack(fill = "both", expand = True)

    class Game_Class():
        def __init__(self):

            self.root = tk.Tk()
            self.root.title("Pac Man")
            self.root.attributes("-fullscreen", True)
            self.root.minsize(1920, 1080)
            self.root.maxsize(1920, 1080)
            self.root.configure(bg = "white")

            self.game_canvas = Canvas(self.root)
            self.game_canvas.configure(bg = "black", width = 1920, height = 1080, highlightbackground = "black")

            self.settings_canvas = Canvas(self.root)
            self.settings_canvas.configure(bg = "grey", width = 1920, height = 1080)


            self.start_canvas = tk.Canvas(self.root)
            self.start_canvas.configure(bg = "black", width = 1920, height = 1080)
            self.start_canvas.pack(fill = "both", expand = True)

            self.start_frame = Frame(self.start_canvas, width = 1920, height = 1080, bg = "black")
            self.start_frame.pack()

            self.start_button = Button(self.start_frame, anchor = CENTER, text = "START", command = begin )
            self.start_button.place(x = 960, y = 500, height = 80, width = 320, anchor = CENTER)

            self.quit_button = Button(self.start_frame, anchor = CENTER, text = "QUIT", command = quitter)
            self.quit_button.place(x = 960, y = 700, height = 40, width = 240, anchor = CENTER)

            self.settings_button = Button(self.start_frame, anchor = CENTER, text = "SETTINGS", command = settings)
            self.settings_button.place(x = 960, y = 640, height = 40, width = 240, anchor = CENTER)

            self.red_img = tk.PhotoImage(file = "Orange.gif")
            self.red = self.game_canvas.create_image(1760, 940, image = self.red_img, anchor = CENTER)

            self.pac_img = tk.PhotoImage(file = "Pac Man2.gif")
            self.pac_man = self.game_canvas.create_image(73, 603, image = self.pac_img, anchor = CENTER)    

            self.root.bind("<Key>", key_handler)

            self.change_x = 0
            self.change_y = 0
            self.direction = 1
            self.stretch = 0
            self.axis = 0
            self.side = 0

    
    Game_Object = Game_Class()



    Game_Object.root.mainloop()


main()