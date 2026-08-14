import builtins
import io
import sys

def compute_display(guess, word):
    display = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            display += guess[i].upper() + ' '
        elif guess[i] in word:
            display += guess[i].lower() + ' '
        else:
            display += "_ "
    return display.strip()

def build_expected_output(word, inputs):
    lines = []
    for guess_num, guess in enumerate(inputs, start=1):
        lines.append(f"Guess {guess_num}:")
        lines.append(compute_display(guess, word))
        lines.append("") #newline 
    return "\n".join(lines)

def test_play_round():
    test_cases = [
        {
            "word": "apple",
            "inputs": ["apple"],
            "expected_return": (1, True),
        },
        {
            "word": "mango",
            "inputs": ["apple", "mango"],
            "expected_return": (2, True),
        },
        {
            "word": "peach",
            "inputs": ["apple", "apple", "apple", "apple", "apple", "apple"],
            "expected_return": (6, False),
        }
    ]

    original_stdout = sys.stdout
    score = 0
    total = len(test_cases) * 2

    for case in test_cases:
        print(f"Word: {case['word']}")
        print(f"Inputs: {case['inputs']}")

        inputs_iter = iter(case["inputs"])
        def mock_get_player_guess():
            return next(inputs_iter)

        sys.stdout = io.StringIO()
        try:
            globals()["get_player_guess"] = mock_get_player_guess
            result = play_round(case["word"])
            output = sys.stdout.getvalue()
        except NameError:
            result = "ERROR: NameError"
            output = ""
        except Exception as e:
            result = f"ERROR: {type(e).__name__} - {e}"
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = original_stdout

        print(f"Returned: {result}")
        if result == case["expected_return"]:
            print("✔ Return value correct")
            score += 1
        else:
            print(f"❌ Return value incorrect (expected {case['expected_return']})")

        expected_output = build_expected_output(case["word"], case["inputs"])
        collapsed_output = " ".join(output.split())
        collapsed_expected = " ".join(expected_output.split())

        if collapsed_expected in collapsed_output:
            print("✔ Printed output correct")
            score += 1
        else:
            print("❌ Printed output incorrect/missing")

        print("Printed output:")
        print(output.strip() if output.strip() else "[no printed output]")
        print("Expected output:")
        print(expected_output)
        print("-" * 60)

    print(f"\nPassed {score}/{total} tests")

test_play_round()
