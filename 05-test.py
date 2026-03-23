try:
  words = ["apple", "banana", "cherry", "grape", "melon"]
  result = get_random_word(words)
  if result in words:
      print("✅ Returned word is in the list")
  else:
      print("❌ Returned word is not in the list")
  results = set()
  for i in range(10):
      results.add(get_random_word(words))
  if len(results) > 1:
      print("✅ Function returns different words (randomness works)")
  else:
      print("⚠️ Only one word returned in 10 tries (might still be random, but unlikely)")
except NameError:
    print("❌ Function 'get_random_word' not defined")
