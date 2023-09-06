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

