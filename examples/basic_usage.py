from event_logger import EventLogger, JsonlHandler

logger = EventLogger(
    handlers=[JsonlHandler("logs/events.jsonl")],
    source="demo",
)

logger.info("application_started", version="0.1.0")
logger.warning("cache_miss", key="homepage")
logger.error("job_failed", job_id=123, reason="timeout")
