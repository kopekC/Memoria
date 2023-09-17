#!/usr/bin/env python3
import subprocess
import time
import datetime
import schedule

import os


def corrupt_video(input_file, initial_crf=30, noise_intensity=2):
    """Corrupts a video using FFmpeg with specific parameters."""
    output_file = "temp_" + input_file

    ffmpeg_command = [
        "ffmpeg", "-y", "-i", input_file,
        "-vf", f"noise=c0s={noise_intensity}:allf=t+u,setpts=PTS",
        "-c:v", "libx264", "-b:v", "1000k", "-g", "60",
        "-crf", str(initial_crf), "-preset", "veryfast",
        "-c:a", "copy", output_file
    ]
    subprocess.run(ffmpeg_command, check=True)

    # Delete the original file and rename the corrupted one
    os.remove(input_file)
    os.rename(output_file, input_file)

    return input_file


def play_video(screen_number, video_file):
    """Plays a video using VLC with specific parameters."""
    vlc_command = [
        "vlc", "--fullscreen",
        f"--qt-fullscreen-screennumber={screen_number}",
        "--loop", "--no-video-title-show", video_file,
        "--no-jack-auto-connect",
        f"--jack-name={screen_number}"
    ]
    return subprocess.Popen(vlc_command)


def process_videos(videos):
    """Corrupts a list of videos."""
    return [corrupt_video(video) for video in videos]


def start_videos(video_files):
    """Plays a list of videos."""
    return [play_video(i, video_file) for i, video_file in enumerate(video_files)]


def stop_videos(vlc_processes):
    """Stops all playing videos."""
    for vlc_process in vlc_processes:
        vlc_process.kill()


def main():
    end_time = datetime.datetime.now() + datetime.timedelta(days=30)

    # Define the video files
    video_files = [f"screen-{i}.mp4" for i in range(1, 5)]
    vlc_processes = start_videos(video_files)

    def scheduled_task(videos, processes):
        """Task to be scheduled: stop videos, process them, and restart them."""
        stop_videos(processes)
        new_videos = process_videos(videos)
        new_processes = start_videos(new_videos)
        return new_videos, new_processes

    # Schedule the corruption process
    schedule.every().day.at("11:30").do(lambda: scheduled_task(video_files, vlc_processes))

    # Check for scheduled tasks every minute
    while datetime.datetime.now() < end_time:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
