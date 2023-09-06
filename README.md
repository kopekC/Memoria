# Memoria - A Project About the Fragility of Memories

## Table of Contents
- [Summary](#summary)
- [Technical Description](#technical-description)
- [Implementation](#implementation)
- [Usage](#usage)
- [Authors](#authors)
- [Gallery](#gallery)
- [Code and Hardware](#code-and-hardware)
- [Special Thanks](#special-thanks)

## Summary

MEMORIA is a four-channel expanded cinema installation combining
ethnographic research, science fiction, and forms of cinema using found or pirated footage. It combines the dystopian narrative of William Gibson’s Johnny Mnemonic (1981) and the real-world Cuban “offline internet”, the Paquete Semanal. Actors and actual Paqueteros portray Gibson’s characters in this "documentary remake." The narrative is displayed on 4 synchronized screens, amalgamating
live-action and Paquete-based found footage, archived in ARCA (Archive).

## Technical Description

MEMORIA employs a unique physical and software setup for a four-channel installation. The hardware revolves around a computer with a video card supporting four 4K outputs. This central server synchronously runs the four video channels and a 4.1 audio track. The server runs a bash script, Lost.CU, executing various programs including FFMPG, and custom Ruby programs, Datamosh and Moshy, that continuously manipulates the video. This mechanism imitates the process of memory loss, visually represented by a gradual degradation of visual information and quality. Counterintuitively, the video files enrich with their own information every day and increase in size throughout their faulty replication process. The deterioration speed is calibrated to the duration of the exhibition, and the process can be compared metaphorically to cancerous growth.




## Implementation

The key components of the Memoria project, implemented with Python and the VLC media player, are:

### `corrupt_video(input_file, output_file_template, initial_crf=30, noise_intensity=2)`
This function applies a noise filter to an input video file, renames it, and deletes the original file.

### `play_video(screen_number, video_file)`
This function plays a specified video file on the VLC media player. 

### `start_videos(video_files)`
Starts instances of the VLC media player for each video file. 

### `stop_videos(vlc_processes)`
Stops all running VLC media player instances.

In the main script, memoria.py, a schedule is set for periodically corrupting and restarting the videos.



## Usage

To use the Memoria project, you'll need to have Python and the VLC media player
installed on your system. Clone the project repository, navigate to the project
directory, and run the following command:

```
python3 final.py
```

None


## Galery

[AKSIOMA](https://aksioma.org/)

None


None


