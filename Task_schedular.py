import tkinter as tk
from tkinter import ttk, messagebox
import time
from threading import Thread
import pygame

# Initialize Pygame for sound
pygame.mixer.init()

# Function to play sound
def play_sound():
    pygame.mixer.music.load("chime.mp3")
    pygame.mixer.music.play()

# Function to check time and trigger sound
def check_reminder():
    while True:
        current_time = time.strftime("%H:%M")
        current_day = time.strftime("%A")
        for task in tasks:
            if task['day'] == current_day and task['time'] == current_time:
                play_sound()
                messagebox.showinfo("Reminder", f"Time to {task['activity']}!")
                tasks.remove(task)
                update_task_list()
        time.sleep(10)

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, f"{task['day']} at {task['time']} - {task['activity']}")

# Function to add a scheduled task
def add_task():
    selected_day = day_var.get()
    selected_hour = hour_var.get()
    selected_minute = minute_var.get()
    selected_activity = activity_var.get()

    if not selected_day or not selected_hour or not selected_minute or not selected_activity:
        messagebox.showwarning("Input Error", "Please select a day, time, and activity.")
        return

    selected_time = f"{selected_hour}:{selected_minute}"
    task = {
        'day': selected_day,
        'time': selected_time,
        'activity': selected_activity
    }
    tasks.append(task)
    update_task_list()

# Create the main window
root = tk.Tk()
root.title("Reminder App")
root.geometry("400x300")

# Task storage
tasks = []

# UI Elements
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Day Dropdown
ttk.Label(frame, text="Day:").grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
day_var = tk.StringVar()
day_dropdown = ttk.Combobox(frame, textvariable=day_var)
day_dropdown['values'] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_dropdown.grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

# Time Selection using Spinbox
ttk.Label(frame, text="Hour:").grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
hour_var = tk.StringVar(value="00")
hour_spinbox = ttk.Spinbox(frame, from_=0, to=23, textvariable=hour_var, width=5, format="%02.0f")
hour_spinbox.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)

ttk.Label(frame, text="Minute:").grid(column=2, row=1, padx=5, pady=5, sticky=tk.W)
minute_var = tk.StringVar(value="00")
minute_spinbox = ttk.Spinbox(frame, from_=0, to=59, textvariable=minute_var, width=5, format="%02.0f")
minute_spinbox.grid(column=3, row=1, padx=5, pady=5, sticky=tk.W)

# Activity Dropdown
ttk.Label(frame, text="Activity:").grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
activity_var = tk.StringVar()
activity_dropdown = ttk.Combobox(frame, textvariable=activity_var)
activity_dropdown['values'] = ("Wake up", "Go to gym", "Breakfast", "Meetings", "Lunch", "Quick nap", "Go to library", "Dinner", "Go to sleep")
activity_dropdown.grid(column=1, row=2, padx=5, pady=5, sticky=tk.EW)

# Add Task Button
add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.grid(column=1, row=3, padx=5, pady=10, sticky=tk.EW)

# Task Listbox
ttk.Label(frame, text="Scheduled Tasks:").grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)
task_listbox = tk.Listbox(frame, height=8)
task_listbox.grid(column=0, row=5, columnspan=4, padx=5, pady=5, sticky=tk.EW)

# Start checking for reminders
reminder_thread = Thread(target=check_reminder)
reminder_thread.daemon = True
reminder_thread.start()

# Make the window responsive
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
frame.columnconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
