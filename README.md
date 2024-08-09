# Reminder App

A simple reminder application built with Python using `tkinter` for the user interface and `pygame` for playing sound alerts. This app allows users to set daily reminders with specific times and activities.

## Features

- **Day Selection**: Choose the day of the week for the reminder.
- **Time Selection**: Pick the time using `Spinbox` widgets for hours and minutes.
- **Activity Selection**: Select from a predefined list of daily activities.
- **Sound Alert**: Plays a chime when a reminder is triggered.
- **Task List**: Displays scheduled tasks in a list.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/reminder-app.git
   cd reminder-app
   ```

## Install Dependencies:

Ensure you have Python 3 installed. Install the required packages using pip:

```bash
pip install pygame
pip install tkcalendar
```

__Note__: tkcalendar is used for a clock widget; if it's not available, modify the time selection as described.

## Add Sound File:

Place a sound file named chime.mp3 in the root directory of the project. This file will be played for reminders.

## Usage

__Run the Application:__

Execute the Python script to start the reminder application:

```bash
python reminder_app.py
```

__Add Reminders:__

- Select the day of the week from the dropdown.
- Choose the time using the hour and minute spin boxes.
- Select the activity from the dropdown.
- Click "Add Task" to schedule the reminder.

__View Scheduled Tasks:__

- The list of scheduled tasks will be displayed in the listbox.
- Tasks will be checked every 10 seconds. When a scheduled time is reached, a sound will play, and a reminder message will be shown.

__Code Details__
**reminder_app.py:** 
- Main script for the reminder application.
- Uses tkinter for GUI.
- Uses pygame for sound playback.
- Implements a threading mechanism to continuously check for reminders.
