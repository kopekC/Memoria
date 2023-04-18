This is a Python project that corrupts and plays back videos on a loop using the VLC media player. The corrupt_video function takes an input video file, applies a noise filter, and saves the output to a new file with the same name. The original file is then deleted, and the new file is renamed to the original filename.

The play_video function takes a screen number and a video file and uses the VLC media player to play the video in full screen mode on the specified screen. The process_videos function corrupts all the video files in the project directory, and the start_videos function starts playing all the corrupted videos on their respective screens.

The main program starts playing the videos immediately upon execution and schedules a task to corrupt and restart the videos every day at 2:00 AM. The program runs until the end_time variable is reached, which is set to 30 days from the current time.

## Requirements

Python 3
VLC media player

## Usage
Clone the repository or download the project files.
Make sure you have Python 3 installed on your system.
Install the VLC media player on your system.
Open a terminal or command prompt and navigate to the project directory.
Run the command python3 main.py to start the program.
The program will start playing the videos immediately and will schedule a task to corrupt and restart the videos every day at 2:00 AM.
The program will run until the end_time variable is reached, which is set to 30 days from the current time.
Note: You can modify the corrupt_video function to change the level of noise corruption applied to the videos. You can also modify the start_videos function to change the number of screens used to play the videos.