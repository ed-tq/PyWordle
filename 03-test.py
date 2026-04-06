import io
import sys

score = 0
total = 2

original_stdout = sys.stdout
original_input = __builtins__.input
captured_output = io.StringIO()

try:
    user_input = "Student"
    sys.stdout = captured_output
    __builtins__.input = lambda _: user_input

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
    __builtins__.input = original_input

if 'error' in locals():
    if isinstance(error, NameError):
        print("❌ Test 1: Function 'get_started' not defined")
        print("❌ Test 2: Return value could not be checked")
    else:
        print(f"❌ Unexpected error: {type(error).__name__} - {error}")
        print("❌ Test 2: Return value could not be checked")
else:
    if output.strip() == expected_output.strip():
        print("✔ Test 1: Output matches expected output")
        score += 1
    else:
        print("❌ Test 1: Output does not match expected output")
        print("#--- Your code output: ---#\n".center(72))
        print(output.strip() + "\n")
        print("#--- Expected output: ---#\n".center(72))
        print(expected_output.strip() + "\n")

    if test_function == 'words.txt':
        print("✔ Test 2: Return value is correct: 'words.txt'")
        score += 1
    else:
        print(f"❌ Test 2: Return value is incorrect: {test_function}")

print(f"\nPassed {score}/{total} tests")
