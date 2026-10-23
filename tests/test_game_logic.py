from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_ranges_match_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_accepts_whole_numbers_and_whitespace():
    assert parse_guess(" 50 ") == (True, 50, None)
    assert parse_guess("-3") == (True, -3, None)


def test_parse_guess_rejects_empty_and_whitespace():
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess("   ") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")


def test_parse_guess_rejects_decimals_instead_of_truncating():
    assert parse_guess("40.9") == (False, None, "Enter a whole number.")


def test_parse_guess_rejects_non_numeric_text():
    assert parse_guess("four") == (False, None, "Enter a whole number.")


def test_check_guess_returns_win():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


def test_check_guess_returns_too_high_and_lower_hint():
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")


def test_check_guess_returns_too_low_and_higher_hint():
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


def test_score_rewards_faster_wins():
    assert update_score(0, "Win", 1) == 100
    assert update_score(0, "Win", 3) == 80


def test_score_penalizes_any_wrong_guess_without_going_negative():
    assert update_score(20, "Too High", 1) == 15
    assert update_score(20, "Too Low", 2) == 15
    assert update_score(0, "Too Low", 1) == 0
