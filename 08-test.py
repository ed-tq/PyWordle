import io
import sys

score = 0
total = 4

def test_play_more():
    global score

    test_cases = [
        {
            "name": "round 1",
            "read": "words.txt",
            "rounds": 1,
            "mock_words_list": ["apple", "mango", "guava", "lemon", "peach"],
            "mock_word": "grape",
            "mock_game": (3, True),
            "expected_return": ((3, True), "grape"),
            "expected_output": """Round: 1

"""
        },
        {
            "name": "round 2",
            "read": "words.txt",
            "rounds": 2,
            "mock_words_list": ["apple", "mango", "guava", "lemon", "peach"],
            "mock_word": "melon",
            "mock_game": (6, False),
            "expected_return": ((6, False), "melon"),
            "expected_output": """Round: 2

"""
        }
    ]

    original_stdout = sys.stdout

    for case in test_cases:
        print(f"Test: {case['name']}")

        sys.stdout = io.StringIO()

        try:
            def mock_list_of_words(read):
                return case["mock_words_list"]

            def mock_get_random_word(words_list):
                return case["mock_word"]

            def mock_play_round(word):
                return case["mock_game"]

            globals()["list_of_words"] = mock_list_of_words
            globals()["get_random_word"] = mock_get_random_word
            globals()["play_round"] = mock_play_round

            result = play_more(case["read"], case["rounds"])
            output = sys.stdout.getvalue()

        except NameError as e:
            result = f"ERROR: NameError - {e}"
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

        print("Printed output:")
        print(output if output.strip() else "[no printed output]")

        if output == case["expected_output"]:
            print("✔ Printed output correct")
            score += 1
        else:
            print("❌ Printed output incorrect")

        print("-" * 60)

test_play_more()
print(f"\nPassed {score}/{total} tests")
