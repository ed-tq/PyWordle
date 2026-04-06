import builtins
import io
import sys

score = 0
total = 5

def test_get_player_guess():
    global score

    test_cases = [
        {
            "name": "valid word first try",
            "inputs": ["apple"],
            "expected_return": "apple"
        },
        {
            "name": "invalid length then valid word",
            "inputs": ["app", "apple"],
            "expected_return": "apple"
        },
        {
            "name": "non-alphabetic then valid word",
            "inputs": ["12345", "apple"],
            "expected_return": "apple"
        },
        {
            "name": "invalid word then valid word",
            "inputs": ["zzzzz", "apple"],
            "expected_return": "apple"
        },
        {
            "name": "uppercase valid word",
            "inputs": ["APPLE"],
            "expected_return": "apple"
        }
    ]

    original_input = builtins.input
    original_stdout = sys.stdout

    for i, case in enumerate(test_cases, start=1):
        print(f"Test: {case['name']}".center(50))

        inputs_used = []
        inputs_iter = iter(case["inputs"])

        def mock_input(prompt):
            value = next(inputs_iter)
            inputs_used.append(value)
            return value

        builtins.input = mock_input
        sys.stdout = io.StringIO()

        try:
            result = get_player_guess()
            output = sys.stdout.getvalue()
        except Exception as e:
            result = f"ERROR: {type(e).__name__} - {e}"
            output = sys.stdout.getvalue()
        finally:
            builtins.input = original_input
            sys.stdout = original_stdout

        output_lines = [line for line in output.strip().split("\n") if line]

        for j, user_input in enumerate(inputs_used):
            print(f"\nInput: '{user_input}'")
            if j < len(output_lines):
                print("Printed output:")
                print(output_lines[j])

        print(f"Returned: {result}")

        if result == case["expected_return"]:
            print(f"✔ Test {i}: Return value correct")
            score += 1
        else:
            print(f"❌ Test {i}: Return value incorrect (expected {case['expected_return']})")

        print("-" * 50)

test_get_player_guess()
print(f"\nPassed {score}/{total} tests")
