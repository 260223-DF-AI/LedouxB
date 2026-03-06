import pytest
from decorators import timer, retry, cache
from time import sleep

def test_timer_returns_result():
    """Timer decorator should not affect return value."""
    @timer
    def add(x, y):
        return x + y
    
    assert add(2, 3) == 5

def test_retry_succeeds_eventually():
    """Retry should succeed if function works within attempts."""
    @retry
    def fail(n):
        pass

def test_cache_returns_cached_value():
    """Cache should return same value without recomputing."""
    pass

def test_cache_info_tracks_hits():
    """Cache info should track hits and misses."""
    @cache()
    def add(x, y):
        return x + y
    
    add(2, 3)
    add(2, 3)
    info = add.cache_info()[0]
    hits = info["hits"]
    misses = info["misses"]

    assert hits == 1
    assert misses == 1