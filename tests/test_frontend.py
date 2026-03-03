import os


def read_index():
    path = os.path.join(os.path.dirname(__file__), "..", "templates", "index.html")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_index_contains_calendar_script():
    html = read_index()
    assert "calendar.js" in html, "calendar.js script tag should be present"


def test_index_calendar_body_id():
    html = read_index()
    assert 'id="calendarBody"' in html


def test_index_event_list_id():
    html = read_index()
    assert 'id="eventList"' in html
    # old classname should be gone
    assert 'class="events"' not in html


def test_index_filter_buttons():
    html = read_index()
    assert 'data-filter="today"' in html
    assert 'data-filter="week"' in html
    assert 'data-filter="all"' in html


def test_index_custom_range_controls_present():
    html = read_index()
    assert 'id="rangeStart"' in html
    assert 'id="rangeEnd"' in html
    assert 'id="applyRangeBtn"' in html
    assert 'id="rangeError"' in html


def test_index_contains_map_script():
    html = read_index()
    assert "map.js" in html, "map.js script tag should be present"
