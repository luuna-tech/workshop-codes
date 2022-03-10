def invalid_action(exception: Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            raise Exception('This action is not permitted')
        return wrapper
    return decorator
