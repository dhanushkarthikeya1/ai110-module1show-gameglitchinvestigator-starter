# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Blank and whitespace-only input | Prompt summary: add pytest coverage for empty input and whitespace so it is rejected with a useful message. | Assert `parse_guess("")`, `parse_guess("   ")`, and `parse_guess(None)` return `(False, None, "Enter a guess.")`. | Yes | Users may submit an empty field; it should not turn into a guess or crash. |
| Decimal input | Prompt summary: check that decimal guesses are handled deliberately instead of silently changing their value. | Assert `parse_guess("40.9")` returns `(False, None, "Enter a whole number.")`. | Yes | The starter used `int(float(raw))`, which truncates a decimal such as 40.9 to 40 and changes the user's input. |
| Non-numeric text | Prompt summary: add a pytest case for text that cannot represent a whole-number guess. | Assert `parse_guess("four")` returns `(False, None, "Enter a whole number.")`. | Yes | This checks invalid text is handled as a normal validation result rather than an exception. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
