import tkinter as tk
from tkinter import ttk
import time

def start_countdown():
    global running
    # start running the countdown
    running = True
    total_time = int(hours_input.get()) * 3600 + int(minutes_input.get()) * 60  # convert to seconds
    for remaining_time in range(total_time, 0, -1):
        if not running:
            # if reset is clicked, stop running the countdown
            break
        percent_complete = (total_time - remaining_time) / total_time * 100
        percent_complete_label.config(text=f"Complete: {percent_complete:.1f}%")
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_label.config(text=f"Time Remaining: {hours}:{minutes:02d}:{seconds:02d}")
        progress['value'] = percent_complete
        root.update()
        time.sleep(1)
    if running:
        end_label.pack()  # show the "Time's up!" label
        animate()

def animate():
    # change the color of the "Time's up!" label in a loop
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for color in colors:
        end_label.config(fg=color)
        root.update()
        time.sleep(0.5)

def reset():
    global running
    running = False  # stop running the countdown
    hours_input.delete(0, 'end')
    minutes_input.delete(0, 'end')
    hours_input.insert(0, '0')
    minutes_input.insert(0, '0')
    progress['value'] = 0
    percent_complete_label.config(text="")
    time_label.config(text="")
    end_label.pack_forget()  # hide the "Time's up!" label
    end_label.config(fg='black')

root = tk.Tk()
root.title('Time Tracker')
running = False  # initial state for the countdown

start_button = tk.Button(root, text="Start", command=start_countdown)
start_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

# input fields for hours and minutes
hours_input = tk.Entry(root)
hours_input.insert(0, '0')
hours_input.pack()
hours_label = tk.Label(root, text="Hours")
hours_label.pack()

minutes_input = tk.Entry(root)
minutes_input.insert(0, '0')
minutes_input.pack()
minutes_label = tk.Label(root, text="Minutes")
minutes_label.pack()

progress = ttk.Progressbar(root, length=100)
progress.pack()

# labels for percent complete and time remaining
percent_complete_label = tk.Label(root, text="")
percent_complete_label.pack()

time_label = tk.Label(root, text="")
time_label.pack()

# "Time's up!" label, hidden at start
end_label = tk.Label(root, text="Time's up!", fg='black')

root.mainloop()
