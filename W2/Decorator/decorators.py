from functools import wraps
import time

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs) # might need to save and return result
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds") #swap for logger?
        return result
    return wrapper

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args} {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                except:
                    time.sleep(delay)
                else:
                    return result
        return wrapper
    return decorator


def cache(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    cache = {}
    c_info = {
        "max_size": max_size,
        "curr_size": len(cache),
        "hits": 0,
        "misses": 0
    }
    @cache(max_size)
    def decorator(func):
        func.cache_info = lambda : c_info
        func.cache_clear = lambda : cache.clear()
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            if (args, kwargs) not in cache.keys():
                # Miss, remove oldest item in cache if filled
                if len(cache) == max_size:
                    first = next(iter(cache.keys()))
                    del(cache[first])
                    c_info["misses"] += 1
                result = func(*args, **kwargs)
            else:
                # Hit, pop result from cache to be moved to end
                result = cache.pop((args, kwargs))
                c_info["hits"] += 1
            cache[(args, kwargs)] = result
            return cache[(args, kwargs)]
        return wrapper
    return decorator