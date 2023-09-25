#!/usr/bin/env python3
import subprocess
import time
import datetime
import schedule
import threading
import os


def corrupt_video(input_file, output_file_template, initial_crf=30, noise_intensity=2):
    """
    Corrupts the input video file by adding noise and renames it to the original filename.
    
    :param input_file: str, the path to the input video file.
    :param output_file_template: str, the template for the output file name.
    :param initial_crf: int, optional, the initial Constant Rate Factor value for video encoding (default is 30).
    :param noise_intensity: int, optional, the intensity of the noise to be added to the video (default is 2).
    :return: str, the path to the corrupted video file.
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
    Plays the input video file in fullscreen mode using VLC and returns the VLC process.
    
    :param screen_number: int, the screen number where the video should be played.
    :param video_file: str, the path to the video file to be played.
    :return: subprocess.Popen, the VLC process playing the video.
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
    Processes a list of video files and returns the list of processed video file paths.
    
    :return: list, the list of paths to the processed video files.
    """
    video_files = [f"screen-{i}.mp4" for i in range(1, 5)]

    for i, video_file in enumerate(video_files):
        # Use the same filename for input and output
        output_file = corrupt_video(video_file, f"temp_{video_file}")
        video_files[i] = output_file

    return video_files


def start_videos(video_files):
    """
    Starts playing the list of video files and returns the list of VLC processes.
    
    :param video_files: list, the list of paths to the video files to be played.
    :return: list, the list of VLC processes playing the videos.
    """
    vlc_processes = []

    for i, video_file in enumerate(video_files):
        vlc_process = play_video(i, video_file)
        vlc_processes.append(vlc_process)

    return vlc_processes


def stop_videos(vlc_processes):
    """
    Stops playing the videos by killing the corresponding VLC processes.
    
    :param vlc_processes: list, the list of VLC processes playing the videos.
    """
    for vlc_process in vlc_processes:
        vlc_process.kill()


end_time = datetime.datetime.now() + datetime.timedelta(days=30)

# Play the videos immediately
video_files = [f"screen-{i}.mp4" for i in range(1, 5)]
vlc_processes = start_videos(video_files)

# Schedule the corruption process


def scheduled_task():
    """
    Stops the currently playing videos, processes the video files, and restarts playing the processed videos.
    """
    global vlc_processes
    global video_files

    stop_videos(vlc_processes)
    video_files = process_videos()
    vlc_processes = start_videos(video_files)


schedule.every().day.at("11:30").do(scheduled_task)

while datetime.datetime.now() < end_time:
    schedule.run_pending()
    time.sleep(60)  # Check for scheduled tasks every minute
