import random
import time

from playsound import playsound
import tkinter as tk
from tkinter import ttk, BOTH, DISABLED, NORMAL
from threading import Timer

class wack_a_mole:
    def __init__(self, root, game_timer):
        self.root = root
        self.root.title("Whack a Mole")
        self.root.resizable(0, 0)
        self.score = 0
        self.game_length = game_timer
        self.count = game_timer
        self.create_buttons()
        self.create_data_frame()
        self.init_game_elements()

    def init_game_elements(self):
        self.timer.config(text=self.count)
        self.score_disp.config(text=self.score)
        self.game_time()
        self.mole_time()

    def one_second(self):
        # print("One second has passed")
        if self.count > 0:
            self.count -=1
            self.timer.config(text=self.count)
            self.game_time()

    def game_time(self):
        self.t = Timer(1 * 1, self.one_second)
        self.t.start()

    def mole_appear(self):
        self.buttons = [self.button1, self.button2, self.button3, self.button4]
        if self.count > 0:
            for button in self.buttons:
                if button.cget('bg') == 'red':
                    self.buttons.pop(self.buttons.index(button))
                button.config(bg='gray')
                button.config(state=NORMAL)
            choose_button = random.choice(self.buttons)
            choose_button.config(bg='red')
            # print(choose_button.cget('bg'))
            self.mole_time()
        else:
            for button in self.buttons:
                button.config(state=DISABLED)

    def get_mole(self, button):
        if self.count > 0:
            if button.cget('bg') == 'red':
                self.score += 1
                playsound('pop.mp3', block=False)
                button.config(state=DISABLED)
            else:
                self.score -=1
            self.score_disp.config(text=self.score)


    def mole_time(self):
        random_time = random.uniform(0.4, 0.8)
        # print(random_time)
        self.t1 = Timer(1 * random_time, self.mole_appear)
        self.t1.start()

    def new_game(self):
        self.t.cancel()
        self.t1.cancel()
        for b in self.buttons:
            b.config(bg='gray')
        self.count = self.game_length
        self.score = 0
        # time.sleep(1)
        self.init_game_elements()

    def create_buttons(self):
        button_frame = tk.LabelFrame(self.root, height=300, width=300, bg='yellow', borderwidth=5)
        button_frame.pack(fill = BOTH, expand = True, padx=5, pady=5)

        # photo = tk.PhotoImage(file="mole.png")
        # photoimage = photo.subsample(3,3)

        button1 = tk.Button(button_frame, bg='gray', compound='left', command= lambda: self.get_mole(button1)) #need to pass lambda here to pass whih button is pressed to get_mole function
        self.button1 = button1
        button1.grid(row=0, column=0, padx=20, pady=20, ipady=40, ipadx=70)

        button2 = tk.Button(button_frame, bg='gray', command= lambda: self.get_mole(button2))
        self.button2 = button2
        button2.grid(row=0, column=1,padx=20, pady=20, ipady=40, ipadx=70)

        button3 = tk.Button(button_frame, bg='gray' , command= lambda: self.get_mole(button3))
        self.button3 = button3
        button3.grid(row=1, column=0, padx=20, pady=20, ipady=40, ipadx=70)

        button4 = tk.Button(button_frame, bg='gray' , command= lambda: self.get_mole(button4))
        self.button4 = button4
        button4.grid(row=1, column=1, padx=20, pady=20, ipady=40, ipadx=70)

    def create_data_frame(self):
        data_frame_bg = tk.LabelFrame(self.root, height=100, width=300, borderwidth=5, bg='cyan')
        data_frame_bg.pack(expand=True, fill= BOTH, padx=5, pady=5)

        data_frame = tk.LabelFrame(data_frame_bg, height=100, width=300, borderwidth=5, bg='cyan')
        data_frame.pack(padx=5, pady=5)

        timer = ttk.Label(data_frame, text=self.count, font=("Courier", 20, "italic"))
        self.timer = timer
        timer.grid(row=0, column=1)
        time_label = ttk.Label(data_frame, text = 'Time:', font=("Courier", 20, "italic"))
        time_label.grid(row=0, column=0)

        styl = ttk.Style()
        styl.configure('TSeparator', background='gray')
        separator = ttk.Separator(data_frame, orient='vertical', style='TSeparator', takefocus= 0)
        separator.grid(row=0, column=2, padx=35, ipadx=2, sticky='ens')

        score_label = ttk.Label(data_frame, text = 'Score:', font=("Courier", 20, "italic"))
        self.score_disp = ttk.Label(data_frame, text=self.score, font=("Courier", 20, "italic"))
        score_label.grid(row=0,column=3, sticky='w')
        self.score_disp.grid(row=0, column=4)

        new_game_button = tk.Button(data_frame, text="New Game",  command=self.new_game ,font=("Courier", 12, "italic"))
        new_game_button.grid(row=1, column=1, columnspan=3, pady=10,ipadx=10, sticky='w')

if __name__ == '__main__':
    root = tk.Tk()
    timer = 20
    wack_a_mole(root, timer)
    root.mainloop()