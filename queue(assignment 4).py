# lab assignment 4
# Implement an event processing system using Queue.

from collections import deque
event_queue = deque()

def add_event(event):
    event_queue.append(event)
    print(f"Event '{event}' added.")

def process_event():
    if event_queue:
        e = event_queue.popleft()
        print(f"Processed Event: {e}")
    else:
        print("No events to process.")

def display_events():
    print("Pending Events:", list(event_queue))

def cancel_event(event):
    if event in event_queue:
        event_queue.remove(event)
        print(f"Cancelled Event: {event}")
    else:
        print("Event not found in queue.")

# Main Program
add_event("Login")
add_event("Upload File")
add_event("Logout")
display_events()
process_event()
cancel_event("Logout")
display_events()
