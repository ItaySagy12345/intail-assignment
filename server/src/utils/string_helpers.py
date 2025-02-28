from datetime import datetime, timezone


def getTimestamp() -> str:
    """
    Returns the current time
    Return [String]: The current date in readable form
    """
        
    now: datetime = datetime.now(timezone.utc)
    date: str = now.strftime("%Y-%m-%d %H:%M:%S %Z")
    return date


def trim_string(string: str) -> str:
    """
    Removes white space from a string
    Param: string [String]: The string to trim
    Return [String]: The trimmed string
    """

    return string.replace(" ", "")


def format_slug(slug: str) -> str:
    """
    Formats a slug before inserting into the db
    Param: slug [String]: The slug to format
    Return [String]: The formatted slug    
    """
        
    return trim_string(string=slug).lower()