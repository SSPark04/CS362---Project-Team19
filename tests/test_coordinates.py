import data_manager


def test_nonvirtual_events_have_coordinates():
    events = data_manager.load_events()
    for ev in events:
        if ev.get("building", "").lower() != "virtual":
            lat = ev.get("latitude")
            lon = ev.get("longitude")
            assert lat is not None and lon is not None
            assert lat != 0 or lon != 0, f"event {ev['event_id']} missing coords"


def test_virtual_events_coordinates_zero():
    events = data_manager.load_events()
    for ev in events:
        if ev.get("building", "").lower() == "virtual":
            assert ev.get("latitude") == 0
            assert ev.get("longitude") == 0
