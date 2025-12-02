if [ -d /etc/X11/xinit/xinitrc.d ] ; then
    for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
        [ -x "$f" ] && . "$f"
    done
    unset f
fi

picom -b
source .fehbg
while xsetroot -name "`date`"
do
  sleep 1
done &
exec dwm

