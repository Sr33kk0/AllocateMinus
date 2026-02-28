import requests
import collections

try:
    collections.Mapping = collections.abc.Mapping
    collections.Iterable = collections.abc.Iterable
except AttributeError:
    pass

from ics import Calendar

def read_and_print_ics_url(calendar_url):
    print(f"🌐 Fetching live timetable from URL...")
    
    try:
        response = requests.get(calendar_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Failed to fetch calendar. Details: {e}")
        return

    calendar = Calendar(response.text)
    events = list(calendar.events)
    
    events.sort(key=lambda event: event.begin)

    print(f"✅ Successfully found {len(events)} classes from the link.\n")
    print("=" * 40)

    for event in events:
        event_name = event.name or "Unknown Class"
        start_time = event.begin.to('local').format('YYYY-MM-DD HH:mm')
        end_time = event.end.to('local').format('HH:mm')

        print(f"📘 Class: {event_name}")
        print(f"⏰ Time:  {start_time} to {end_time}")
        print(f"📍 Location: {event.location or 'No room assigned'}")
        print("-" * 40)

