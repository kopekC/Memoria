# Memoria - A Project About the Fragility of Memories

## Introduction

Memoria is a Python project that explores the fragile nature of memories and how they can be easily overwritten and lost over time. The project is inspired by the idea that memories are not fixed, but rather are constantly changing and fading away.

## Objective

The objective of the project is to express this concept through a visual and auditory experience. The project consists of a set of videos that are corrupted with a noise filter, making them difficult to see and hear clearly. These videos are played on a loop using the VLC media player, creating a surreal and dream-like atmosphere.

As the videos are corrupted and played repeatedly, they begin to lose their original form and content, mirroring the way memories can be overwritten and distorted over time. The project invites the viewer to contemplate the ephemeral nature of memories and the fleeting nature of human experience.

## Implementation

The Memoria project is implemented using Python and the VLC media player. The main components of the project include:

### `corrupt_video(input_file, output_file_template, initial_crf=30, noise_intensity=2)`

This function takes an input video file and applies a noise filter to it using FFmpeg. The corrupted video is saved as a temporary file with a new name specified by the output_file_template parameter. The original input file is then deleted, and the temporary file is renamed to the original file name.

### `play_video(screen_number, video_file)`
This function plays a given video file on the VLC media player, using the specified screen number. The video is played in fullscreen mode, and the player is configured to loop the video and hide the video title. The function returns a subprocess.Popen object representing the running VLC process.

### `process_videos()`
This function applies the corrupt_video() function to a set of input video files, creating a set of corrupted video files that will be played by the play_video() function.

### `start_videos(video_files)`
This function starts a set of VLC media player instances, each playing one of the given video files using a unique screen number. The function returns a list of subprocess.Popen objects representing the running VLC processes.

### `stop_videos(vlc_processes)`
This function stops a set of running VLC media player instances by killing their corresponding subprocess.Popen objects.

The main script for the project is memoria.py, which sets up the schedule for periodically corrupting and restarting the videos. The schedule is created using the schedule module, and the scheduled_task() function is called at a set time each day to stop the current videos, process new corrupted videos, and start playing them.

## Usage
To use the Memoria project, you'll need to have Python and the VLC media player installed on your system. Clone the project repository, navigate to the project directory, and run the following command:

```
python3 final.py
```
## Special thanks to:

[g1smo](https://github.com/g1smo) for all the help with the audio, thanks m8 !