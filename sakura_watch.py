import tkinter
from tkinter import ttk
import time
import platform
import os

window = tkinter.Tk()
window_width = 400
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_pos_x = int(screen_width/3 - window_width/2)
window_pos_y = int(screen_height/3 - window_height/2)
new_geo = f"{window_width}x{window_height}+{window_pos_x}+{window_pos_y}"
window.geometry(new_geo)
window.resizable(False, False)
window.config(bg='white')

frame = tkinter.Frame(window, width=window_width, height=window_height, 
                      relief="flat", background="white")
frame.place(x=0, y=0)

def update_label_watch():
    label_watch.config(text=time.strftime("%H:%M:%S", 
                        time.localtime(time.time())))
    label_watch.after(500, update_label_watch)

label_watch = tkinter.Label(frame, background='white', foreground='black', 
                        font=('comfortaa', 40, 'bold'))
label_watch.place(x=44, y=12)
update_label_watch()

class StopWatch():
    def __init__(self, label_stopwatch):
        self.label_stopwatch = label_stopwatch
        self.init_stopwatch()
        self.go_stopwatch()
        
    def init_stopwatch(self):
        self.time_start = 0.0
        self.time_elapse = 0.0
        self.time_stop_start = 0.0
        self.time_stop_elapse = 0.0
        self.time_stop_elapse_acc = 0.0
        self.time_hours = 0
        self.time_mins = 0
        self.time_secs = 0
        self.time_0_01_secs = 0
        self.time_str = f"{self.time_hours:02}:{self.time_mins:02}:"
        self.time_str += f"{self.time_secs:02} {self.time_0_01_secs:02}"
        self.check_first_time = True
        self.check_stopped = True
        self.label_stopwatch.config(text=self.time_str)
        
        self.to_stop = 0

        self.src_path = os.path.abspath(__file__)
        self.src_dir = os.path.dirname(self.src_path)
        self.img_path = os.path.join(self.src_dir, "sewoo_1.png")
        self.img_sewoo_1 = tkinter.PhotoImage(file=self.img_path)
        self.img_sewoo_1 = self.img_sewoo_1.zoom(2)
        self.img_path = os.path.join(self.src_dir, "sewoo_2.png")
        self.img_sewoo_2 = tkinter.PhotoImage(file=self.img_path)
        self.img_sewoo_2 = self.img_sewoo_2.zoom(2)
        self.label_sewoo = tkinter.Label(frame, image=self.img_sewoo_1, bg="white")
        self.label_sewoo.place(x=264, y=11)
        
    def click_btn_go(self):
        if self.check_stopped==True:
            self.time_stop_elapse_acc += self.time_stop_elapse
        self.check_stopped = False
        if self.check_first_time:
            self.time_start = time.time()
            self.check_first_time = False
        
    def click_btn_stop(self):
        if self.check_stopped==False:
            self.time_stop_start = time.time()
        self.check_stopped = True
    
    def go_stopwatch(self):
        self.time_elapse = time.time() - self.time_start
        if not self.check_stopped:
            self.time_elapse -= self.time_stop_elapse_acc
            self.time_hours = int(self.time_elapse // 3600)
            self.time_mins  = int((self.time_elapse 
                                - (self.time_hours * 3600)) // 60)
            self.time_secs = int(self.time_elapse 
                                - (self.time_hours * 3600) 
                                - (self.time_mins * 60))
            self.time_0_01_secs = int((self.time_elapse
                                - (self.time_hours * 3600) 
                                - (self.time_mins * 60)
                                - self.time_secs) * 100)
            if self.time_hours >= 100:
                self.time_hours = self.time_hours % 100
            self.time_str = f"{self.time_hours:02}:{self.time_mins:02}:"
            self.time_str += f"{self.time_secs:02}"
            self.time_str += f" {self.time_0_01_secs:02}"
            self.label_stopwatch.config(text=self.time_str)
            if int(self.time_elapse)%2==1:
                self.label_sewoo.config(image=self.img_sewoo_1)
            else:
                self.label_sewoo.config(image=self.img_sewoo_2)
        else:
            if self.time_stop_start:
                self.time_stop_elapse = time.time() - self.time_stop_start
        self.label_stopwatch.after(1, self.go_stopwatch)

    def reset_stopwatch(self):
        self.init_stopwatch()

label_stopwatch = tkinter.Label(frame, 
                                background = 'white', foreground='black',
                                font=('comfortaa', 40, 'bold'))
label_stopwatch.place(x=44, y=81)

stopwatch_obj = StopWatch(label_stopwatch)

what_platform=platform.system()
if what_platform=="Darwin":
    btn_go = tkinter.Button(frame, text="Go", 
                            borderwidth=0, background="white", relief="solid",
                            command=stopwatch_obj.click_btn_go)
    btn_go.place(x=50, y=160, width=148, height=50, bordermode="inside")

    btn_stop = tkinter.Button(frame, text="Stop",
                              borderwidth=0, background="white", relief="solid",
                              command=stopwatch_obj.click_btn_stop)
    btn_stop.place(x=202, y=160, width=148, height=50, bordermode="inside")

    btn_reset = tkinter.Button(frame, text="Reset", 
                               borderwidth=0, background="white", relief="solid",
                               command=stopwatch_obj.reset_stopwatch)
    btn_reset.place(x=50, y=220, width=300, height=50)
elif what_platform=="Windows":
    btn_go = ttk.Button(frame, text="Go",
                            command=stopwatch_obj.click_btn_go)
    btn_go.place(x=50, y=160, width=150, height=50, bordermode="inside")

    btn_stop = ttk.Button(frame, text="Stop",
                            command=stopwatch_obj.click_btn_stop)
    btn_stop.place(x=200, y=160, width=150, height=50, bordermode="inside")

    btn_reset = ttk.Button(frame, text="Reset", 
                            command=stopwatch_obj.reset_stopwatch)
    btn_reset.place(x=50, y=220, width=300, height=50)
    
    src_path = os.path.abspath(__file__)
    src_dir = os.path.dirname(src_path)
    img_path = os.path.join(src_dir, "sewoo.png")
    window.iconphoto(False, tkinter.PhotoImage(file=img_path))
else:
    btn_go = ttk.Button(frame, text="Go",
                            command=stopwatch_obj.click_btn_go)
    btn_go.place(x=50, y=160, width=150, height=50, bordermode="inside")

    btn_stop = ttk.Button(frame, text="Stop",
                            command=stopwatch_obj.click_btn_stop)
    btn_stop.place(x=200, y=160, width=150, height=50, bordermode="inside")

    btn_reset = ttk.Button(frame, text="Reset", 
                            command=stopwatch_obj.reset_stopwatch)
    btn_reset.place(x=50, y=220, width=300, height=50)

window.title('SAKURA Watch')
window.mainloop()

# For Windows
# pyinstaller --onefile --noconsole --icon sewoo.ico 
# --add-data="./sewoo.png;." --add-data="./sewoo_1.png;." --add-data="./sewoo_2.png;." 
# .\sakura_watch.py

# For Mac
# pyinstaller --onefile --noconsole
# --add-data="./sewoo_1.png;." --add-data="./sewoo_2.png;."
# ./sakura_watch.py

# For Linux
# pyinstaller --onefile --noconsole
# --add-data="./sewoo_1.png;." --add-data="./sewoo_2.png;."
# ./sakura_watch.py