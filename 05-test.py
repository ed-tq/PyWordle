score = 0
total = 2
words = ["apple", "mango", "guava", "lemon", "peach"]

# Test 1: Returned word is in the list
try:
    result = get_random_word(words)
    if result in words:
        print("✔ Test 1: Returned word is in the list")
        print(f"Returned: {result}\n")
        score += 1
    else:
        print(f"❌ Test 1: Returned value is not in the list")
        print(f"Returned: {result}\n")
except Exception as e:
    print(f"❌ Test 1: {type(e).__name__} - {e}")

# Test 2: Randomness check
try:
    results = set()
    all_results = []
    for _ in range(50):
        word = get_random_word(words)
        results.add(word)
        all_results.append(word)
    if len(results) > 1:
        print("✔ Test 2: Function returns different words (randomness works)")
        score += 1
    else:
        print("❌ Test 2: Only one word returned in 50 tries (not random)")
    print("Showing 5 of 50 returns:")
    for word in all_results[:5]:
        print(f"Returned: {word}")
except Exception as e:
    print(f"❌ Test 2: {type(e).__name__} - {e}")

print(f"\nScore: {score}/{total}")
