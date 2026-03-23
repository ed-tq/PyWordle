try:
    original = ["apple", "banana", "cherry"]
    new_list = list_of_words(original)
    if new_list == original:
        print("✅ Values match the original list")
    else:
        print("❌ Values do not match the original list")
    if new_list is not original:
        print("✅ Returned a new list (different object)")
    else:
        print("❌ Returned the original list (not a new list)")
    new_list.append("date")
    if "date" not in original:
        print("✅ Modifying new list does not change the original")
    else:
        print("❌ Modifying new list changed the original")
except NameError:
    print ("❌ Function 'list_of_words' not defined")
