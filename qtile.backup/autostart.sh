#!/bin/sh
feh --bg-scale /usr/share/endeavouros/backgrounds/1440pBoba.png
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
# ~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
# eos-welcome & disown

# /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
