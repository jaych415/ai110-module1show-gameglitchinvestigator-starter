def parse_guess(user_input):
    """
    Converts user input into an integer.
    Returns None if invalid.
    """
    try:
        guess = int(user_input)
        if 1 <= guess <= 100:
            return guess
        return None
    except:
        return None


def check_guess(guess, secret):
    """
    Compares guess with secret number.
    Returns: 'high', 'low', or 'correct'
    """
    if guess > secret:
        return "high"
    elif guess < secret:
        return "low"
    else:
        return "correct"