def validate_topic(topic: str):
    if not topic or len(topic.strip()) < 3:
        raise ValueError("Topic must be at least 3 characters long.")
