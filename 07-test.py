import io
import sys

score = 0
total = 3

def test_play_round():
    global score

    test_cases = [
        {
            "name": "correct on first guess",
            "word": "apple",
            "inputs": ["apple"],
            "expected_return": (1, True),
        },
        {
            "name": "incorrect then correct",
            "word": "mango",
            "inputs": ["apple", "mango"],
            "expected_return": (2, True),
        },
        {
            "name": "all six guesses used",
            "word": "peach",
            "inputs": ["apple", "apple", "apple", "apple", "apple", "apple"],
            "expected_return": (6, False),
        }
    ]

    original_stdout = sys.stdout

    for i, case in enumerate(test_cases, start=1):
        print(f"Test: {case['name']}")
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
            print(f"✔ Test {i}: Return value correct")
            score += 1
        else:
            print(f"❌ Test {i}: Return value incorrect (expected {case['expected_return']})")

        print("Printed output:")
        print(output.strip() if output.strip() else "[no printed output]")
        print("-" * 60)

test_play_round()
print(f"\nPassed {score}/{total} tests")
