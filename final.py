#!/usr/bin/env python3
import subprocess
import time
import datetime
import schedule
import threading
import os


def corrupt_video(input_file, output_file_template, initial_crf=30, noise_intensity=2):
    """
    This function takes an input video file and applies a noise filter to it using FFmpeg. The corrupted video is saved 
    as a temporary file with a new name specified by the output file template parameter. The original input file 
    is then deleted, and the temporary file is renamed to the original file name.
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
    This function opens a new VLC instance and plays a given video file on a specified screen number.
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
    This function applies the corrupt_video() function to a set of input video files, creating a new set 
    of corrupted video files for each original file in the list 'video_files'.
    """
    video_files = [f"screen-{i}.mp4" for i in range(1, 5)]

    for i, video_file in enumerate(video_files):
        # Use the same filename for input and output
        output_file = corrupt_video(video_file, f"temp_{video_file}")
        video_files[i] = output_file

    return video_files


def start_videos(video_files):
    """
    This function initializes the VLC instances to play the given video files on unique screen numbers as 
    specified in the video_files list. It returns a list of these running VLC processes.
    """
    vlc_processes = []

    for i, video_file in enumerate(video_files):
        vlc_process = play_video(i, video_file)
        vlc_processes.append(vlc_process)

    return vlc_processes


def stop_videos(vlc_processes):
    """
    This function discontinues any running VLC instances by killing their corresponding processes.
    """
    for vlc_process in vlc_processes:


        vlc_process.kill()


end_time = datetime.datetime.now() + datetime.timedelta(days=30)

# Play the videos immediately
video_files = [f"screen-{i}.mp4" for i in range(1, 5)]
vlc_processes = start_videos(video_files)

# Schedule the corruption process


def scheduled_task():
    global vlc_processes
    global video_files

    stop_videos(vlc_processes)
    video_files = process_videos()
    vlc_processes = start_videos(video_files)


schedule.every().day.at("11:30").do(scheduled_task)

while datetime.datetime.now() < end_time:
    schedule.run_pending()
    time.sleep(60)

