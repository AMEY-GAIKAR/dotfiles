#!/bin/sh

# picom
picom -b

# Wallpaper
feh --no-feh --bg-fill '/home/amey/Pictures/Wallpapers/Witcher_IV_Wallpaper_01_13840x2160_EN.jpeg'

# touchpad
xinput set-prop "SynPS/2 Synaptics TouchPad" "libinput Tapping Enabled" 1
xinput set-prop "SynPS/2 Synaptics TouchPad" "libinput Natural Scrolling Enabled" 1
