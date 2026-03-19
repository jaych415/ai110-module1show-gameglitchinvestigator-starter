from logic_utils import check_guess, parse_guess

def test_check_guess_high():
    assert check_guess(60, 50) == "high"

def test_check_guess_low():
    assert check_guess(40, 50) == "low"

def test_check_guess_correct():
    assert check_guess(50, 50) == "correct"

def test_parse_valid():
    assert parse_guess("25") == 25

def test_parse_invalid_string():
    assert parse_guess("abc") is None

def test_parse_out_of_range():
    assert parse_guess("150") is None