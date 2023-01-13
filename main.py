import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#C0EEE4"
YELLOW = "#F8F988"
PINK_LIGHT = "#FFCAC8"
DEEP_PINK = "#FF9E9E"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
TICK = "✔"
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 1
    check_mark.config(text="")
    header_text.config(text="Timer", fg=BLUE)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    print(reps)
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 2 != 0:
        header_text.config(text="Work", fg=DEEP_PINK)
        count_down(work_sec)
    elif reps == 8:
        header_text.config(text="Long Break", fg=BLUE)
        count_down(long_break_sec)
    else:
        header_text.config(text="Short Break", fg=PINK_LIGHT)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global reps, timer
    count_minute = math.floor((count/60))
    count_seconds = round(count % 60)
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        if reps % 2 == 0:
            marks = ""
            for i in range(0, int(reps/2)):
                marks += TICK
            check_mark.config(text=marks)
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Header
header_text = Label(text="Timer", font=(FONT_NAME, 28, 'bold'), bg=YELLOW, fg=BLUE)
header_text.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=280, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", font=(FONT_NAME, 14, 'normal'), command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 14, 'normal'), command=reset_timer)
reset_button.grid(column=2, row=2)

# Check mark label
check_mark = Label(font=(FONT_NAME, 12, 'bold'), bg=YELLOW, fg=DEEP_PINK)
check_mark.grid(column=1, row=3)

window.mainloop()