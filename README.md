# Screentime
> ScreenTime™ for non iOS devices

## Why?
Now adays most modern mobile phones are equiped with software to keep track of its usage while many desktop devices do not so I decided to make one.  Also it is made entirely from the Python standard library.

## Usage:
```
usage: screentime.py [-h] [--begin] [--end] [--summary]

Keep track of Daniel's unhealthy screen usage.

optional arguments:
  -h, --help     show this help message and exit
  --begin, -b    begin a new session
  --end, -e      end a session
  --summary, -s  get infromation on previous sessions
```

The program works based on sessions.  A session is how long you spend on your device.  This means that you have to *manually* say tell it when you start and stop using your device.

## Begin a session
`$ python3 screentime.py -b`

## Ending a session
`$ python3 screentime.py -e`

## View a summary of your screentime
`$ python3 screentime.py -s`

## Some issues you should know about
- You cannot view how long a session is currently
- You have to *manually* tell the programm when you are using your device
- The screen time information is presented in the mos plain and boring way possible
