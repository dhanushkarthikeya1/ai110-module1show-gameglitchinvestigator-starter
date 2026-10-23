"""Pure game rules for the Glitch Investigator guessing game."""


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the inclusive secret-number range for a difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str | None) -> tuple[bool, int | None, str | None]:
    """Parse a whole-number guess, rejecting blank, decimal, and invalid input."""
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        value = int(raw.strip())
    except ValueError:
        return False, None, "Enter a whole number."

    return True, value, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """Return the outcome and useful direction for a guess."""
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Apply a five-point penalty for a miss or reward a win by speed."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points
    if outcome in {"Too High", "Too Low"}:
        return max(0, current_score - 5)
    return current_score
