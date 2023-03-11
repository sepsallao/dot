# EDITOR: SEP SALLAO

from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty -e fish"      # My terminal of choice
myBrowser = "brave"  # My terminal of choice
myIDE = "code" # my dev environment
myScreenShot = "scrot -s /home/sep/Pictures/Screenshots/sep-sc-%b%d-%H%M%S.png"
libreofficeTaskMntr = "libreoffice Documents/work/tracker/cis-local-tracker.ods"
myFileManager = "thunar"

keys = [
    # The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'
        ),
    Key([mod, "shift"], "Return",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc='Run Launcher'
        ),
    Key([mod], "f",
        lazy.spawn(myFileManager),
        desc='Launch File Mager: Thunar'
        ),
    Key([mod], "b",
        lazy.spawn(myBrowser),
        desc='brave'
        ),
    Key([mod], "d",
        lazy.spawn(myIDE),
        desc='vs code'
        ),
    Key([mod], "t",
        lazy.spawn(libreofficeTaskMntr),
        desc='libreoffice directly to the file'
        ),
    Key([mod], "s",
        lazy.spawn(myScreenShot),
        desc='scrot -s'
        ),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
        ),
    Key([mod], "w",
        lazy.window.kill(),
        desc='Kill active window'
        ),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
        ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
        ),
    #  Key(["control", "shift"], "e",
    #      lazy.spawn("emacsclient -c -a emacs"),
    #      desc='Doom Emacs'
    #      ),
    # Switch focus to specific monitor (out of three)
    #  Key([mod], "w",
    #      lazy.to_screen(0),
    #      desc='Keyboard focus to monitor 1'
    #      ),
    #  Key([mod], "e",
    #      lazy.to_screen(1),
    #      desc='Keyboard focus to monitor 2'
    #      ),
    #  Key([mod], "r",
    #      lazy.to_screen(2),
    #      desc='Keyboard focus to monitor 3'
    #      ),
    # Switch focus of monitors
    #  Key([mod], "period",
    #      lazy.next_screen(),
    #      desc='Move focus to next monitor'
    #      ),
    #  Key([mod], "comma",
    #      lazy.prev_screen(),
    #      desc='Move focus to prev monitor'
    #      ),
    # Treetab controls
    #   Key([mod, "shift"], "h",
    #      lazy.layout.move_left(),
    #      desc='Move up a section in treetab'
    #      ),
    #  Key([mod, "shift"], "l",
    #      lazy.layout.move_right(),
    #      desc='Move down a section in treetab'
    #      ),
    # Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
#    Key([mod, "shift"], "f",
#        lazy.window.toggle_floating(),
#        desc='toggle floating'
#        ),
#    Key([mod], "f",
#        lazy.window.toggle_fullscreen(),
#        desc='toggle fullscreen'
#        ),
    # Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioMicMute",lazy.spawn("amixer set Capture toggle"))
    # Emacs programs launched using the key chord CTRL+e followed by 'key'
    # KeyChord(["control"], "e", [
    #          Key([], "e",
    #              lazy.spawn("emacsclient -c -a 'emacs'"),
    #              desc='Launch Emacs'
    #              ),
    #          Key([], "b",
    #              lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
    #              desc='Launch ibuffer inside Emacs'
    #              ),
    #          Key([], "d",
    #              lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
    #              desc='Launch dired inside Emacs'
    #              ),
    #          Key([], "i",
    #              lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
    #              desc='Launch erc inside Emacs'
    #              ),
    #          Key([], "m",
    #              lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
    #              desc='Launch mu4e inside Emacs'
    #              ),
    #          Key([], "n",
    #              lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
    #              desc='Launch elfeed inside Emacs'
    #              ),
    #          Key([], "s",
    #              lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
    #              desc='Launch the eshell inside Emacs'
    #              ),
    #          Key([], "v",
    #              lazy.spawn(
    #                  "emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
    #              desc='Launch vterm inside Emacs'
    #              )
    #          ]),
    # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
    # KeyChord([mod], "p", [
    #          Key([], "e",
    #              lazy.spawn("./dmscripts/dm-confedit"),
    #              desc='Choose a config file to edit'
    #              ),
    #          Key([], "i",
    #              lazy.spawn("./dmscripts/dm-maim"),
    #              desc='Take screenshots via dmenu'
    #              ),
    #          Key([], "k",
    #              lazy.spawn("./dmscripts/dm-kill"),
    #              desc='Kill processes via dmenu'
    #              ),
    #          Key([], "l",
    #              lazy.spawn("./dmscripts/dm-logout"),
    #              desc='A logout menu'
    #              ),
    #          Key([], "m",
    #              lazy.spawn("./dmscripts/dm-man"),
    #              desc='Search manpages in dmenu'
    #              ),
    #          Key([], "o",
    #              lazy.spawn("./dmscripts/dm-bookman"),
    #              desc='Search your qutebrowser bookmarks and quickmarks'
    #              ),
    #          Key([], "r",
    #              lazy.spawn("./dmscripts/dm-reddit"),
    #              desc='Search reddit via dmenu'
    #              ),
    #          Key([], "s",
    #              lazy.spawn("./dmscripts/dm-websearch"),
    #              desc='Search various search engines via dmenu'
    #              ),
    #          Key([], "p",
    #              lazy.spawn("passmenu"),
    #              desc='Retrieve passwords with dmenu'
    #              )
    #          ])
]

