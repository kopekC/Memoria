#!/usr/bin/env python3
import subprocess
import time
import datetime
import schedule
import threading
import os


def corrupt_video(input_file, output_file_template, initial_crf=30, noise_intensity=2):
    """
    This function takes an input video file, applies a corruption effect using ffmpeg
    and replaces the input file with the corrupted version. 

    Parameters:
    input_file: Path to the video file to corrupt.
    output_file_template: Template for the output file path.
    initial_crf: Initial CRF value, default 30.
    noise_intensity: Intensity of the noise to add, default 2. 

    Returns:
    Path to the corrupted video file.
    """
    crf_value = initial_crf
    current_noise_intensity = noise_intensity

    output_file = output_file_template
    ffmpeg_command = [
        "ffmpeg", "-y", "-i", input_file,
        "-vf", f"noise=c0s={current_noise_intensity}:allf=t+u,setpts=PTS",
        "-c:v", "libx264", "-b:v", "1000k", "-g", "60",
        "-crf", str(crf_value), "-preset", "veryfast",
        "-c:a", "copy", output_file
    ]
    subprocess.run(ffmpeg_command, check=True)

    # Delete the original file
    os.remove(input_file)

    # Rename the temporary file to the original filename
    os.rename(output_file, input_file)

    return input_file


def play_video(screen_number, video_file):
    """
    This function plays the video in fullscreen mode on a specific screen.

    Parameters:
    screen_number: Number of the screen where the video should be played.
    video_file: Path to the video file to play.

    Returns:
    Process of the VLC player playing the video.
    """
    vlc_command = [
        "vlc", "--fullscreen",
        f"--qt-fullscreen-screennumber={screen_number}",
        "--loop", "--no-video-title-show", video_file,
        "--no-jack-auto-connect",
        f"--jack-name={screen_number}"
    ]

    vlc_process = subprocess.Popen(vlc_command)
    return vlc_process


def process_videos():
    """
    This function applies the `corrupt_video` function to multiple video files.
    Returns:
    List of paths to the corrupted video files.
    """

    video_files = [f"screen-{i}.mp4" for i in range(1, 5)]

    for i, video_file in enumerate(video_files):
        # Use the same filename for input and output
        output_file = corrupt_video(video_file, f"temp_{video_file}")
        video_files[i] = output_file

    return video_files


def start_videos(video_files):
    """
    This function launches the `play_video` function on multiple video files.

    Parameters:
    video_files: List of paths to the video files to play.

    Returns:
    List of processes of the VLC player playing the videos.
    """
    vlc_processes = []

    for i, video_file in enumerate(video_files):
        vlc_process = play_video(i, video_file)
        vlc_processes.append(vlc_process)

    return vlc_processes


def stop_videos(vlc_processes):
    """
    This function stops playing of multiple video files.

    Parameters:
    vlc_processes: List of processes of the VLC player playing the videos.
    """
    

    for vlc_process in vlc_processes:
        vlc_process.kill()


end_time = datetime.datetime.now() + datetime.timedelta(days=30)
"""
end_time: datetime. This indicates when the schedule should stop. In this case, it is set to 30 days from now.
"""

# Play the videos immediately
video_files = [f"screen-{i}.mp4" for i in range(1, 5)]
vlc_processes = start_videos(video_files)

# Schedule the corruption process


def scheduled_task():
    """
    This task is scheduled to run every day at 11:30. It stops the videos, corrupts them and restarts them.
    """


    global vlc_processes
    global video_files

    stop_videos(vlc_processes)
    video_files = process_videos()
    vlc_processes = start_videos(video_files)


schedule.every().day.at("11:30").do(scheduled_task)

while datetime.datetime.now() < end_time:
    """
    This while loop runs until the current datetime is less than the end_time. Within this loop the scheduled_task 
    is run every day at 11:30. After this, the function sleeps for 60 seconds before checking the schedule again.
    """
    schedule.run_pending()
    time.sleep(60)  # Check for scheduled tasks every minute
