def format_name(first: str, last: str) -> str:
    """Format a full name from the first and last names"""
    return f"{first} {last}"

def truncate(text, length: int = 50) -> str:
    """Truncate text to a certain length"""
    if type(text) != str:
        text = str(text)
    if len(text) < length:
        return text
    else:
        return text[:length] + "..."
    
DEFAULT_ENCODING = "utf-8" # module-level variable, will be accessible wherever module imported

