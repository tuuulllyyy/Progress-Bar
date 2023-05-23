import tkinter as tk
from tkinter import ttk
import time

def start_countdown():
    global running
    running = True
    total_time = int(hours_input.get()) * 3600 + int(minutes_input.get()) * 60  # convert to seconds
    for remaining_time in range(total_time, 0, -1):
        if not running:
            break
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_label.config(text=f"Time Remaining: {hours}:{minutes:02d}:{seconds:02d}")
        progress['value'] = (total_time - remaining_time) / total_time * 100
        root.update()
        time.sleep(1)
    if running:
        animate()

def animate():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for color in colors:
        end_label.config(fg=color)
        root.update()
        time.sleep(0.5)

def reset():
    global running
    running = False
    hours_input.delete(0, 'end')
    minutes_input.delete(0, 'end')
    hours_input.insert(0, '0')
    minutes_input.insert(0, '0')
    progress['value'] = 0
    time_label.config(text="")
    end_label.config(fg='black')

root = tk.Tk()
root.title('Time Tracker')
running = False

start_button = tk.Button(root, text="Start", command=start_countdown)
start_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

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

time_label = tk.Label(root, text="")
time_label.pack()

end_label = tk.Label(root, text="Time's up!", fg='black')
end_label.pack()

root.mainloop()
