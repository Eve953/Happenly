import streamlit as st
from streamlit_calendar import calendar


calendar_options = {
    "editable": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},  # placeholder 
    ],
}
calendar_events = [
    {
        "title": "Event 1",         # this is just a placeholder
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "a",
    },
    
]


calendar = calendar(
    events=calendar_events,
    options=calendar_options,
    key='calendar', 
    )
