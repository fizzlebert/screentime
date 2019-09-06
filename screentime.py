import pickle

from argparse import ArgumentParser
from datetime import datetime, timedelta
from dataclasses import dataclass
from pathlib import Path


# Files and folders where information is stored
SCREEN_FOLDER = Path.home() / ".screentime"
SCREEN_FILE = SCREEN_FOLDER / "screentimes"
TIME_FILE = SCREEN_FOLDER / "lasttime"


@dataclass
class Day:
    date: datetime
    screentime: list


@dataclass
class ScreenData:
    days: dict

    def __iter__(self):
        return iter(self.days)


def store(date: datetime, screentime: timedelta):
    screentimes = pickle.load(SCREEN_FILE.open("rb")) if SCREEN_FILE.exists() else None

    if screentimes is None:
        day = Day(date, [screentime])
        screentimes = ScreenData({date: day})
    else:
        found = False
        for day in screentimes:
            if day.date() == date.date():
                found = True
                screentimes.days[day].screentime.append(screentime)

        if not found:
            day = Day(date, [screentime])
            screentimes[date] = day

    pickle.dump(screentimes, SCREEN_FILE.open("wb"))


now = datetime.now()

# Basic argument parsing
parser = ArgumentParser(description="Keep track of Daniel's unhealthy screen usage.")
parser.add_argument("--begin", "-b", help="begin a new session", action="store_true")
parser.add_argument("--end", "-e", help="end a session", action="store_true")
parser.add_argument(
    "--summary", "-s", help="get infromation on previous sessions", action="store_true"
)

args = parser.parse_args()

# Create folders if they don't already exist
if not SCREEN_FOLDER.exists() or not SCREEN_FOLDER.is_dir():
    Path.mkdir(SCREEN_FOLDER)

# Make sure user hasn't told the program to do something unreasonable
if args.begin and args.end:
    raise parser.error("either beinging or ending a session")

if args.begin:
    # If a session has started check if user wants to override it
    if TIME_FILE.exists():
        choice = input("Session already started are you sure you want to override it? ")
        if choice.lower() == "y":
            pickle.dump(now, TIME_FILE.open("wb"))
    # Otherwise save the start time of the session
    else:
        pickle.dump(now, TIME_FILE.open("wb"))

elif args.end:
    # Make sure a session has been started
    if not TIME_FILE.exists():
        raise RuntimeError("no session has been started")

    # Check if any previous session stored
    initialise = not SCREEN_FILE.exists()

    # Load when session started and remove file to mark end of a session
    beginning = pickle.load(TIME_FILE.open("rb"))
    TIME_FILE.unlink()

    # If session goes across multiple days split up into sections
    if beginning.date() != now.date():
        screen_times = []

        # Iterate through number of days session goes for storing
        # screen time for each day in screen_times
        today = beginning
        for _ in range((now - beginning).days):
            tomorrow = datetime(today.year, today.month, today.day + 1)
            screen_time = tomorrow - today
            store(today, screen_time)

            today = tomorrow
    else:
        store(beginning, now - beginning)

elif args.summary:
    # Make sure there are sessions to get information from
    if not SCREEN_FILE.exists():
        print("No sessions to show, sorry 😏.")
        quit()

    screentimes = pickle.load(SCREEN_FILE.open("rb")) if SCREEN_FILE.exists() else None

    # Sum all time differences for past few days
    for day in screentimes.days.values():
        seconds = (sum(day.screentime, timedelta(0))).total_seconds()
        minutes = seconds // 60
        hours = minutes // 60
        print(f"{day.date.date()} {hours:2.0f}:{minutes:2.0f}:{seconds:2.0f}")
