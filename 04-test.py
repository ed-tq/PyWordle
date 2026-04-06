score = 0
total = 3

original = ["apple", "mango", "guava"]

# 1 Test: Check values
try:
    new_list = list_of_words(original)
    if new_list == original:
        print("✔ Test 1: new and original list values match")
        print(f"Values match: \nOriginal: {original}\nReturned: {new_list}")
        print("\n"+ ("-" * 50)+ "\n")
        score += 1
    else:
        print("❌ Test 1: new and original list values match")
        print(f"Returned value is incorrect:\nOriginal: {original}\nReturned: {new_list}")
        print("\n"+ ("-" * 50)+ "\n")
except Exception as e:
    print(f"❌ Test 1 raised an error: {e}")
    new_list = None


# 2 Test: Check new list object
try:
    if new_list is not None:
        if new_list is not original:
            print("✔ Test 2: function returns a new list object")
            print(f"Returned new object:\nOriginal object id: {id(original)}\nReturned object id: {id(new_list)}")
            print("\n"+ ("-" * 50)+ "\n")
            score += 1
        else:
            print("❌ Test 2: function returns a new list object")
            print(f"Returned the same object:\nOriginal id: {id(original)}\nReturned id: {id(new_list)}")
            print("\n"+ ("-" * 50)+ "\n")
except Exception as e:
    print(f"❌ Test 2 raised an error: {e}")


# 3 Test: Check that modifying new list does not change original
try:
    if new_list is not None:
        new_list.append("lemon")
        if "lemon" not in original:
            print("✔ Test 3: modifying new list does not change the original")
            print(f"Original after modification: {original}")
            print(f"Returned after modification: {new_list}")
            print("\n"+ ("-" * 50)+ "\n")
            score += 1
        else:
            print("❌ Test 3: modifying new list does not change the original")
            print(f"Modifying new list changed the original:\nOriginal: {original}\nReturned: {new_list}")
            print("\n"+ ("-" * 50)+ "\n")
except Exception as e:
    print(f"❌ Test 3 raised an error: {e}")

print(f"\nPassed {score}/{total} tests")
