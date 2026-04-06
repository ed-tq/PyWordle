import builtins
import io
import sys

score = 0
total = 3

def test_play_game():
    global score

    test_cases = [
        {
            "name": "one win then stop",
            "inputs": ["N"],
            "mock_play_more_results": [
                (((2, True), "apple"))
            ],
            "expected_contains": [
                "Success! The word is apple!",
                "Summary",
                "Win percentage: 100%",
                "1|0",
                "2|#1",
                "3|0",
                "4|0",
                "5|0",
                "6|0"
            ]
        },
        {
            "name": "one loss then stop",
            "inputs": ["N"],
            "mock_play_more_results": [
                (((6, False), "grape"))
            ],
            "expected_contains": [
                "Better luck next time! The word is grape!",
                "Summary",
                "Win percentage: 0%",
                "1|0",
                "2|0",
                "3|0",
                "4|0",
                "5|0",
                "6|0"
            ]
        },
        {
            "name": "invalid input then continue then stop",
            "inputs": ["X", "Y", "N"],
            "mock_play_more_results": [
                (((1, True), "melon")),
                (((3, True), "peach"))
            ],
            "expected_contains": [
                "Success! The word is melon!",
                "Success! The word is peach!",
                "Only enter 'Y' or 'N'!",
                "Summary",
                "Win percentage: 100%",
                "1|#1",
                "2|0",
                "3|#1",
                "4|0",
                "5|0",
                "6|0"
            ]
        }
    ]

    original_input = builtins.input
    original_stdout = sys.stdout
    original_open = builtins.open

    for i, case in enumerate(test_cases, start=1):
        print(f"Test: {case['name']}")

        inputs_iter = iter(case["inputs"])
        play_more_iter = iter(case["mock_play_more_results"])

        def mock_input(prompt):
            return next(inputs_iter)

        class MockFile:
            def read(self):
                return "apple mango peach grape melon"
            def close(self):
                pass

        def mock_open(filename, mode="r"):
            return MockFile()

        def mock_play_more(read, rounds):
            return next(play_more_iter)

        builtins.input = mock_input
        builtins.open = mock_open
        globals()["play_more"] = mock_play_more
        sys.stdout = io.StringIO()

        try:
            play_game("words.txt")
            output = sys.stdout.getvalue()
        except NameError as e:
            output = f"ERROR: NameError - {e}"
        except Exception as e:
            output = f"ERROR: {type(e).__name__} - {e}"
        finally:
            builtins.input = original_input
            builtins.open = original_open
            sys.stdout = original_stdout

        passed = True
        for expected in case["expected_contains"]:
            if expected not in output:
                passed = False
                print(f"❌ Missing expected output: {expected}")

        if passed:
            print(f"✔ Test {i}: All expected output found")
            score += 1
        else:
            print(f"❌ Test {i}: Output did not match expected content")

        print("Printed output:")
        print(output.strip())
        print("-" * 60)

test_play_game()
print(f"\nPassed {score}/{total} tests")
