

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if not isinstance(friend_name, str):
        raise TypeError("expect string as input only")
    return f"Hello, {friend_name}!"
