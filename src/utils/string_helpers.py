from datetime import datetime, timezone


def getTimestamp() -> str:
    """
    Returns the current time
    Return [String]: The current date in readable form
    """
        
    now: datetime = datetime.now(timezone.utc)
    date: str = now.strftime("%Y-%m-%d %H:%M:%S %Z")
    return date