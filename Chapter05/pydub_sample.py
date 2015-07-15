#!/usr/bin/env python

from pydub.generators import Pulse

# Create 10 seconds of audio
audio = Pulse(440, duty_cycle=0.6).to_audio_segment() * 10

# Fade it in and out
faded = audio.fade_in(2500).fade_out(5000)

# Save it
faded.export("test_audio.mp3", format="mp3")

