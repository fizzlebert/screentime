# Screentime
> ScreenTime™ for non iOS devices

## Why?
Now adays most modern mobile phones are equiped with software to keep track of its usage while many desktop devices do not so I decided to make one.  Also it is made entirely from the Python standard library.

## Installation
`pip3 install --user screentime`

## Usage:
```
usage: screentime [-h] [--begin] [--end] [--summary]

Keep track of Daniel's unhealthy screen usage.

optional arguments:
  -h, --help     show this help message and exit
  --begin, -b    begin a new session
  --end, -e      end a session
  --summary, -s  get infromation on previous sessions
```

The program works based on sessions.  A session is a period of time that you spend on your device.  This means that you have to **manually** say tell it when you start and stop using your device.

## Begin a session
`$ screentime -b`

## Ending a session
`$ screentime -e`

## View a summary of your screentime
`$ screentime -s`

## Some issues you should know about
- You have to **manually** tell the programm when you are using your device
- The screen time information is presented in the most plain and boring way possible
