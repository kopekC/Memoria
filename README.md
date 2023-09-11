<!-- hola mundo ✭ 🚀 -->
# Memoria - A Project About the Fragility of Memories - 

## STATEMENT

MEMORIA is an immersive four-channel expanded cinema installation with
specifically developed software and hardware components. It combines
ethnographic research, science fiction, and “recombinatory” forms of cinema that
appropriate found or pirated footage. The work intertwines two narrative planes:
the dystopian vision of William Gibson’s Johnny Mnemonic (1981), one of the
earliest cyberpunk short stories, and the real-world Cuban “offline internet”,
the physical data distribution network Paquete Semanal. The work takes the form
of a “documentary remake” in which actors, performers, and actual Paqueteros
embody Gibson’s fictional characters. Havana stands in for the “Sprawl”, the
urban dystopia Gibson describes as a ruin of the future where technological and
scientific advances, such as artificial intelligence and cybernetics go hand in
hand with the breakdown of the social order.

MEMORIA’s narrative is presented on 4 synchronized screens that merge
live-action footage with found footage from videos that have circulated in Cuba
through the Paquete. These materials come from ARCA (Archive), an artwork
consisting of a 64 TB server that contains the entire content of Paquete Semanal
for an entire year (52 weekly issues). It remains the only large-scale archive
of this ephemeral phenomenon.

## TECHNICAL DESCRIPTION

Installation with 4 video channels, a central server, adapted hardware and
software, and computer chairs.

The installation surrounds the viewer with 4 synchronized screens of variable
sizes, hanging from the ceiling and transparent so that the projected image can
be seen from both sides. Between the screens are several rotating computer
chairs that invite the audience to sit.

To represent the protagonist's loss of memory, the work will slowly "die" over
the course of the exhibition. For this purpose, we have developed a special
hardware setup consisting of a computer with a video card with four 4K outputs,
which acts as the central server of the installation. From this server, the four
video channels and a 4.1 audio track are played back synchronously. This
computer also runs Lost.CU a bash script that executes various programs that
continuously manipulate the video: FFMPG, a powerful free software for video and
audio transcoding, and two custom programs written in Ruby: Datamosh, which
deletes segments of the video so they can be overwritten afterwards, and Moshy,
which overwrites these empty segments with information copied from random other
parts of the video. This process gives the impression that the visual
information in the videos is gradually lost and the image progressively
degrades. However, the process does just the opposite. The video files are
enriched with their own information, so the file increases in size during this
copy and overwrite process. Since there is no linear header in the file to
convert these bits into pixels, they become visible as artifacts that affect the
quality and smoothness of the videos. This automated, constant copying process
not only corrupts the audiovisual material, but eventually also damages the hard
disk where the project files are stored. The speed at which the material
deteriorates is adjusted to the duration of the work's exhibition. The copy
script basically operates like a tumor virus, like a cancer that makes the cells
inside the host grow in a random and uncontrolled way. Every day it produces a
new set of video files that amplifies the changes of the previous set: what
appear to be subtle changes in the first generations of video files become more
and more obvious in the later generations, eventually causing the information to
become completely distorted over time as the video devours itself through the
constant process of faulty replication. This process corresponds to what happens
to Johnny in the narrative when he loses his own memories due to the overload of
information in his brain.

## Implementation

The Memoria project is implemented using Python and the VLC media player. The
main components of the project include:

### `corrupt_video(input_file, output_file_template, initial_crf=30, noise_intensity=2)`

This function takes an input video file and applies a noise filter to it using
FFmpeg. The corrupted video is saved as a temporary file with a new name
specified by the output_file_template parameter. The original input file is then
deleted, and the temporary file is renamed to the original file name.

### `play_video(screen_number, video_file)`

This function plays a given video file on the VLC media player, using the
specified screen nuasdasdasd asdasd asdasd asd This function applies the
corrupt_video() function to a set of input video files, creating a set of
corrupted video files that will be played by the play_video() function.

### `start_videos(video_files)`

This function starts a set of VLC media player instances, each playing one of
the given video files using a unique screen number. The function returns a list
of subprocess.Popen objects representing the running VLC processes.

### `stop_videos(vlc_processes)`

This function stops a set of running VLC media player instances by killing their
corresponding subprocess.Popen objects.

The main script for the project is memoria.py, which sets up the schedule for
periodically corrupting and restarting the videos. The schedule is created using
the schedule module, and the scheduled_task() function is called at a set time
each day to stop the current videos, process new corrupted videos, and start
playing them.

## Usage

To use the Memoria project, you'll need to have Python and the VLC media player
installed on your system. Clone the project repository, navigate to the project
directory, and run the following command:

```
python3 final.py
```

## Authors

[Nestor Siré](https://nestorsire.com/en/)

[Steffen Köhn](http://steffenkoehn.com/)

## Galery

[AKSIOMA](https://aksioma.org/)

## Issues

### Missing HDMI audio outputs

When the project was set up in Aksioma, HDMI audio interfaces failed to appear.
Seems it was a bug in Ubuntu 22.10 (or was it 23.04?) default kernel. Upgrading
to the latest 6.1 kernel fixed that. There's a handy script
[here](https://github.com/pimlie/ubuntu-mainline-kernel.sh). Usually running the
latest kernel is not the best choice but in this case, bugs were fixed.

### Audio outputs do not match projections

Audio interfaces appeared but speakers did not match the projections shown. So
we switched VLC to JACK audio and modified the script to include the video IDs
in audio output names. Then used [qpwgraph](https://github.com/rncbc/qpwgraph)
to match audio outputs to projections. Connections can be persisted so future
glitched videos still match outputs.

## Code and Hardware

KopeK

## Special thanks to:

[g1smo](https://github.com/g1smo) for all the help with the audio, thanks m8 !


## Made with :heart: and FOSS in :cuba:
