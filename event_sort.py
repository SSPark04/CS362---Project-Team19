from dataclasses import dataclass, field
from datetime import date, time
from typing import List, Callable


@dataclass
class Event:
    name: str
    date: date
    time: time
    tags: List[str] = field(default_factory=list)


def sort_events(events: List[Event], by: str, reverse: bool = False, tag: str = None) -> List[Event]:
    """
    Sort events by a given attribute.
    by: "name", "date", "time", "tags"
    reverse: True for descending order
    tag: used only when sorting by tags (sort by whether tag is present)
    """

    if by == "name":
        key_func = lambda e: e.name.lower()

    elif by == "date":
        key_func = lambda e: e.date

    elif by == "time":
        key_func = lambda e: e.time

    elif by == "tags":
        if tag:
            # Sort by whether the tag is present (True first), then alphabetically
            key_func = lambda e: (tag not in e.tags, sorted(e.tags))
        else:
            # Sort alphabetically by first tag
            key_func = lambda e: sorted(e.tags) if e.tags else [""]

    else:
        raise ValueError(f"Unknown sort key: {by}")

    return sorted(events, key=key_func, reverse=reverse)