import requests
import collections
import arrow

try:
    collections.Mapping = collections.abc.Mapping
    collections.Iterable = collections.abc.Iterable
except AttributeError:
    pass

from ics import Calendar

def merge_intervals(slots):
    if not slots:
        return []
    
    slots.sort(key=lambda x: x[0])
    merged = [slots[0]]
    for current in slots[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)
    return merged

def fetch_busy_times(calendar_url):
    """
    Fetches the iCalendar URL using requests, parses the text using Calendar(), 
    and returns a list of all events.
    """
    from ics import Calendar
    try:
        response = requests.get(calendar_url)
        response.raise_for_status()
        
        calendar = Calendar(response.text)
        return list(calendar.events)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch calendar {calendar_url}: {e}")
        return []
    except Exception as e:
        print(f"Error parsing calendar data: {e}")
        return []

def find_group_free_time(urls, start_date=None, end_date=None, start_hour=8, end_hour=18, min_duration_minutes=30):
    """
    Core engine loop to find overlapping free time windows for a group.
    
    start_date / end_date: Should be Arrow objects, sets the date range to check.
    start_hour / end_hour: Integers representing the daily window (e.g. 8 to 18)
    """
    all_events = []
    for url in urls:
        events = fetch_busy_times(url)
        all_events.extend(events)
        
    if start_date is None:
        start_date = arrow.now('local').floor('day')
    if end_date is None:
        end_date = start_date.shift(days=4) 
    
    free_slots = []

    current_check_date = start_date
    while current_check_date <= end_date:
        
        day_start = current_check_date.replace(hour=start_hour, minute=0, second=0, microsecond=0)
        day_end = current_check_date.replace(hour=end_hour, minute=0, second=0, microsecond=0)
        
        slot_start = day_start
        while slot_start < day_end:
            slot_end = slot_start.shift(minutes=30)
            
            is_busy = False
            
            for event in all_events:
                event_start = event.begin.to('local')
                event_end = event.end.to('local')
                
                if event_start < slot_end and slot_start < event_end:
                    is_busy = True
                    break
            
            if not is_busy:
                free_slots.append((slot_start, slot_end))
                
            slot_start = slot_end
            
        current_check_date = current_check_date.shift(days=1)
        
    merged_slots = merge_intervals(free_slots)
    final_slots = []
    for start, end in merged_slots:
        duration_minutes = (end - start).total_seconds() / 60
        if duration_minutes >= min_duration_minutes:
            final_slots.append((start, end))
            
    return final_slots, len(all_events)


