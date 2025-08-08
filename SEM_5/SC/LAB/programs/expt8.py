def get_fuzzy_set(name):
    fuzzy_set = {}
    print(f"Enter elements and their membership degrees for {name} (format: element degree). Type 'done' to finish:")
    while True:
        user_input = input()
        if user_input.lower() == "done":
            break
        element, degree = user_input.split()
        fuzzy_set[element] = float(degree)
    return fuzzy_set

def complement(fuzzy_set):
    return {x: 1 - degree for x, degree in fuzzy_set.items()}

def union(set1, set2):
    return {x: max(set1.get(x, 0), set2.get(x, 0)) for x in set(set1) | set(set2)}

def intersection(set1, set2):
    return {x: min(set1.get(x, 0), set2.get(x, 0)) for x in set(set1) & set(set2)}

fuzzy_A = get_fuzzy_set("Fuzzy Set A")
fuzzy_B = get_fuzzy_set("Fuzzy Set B")

complement_A = complement(fuzzy_A)
union_AB = union(fuzzy_A, fuzzy_B)
intersection_AB = intersection(fuzzy_A, fuzzy_B)

print("\nComplement of Fuzzy Set A:", complement_A)
print("Union of Fuzzy Set A and B:", union_AB)
print("Intersection of Fuzzy Set A and B:", intersection_AB)
