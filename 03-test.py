import builtins
import io
import sys

score = 0
total = 2
error = None

original_stdout = sys.stdout
original_input = builtins.input
captured_output = io.StringIO()

try:
    user_input = "Student"
    sys.stdout = captured_output
    builtins.input = lambda _: user_input
    test_function = get_started()
    output = captured_output.getvalue()
    expected_output = """
Welcome to Wordle 101 Student

========================================================================
                                 Rules
You have 6 guesses to figure out the solution.
All solutions are words that are 5 letters long.
Letters that have been guessed correctly are displayed in uppercase.
Letters that are in the word but have been guessed in the wrong location
are displayed in lowercase.
========================================================================

"""
except Exception as e:
    error = e
finally:
    sys.stdout = original_stdout
    builtins.input = original_input

if error is not None:
    print(f"❌ Test 1: {type(error).__name__} - {error}")
    print(f"❌ Test 2: {type(error).__name__} - {error}")
else:
    if output.strip() == expected_output.strip():
        print("✔ Test 1: Output matches expected output")
        score += 1
    else:
        print("❌ Test 1: Output does not match expected output")
        actual_lines = output.strip().splitlines()
        expected_lines = expected_output.strip().splitlines()
        max_lines = max(len(actual_lines), len(expected_lines))
        for i in range(max_lines):
            actual_line = actual_lines[i] if i < len(actual_lines) else "<missing line>"
            expected_line = expected_lines[i] if i < len(expected_lines) else "<missing line>"
            if actual_line != expected_line:
                print(f"  ❌ Line {i+1}:")
                print(f"     Got:      '{actual_line}'")
                print(f"     Expected: '{expected_line}'\n")

    if test_function == "words.txt":
        print("✔ Test 2: Return value is correct: 'words.txt'")
        score += 1
    else:
        print(f"❌ Test 2: Return value is incorrect: {test_function}")

print(f"\nPassed {score}/{total} tests")
