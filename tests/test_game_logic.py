from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # FIX: Updated assertion to unpack the tuple returned by check_guess (instead of direct string comparison) and added a test for parsing floats, implemented in agent mode.
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_parse_guess_float():
    # Parse a decimal string to an integer
    ok, val, err = parse_guess("42.5")
    assert ok is True
    assert val == 42
    assert err is None

