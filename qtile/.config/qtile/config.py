import os
import subprocess

import colors
from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "x", lazy.spawn("/home/amey/i3lock-color/lock"), desc="Lock screen"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    # Control brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10"), desc="Brightness Up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10"), desc="Brightness Down"),
    # Control audio
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    # Screenshot
    Key([], "Print", lazy.spawn('maim /home/amey/Pictures/Screenshots/"$(date)".png', shell=True), desc="Screenshot"),
    # FIX
    Key([mod], "Print", lazy.spaw('maim --window "$(xdotool getactivewindow)" /home/amey/Pictures/Screenshots/"$(date)".png', shell=True), desc="Screenshot"),
    Key([mod, "shift"], "Print", lazy.spawn('maim --select /home/amey/Pictures/Screenshots/"$(date)".png', shell=True), desc="Screenshot"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
            # mod + tab to move to next group
            Key([mod], "Tab", lazy.screen.next_group()),
            # mod + shift + tab to move to previous group
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        ]
    )

layouts = [
    # layout.Columns(),
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        border_focus=colors.color_palette["sky"],
        border_normal=colors.color_palette["overlay0"],
        border_width=3,
        margin=2,
    ),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(
    #     border_focus=colors.color_palette['sky'],
    #     border_normal=colors.color_palette['overlay0'],
    #     border_width=3,
    #     margin=2,
    # ),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="CaskaydiaMono Nerd Font",
    fontsize=12,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    background=colors.color_palette["base"],
                    filename="/home/amey/Pictures/Wallpapers/HoYoWiki-image.webp",
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.GenPollText(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    func=lambda: subprocess.check_output(["light", "-G"])
                        .decode("utf-8")
                        .split(".")[0],
                    update_interval=0.5,
                    fmt=" {}%",
                    mouse_callbacks={
                        "Button5": lazy.spawn("light -A 5"),
                        "Button4": lazy.spawn("light -U 5"),
                    },
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.GenPollText(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    update_interval=0.5,
                    func=lambda: (
                        (lambda vol, mute: f"{'󰝛' if mute=='yes' else ''} {vol}%")(
                            int(
                                subprocess.check_output(
                                    ["pactl", "get-sink-volume", "@DEFAULT_SINK@"]
                                )
                                .decode()
                                .split("/")[1]
                                .strip()
                                .strip("%")
                            ),
                            subprocess.check_output(
                                ["pactl", "get-sink-mute", "@DEFAULT_SINK@"]
                            )
                            .decode()
                            .split(":")[1]
                            .strip(),
                        )
                    ),
                    mouse_callbacks={
                        "Button1": lazy.spawn(
                            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
                        ),
                        "Button5": lazy.spawn(
                            "pactl set-sink-volume @DEFAULT_SINK@ +5%"
                        ),
                        "Button4": lazy.spawn(
                            "pactl set-sink-volume @DEFAULT_SINK@ -5%"
                        ),
                    },
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.GenPollText(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    fmt="󰄀 ",
                    mouse_callbacks={
                        "Button1": lazy.spawn('maim /home/amey/Pictures/Screenshots/"$(date)".png', shell=True),
                    },
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.Spacer(),
                widget.GroupBox(
                    active=colors.color_palette["lavender"],
                    background=colors.color_palette["base"],
                    block_highlight_text_color=colors.color_palette["green"],
                    borderwidth=0,
                    hide_unused=True,
                    highlight_color=colors.color_palette["red"],
                    this_current_screen_border=colors.color_palette["maroon"],
                    spacing=2,
                    margin=2,
                    padding=5,
                    rounded=True,
                ),
                widget.Spacer(),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.CPU(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    format="󰍛 {load_percent}%",
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.Memory(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    format="  {MemUsed:.0f}/{MemTotal:.0f}",
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.Battery(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    charge_char="󰂄",
                    full_char="󰁹",
                    discharge_char="󰂀",
                    empty_char="󰂎",
                    format="{char}{percent: 2.0%}",
                    low_foreground=colors.color_palette["rosewater"],
                    low_percentage=0.3,
                    notification_timeout=10,
                    notify_below=30,
                    update_interval=0.5,
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.Clock(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    format=" %H:%M:%S",
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.Clock(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    format="󰃭 %a %b %d",
                ),
                widget.Sep(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    padding=10,
                ),
                widget.QuickExit(
                    background=colors.color_palette["base"],
                    foreground=colors.color_palette["text"],
                    default_text="⏻ ",
                    countdown_format="{}",
                ),
            ],
            24,
            opacity=0.8,
            background=colors.color_palette["base"],
            foreground=colors.color_palette["text"],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors.color_palette["sky"],
    border_normal=colors.color_palette["overlay0"],
    border_width=2,
    fullscreen_border_width=2,
    max_border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    start = os.path.expanduser(".config/qtile/autostart.sh")
    subprocess.run([start])
