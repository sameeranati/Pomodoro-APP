import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer_text="00:00"
    canvas.itemconfig(timer_text="00:00")
    timer_label.config(text="timer")
    tick_label.config(text="")
    global reps
    reps=0

    # timer_label="timer"
    #reset checkmarks
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60;    
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    # if it's 1st/3rd/5th/7th rep
    
    if reps%8==0:
        timer_label.config(text="LONG BREAK",fg=RED)
        count_down(long_break_sec)
    elif reps%2==0:
        timer_label.config(text="SHORT BREAK",fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="WORK",fg=GREEN)
        count_down(work_sec)
        # tick_label.config(text=tick)
        # tick_label.grid(column=1,row=3)

    # tick_label.grid(column=1,row=3)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<0:
        count_sec=f"0{count_sec}"
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    elif count_sec<=9:
        canvas.itemconfig(timer_text,text=f"{count_min}:0{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    else:
        starttimer()
        mark=" "
        for _ in math.floor(reps/2):
            mark+=tick
        tick_label.config(text=mark)
        tick_label.grid(column=1,row=3)
# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro")

window.config(padx=100,pady=50,bg=YELLOW)

#canvas
canvas=tkinter.Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
t_img=tkinter.PhotoImage(file="/home/sameeranati/pomodoro/tomato.png")
canvas.create_image(100,112,image=t_img)
timer_text=canvas.create_text(103,140,text="00:00",fill="White",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
count_down(WORK_MIN*60)

#timer label
timer_label=tkinter.Label(text="WORK",fg=GREEN,bg=YELLOW,font=("ariel",35,"bold"))
timer_label.grid(column=1,row=0)

#start button


start_button=tkinter.Button(text="START",highlightthickness=0,command=starttimer)
start_button.grid(column=0,row=2)

#reset button
def resetbutton():
    pass
reset_button=tkinter.Button(text="RESET",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

#tick mark label
tick='🗸'
tick_label=tkinter.Label(fg=GREEN,bg=YELLOW,font=("courier",12,"bold"))
# tick_label.grid(column=1,row=3)
window.mainloop()