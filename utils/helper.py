from datetime import datetime

def get_current_timestamp():
    return datetime.now().isoformat()


def format_datetime(timestamp: str) -> str:
    try:
        dt = datetime.fromisoformat(timestamp)
        return dt.strftime("%d %b %Y, %I:%M %p")
    except Exception:
        return timestamp 