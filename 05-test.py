try:
    words = ["apple", "mango", "peach", "grape", "melon"]

    result = get_random_word(words)
    print(f"Returned: {result}")

    if result in words:
        print("✅ Returned word is in the list")
    else:
        print("❌ Returned word is not in the list")

    results = set()
    for _ in range(10):
        results.add(get_random_word(words))

    if len(results) > 1:
        print("✅ Function returns different words (randomness works)")
    else:
        print("⚠️ Only one word returned in 10 tries (might still be random, but unlikely)")

except NameError as e:
    if "random" in str(e):
        print("❌ random module not imported")
    else:
        print("❌ Function 'get_random_word' not defined")

except TypeError:
    print("❌ Function may not accept a list argument")

except Exception as e:
    print(f"❌ Unexpected error: {type(e).__name__} - {e}")
