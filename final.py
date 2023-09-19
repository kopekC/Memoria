#!/usr/bin/env python3
import subprocess
import time
import datetime
import schedule
import threading
import os


def corrupt_video(input_file, output_file_template, initial_crf=30, noise_intensity=2):
        """
    Corrupts a video file using the ffmpeg command-line tool.
    
    Args:
        input_file (str): Path to the input video file.
        output_file_template (str): Path template for the output file.
        initial_crf (int): Initial constant rate factor for video compression.
        noise_intensity (int): Intensity of the noise to be added to the video.
    
    Returns:
        str: Path to the corrupted video file.
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
    Plays a video file using VLC media player in fullscreen mode.
    
    Args:
        screen_number (int): The screen number to play the video on.
        video_file (str): Path to the video file to be played.
    
    Returns:
        subprocess.Popen: Process object of the VLC player.
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
    Process multiple video files to corrupt them.
    
    Returns:
        list: List of paths to the corrupted video files.
    """

    video_files = [f"screen-{i}.mp4" for i in range(1, 5)]

    for i, video_file in enumerate(video_files):
        # Use the same filename for input and output
        output_file = corrupt_video(video_file, f"temp_{video_file}")
        video_files[i] = output_file

    return video_files


def start_videos(video_files):
        """
    Start playing a list of video files in fullscreen mode.
    
    Args:
        video_files (list): List of paths to the video files to be played.
    
    Returns:
        list: List of VLC process objects.
    """

    vlc_processes = []

    for i, video_file in enumerate(video_files):
        vlc_process = play_video(i, video_file)
        vlc_processes.append(vlc_process)

    return vlc_processes


def stop_videos(vlc_processes):
        """
    Terminate the VLC processes that are playing videos.
    
    Args:
        vlc_processes (list): List of VLC process objects to be terminated.
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
    Scheduled task that stops the video playback, corrupts the video files,
    and restarts the video playback.
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
