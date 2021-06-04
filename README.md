# trigger.py

This is a small script to trigger some action based on a user-defined 
period of keyboard inactivity. It must be run as root since it monitors
the keyboard regardless of focus.

## Usage

Invoke the script as follows:
```
./trigger.py --timeout <some whole number of seconds> \
             --trigger-action <some shell command to be run> \
             --reset-action <some other shell command to be run>
```

The script can also be invoked with the ```--help``` flag, which will provide basic usage instructions.

Both ```trigger-action``` and ``` reset-action``` must be quoted if the contain spaces.

Providing ```reset-action``` is optional, but probably necessary in most cases, unless the ```trigger-action``` can meaningfully run several times in a row.

## Examples

Trigger a screen locker (```slock```) after 1 minute of inactivity (careful, it will require the root password!):
```
./trigger.py -t 60 -a slock
```

Disable the keyboard backlight after 30 seconds, restoring it on keyboard input. ```xset led *``` must work with the keyboard:
```
./trigger.py -t 30 -a 'xset led off' -r 'xset led on'
