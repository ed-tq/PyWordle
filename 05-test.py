score = 0
total = 2

try:
    words = ["apple", "mango", "guava", "lemon", "peach"]

    result = get_random_word(words)
    print(f"Returned: {result}")

    if result in words:
        print("✔ Test 1: Returned word is in the list")
        score += 1
    else:
        print("❌ Test 1: Returned word is not in the list")

    results = set()
    for _ in range(10):
        results.add(get_random_word(words))

    if len(results) > 1:
        print("✔ Test 2: Function returns different words (randomness works)")
        score += 1
    else:
        print("❌ Test 2: Only one word returned in 10 tries (not random)")

except NameError as e:
    if "random" in str(e):
        print("❌ Test 1: random module not imported")
        print("❌ Test 2: random module functions do not work")
    else:
        print("❌ Test 1: Function 'get_random_word' not defined")
        print("❌ Test 2: Function could not be checked")

except TypeError:
    print("❌ Test 1: Function may not accept a list argument")
    print("❌ Test 2: Function could not be checked")

except Exception as e:
    print(f"❌ Unexpected error: {type(e).__name__} - {e}")

print(f"\nPassed {score}/{total} tests")
