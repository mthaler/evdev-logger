import json

from event_logger import EventLogger, JsonlHandler


def test_logger_writes_jsonl(tmp_path) -> None:
    output = tmp_path / "logs" / "events.jsonl"
    logger = EventLogger(handlers=[JsonlHandler(output)], source="tests")

    logger.info("user_login", user_id=12)

    records = output.read_text(encoding="utf-8").splitlines()
    assert len(records) == 1
    event = json.loads(records[0])
    assert event["name"] == "user_login"
    assert event["source"] == "tests"
    assert event["data"]["user_id"] == 12


def test_logger_returns_event() -> None:
    logger = EventLogger(source="unit-test")
    event = logger.warning("slow_request", duration_ms=500)
    assert event.name == "slow_request"
    assert event.source == "unit-test"
