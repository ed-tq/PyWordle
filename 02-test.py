score = 0
total = 2

# Test 1: Check if 'random' module is imported
try:
    random  # checks if 'random' exists in namespace
    print("✔ Test 1: 'random' module imported")
    score += 1
except NameError:
    print("❌ Test 1: 'random' module not imported")

# Test 2: Check if any function from 'random' works
try:
    val = random.random()  # generate a float between 0 and 1
    print(f"✔ Test 2: random module works (random.random() = {val})")
    score += 1
except Exception:
    print("❌ Test 2: random module functions do not work")

print(f"\nPassed {score}/{total} tests")
