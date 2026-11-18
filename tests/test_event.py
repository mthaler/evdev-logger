from datetime import timezone

from event_logger import Event, EventLevel


def test_event_has_utc_timestamp() -> None:
    event = Event(name="test")
    assert event.timestamp.tzinfo == timezone.utc


def test_event_serializes_level_and_data() -> None:
    event = Event(name="user_created", level=EventLevel.INFO, data={"user_id": 7})
    result = event.to_dict()
    assert result["name"] == "user_created"
    assert result["level"] == "INFO"
    assert result["data"] == {"user_id": 7}