groups = [Group(" Trm ", {'layout': 'monadtall'}),
          Group(" Dev ", {'layout': 'monadtall'}),
          Group(" Dsk ", {'layout': 'monadtall'}),
          Group(" Web ", {'layout': 'monadtall'}),
          Group(" Spc ", {'layout': 'monadtall'}),
          Group(" Cfg ", {'layout': 'monadtall'})]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 2,
                "border_focus": "ffffff"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    # layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Floating(**layout_theme)
]

colors = [["#C6D4D7", "#C6D4D7"],  # 0 DARKER WHITE
          ["#ffffff", "#ffffff"],  # 1 WHITE
          ["#4F6F62", "#4F6F62"],  # 2 GREEN
          ["#CD3F59", "#CD3F59"],  # 3 RED
          ["#FEDD5A", "#FEDD5A"],  # 4 YELLOW
          ["#191919", "#191919"],  # 5 DARK GRAY
          ["#BB9672", "#BB9672"],  # 6 BROWN
          ["#56575A", "#56575A"]]  # 7 GUN GRAY

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu",
    fontsize=12,
    padding=2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[5],
            background=colors[5]
        ),
        #   widget.Image(
        #            filename = "~/.config/qtile/icons/python-white.png",
        #            scale = "False",
        #            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
        #            ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[5],
            background=colors[5]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=0,
            padding_x=5,
            borderwidth=4,
            active=colors[3],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[4],
            highlight_method="line",
            this_current_screen_border=colors[2],
            this_screen_border=colors[7],
            other_current_screen_border=colors[0],
            other_screen_border=colors[1],
            foreground=colors[1],
            background=colors[5]
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=colors[5],
            background=colors[5]
        ),
        widget.Sep(
            linewidth=0,
            padding=40,
            foreground=colors[5],
            background=colors[5]
        ),
        widget.WindowName(
            font="Ubuntu Bold",
            foreground=colors[5],
            background=colors[5],
            padding=0
        ),
        widget.TextBox(
            text='',
            background=colors[5],
            foreground=colors[2],
            padding=0,
            fontsize=37
        ),
        #   widget.Systray(
        #            background = colors[1],
        #            padding = 5,
        #            margin_x = 5
        #            ),
        widget.Sep(
            linewidth=10,
            padding=10,
            foreground=colors[2],
            background=colors[2],
            size_percent=80
        ),
        widget.Net(
            interface="wlan0",
            format='↓{down}  |  ↑{up}',
            foreground=colors[1],
            background=colors[2],
            padding=10,
            fontsize=12,
            font="Ubuntu Bold",
            use_bits=True,
            update_interval=3
        ),
        widget.TextBox(
            text='',
            background=colors[2],
            foreground=colors[4],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text="CPU: ",
            padding=2,
            foreground=colors[7],
            background=colors[4],
            font="Ubuntu Bold",
            fontsize=12
        ),
        widget.ThermalSensor(
            foreground=colors[7],
            background=colors[4],
            threshold=90,
            font="Ubuntu Bold",
            padding=5
        ),
        widget.TextBox(
            text='',
            background=colors[4],
            foreground=colors[3],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text="BATT: ",
            padding=2,
            foreground=colors[1],
            background=colors[3],
            font="Ubuntu Bold",
            fontsize=12
        ),
        widget.Battery(
            foreground=colors[1],
            background=colors[3],
            font="Ubuntu Bold",
            fontsize=12
        ),
        widget.TextBox(
            text='',
            background=colors[3],
            foreground=colors[6],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=" RAM: ",
            foreground=colors[1],
            background=colors[6],
            padding=0,
            font="Ubuntu Bold",
            fontsize=12
        ),
        widget.Memory(
            foreground=colors[1],
            background=colors[6],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            fontsize=12,
            font="Ubuntu Bold",
            padding=5
        ),
          widget.TextBox(
            text = '',
            background = colors[6],
            foreground = colors[7],
            padding = 0,
            fontsize = 37
                   ),
          widget.TextBox(
            fontsize=12,
            font="Ubuntu Bold",
            text = " VOL: ",
            foreground = colors[1],
            background = colors[7],
            padding = 0
                   ),
          widget.Volume(
            fontsize=12,
            font="Ubuntu Bold",
            foreground = colors[1],
            background = colors[7],
            padding = 5
                   ),
        #   widget.TextBox(
        #            text = '',
        #            background = colors[2],
        #            foreground = colors[3],
        #            padding = 0,
        #            fontsize = 37
        #            ),
        #   widget.CurrentLayoutIcon(
        #            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
        #            foreground = colors[1],
        #            background = colors[3],
        #            padding = 0,
        #            scale = 0.7
        #            ),
        #   widget.CurrentLayout(
        #            foreground = colors[1],
        #            background = colors[3],
        #            padding = 5
        #            ),
        widget.TextBox(
            text='',
            background=colors[7],
            foreground=colors[0],
            padding=0,
            fontsize=37
        ),
        widget.Clock(
            foreground=colors[7],
            background=colors[0],
            fontsize=12,
            font="Ubuntu Bold",
            format="%b %d | %H:%M "
        ),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # Slicing removes unwanted widgets (systray) on Monitors 1,3
    del widgets_screen1[7:8]
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # Monitor 2 will display all widgets in widgets_list
    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    # *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    # Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),
    # Match(wm_class='Blueman-adapters'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
