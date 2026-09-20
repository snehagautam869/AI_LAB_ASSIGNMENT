# DNA Marker Finder

def search4letters(sequence, markers="ATCG")->set:
    # Find common DNA markers
    return set(sequence).intersection(set(markers))


print("----- TASK 1 -----")

print(search4letters("TGGACC", "GC"))          # Positional
print(search4letters(sequence="TGGACC",
                     markers="CG"))             # Keyword
print(search4letters("TGGACC"))               # Default


' ' ' 3.2 The Discoverey Challenge ' ' '
print("Ques -- why was dna database modified in the global scope, even though analyze sequence never returned anything?")
print("Answer -- ")


# ----- TASK 2 -----

def analyze_sequence(sequence_list, marker):
    print(f"Inside Function (Start) - ID: {id(sequence_list)} | Data: {sequence_list}")

    # Modify the existing list
    sequence_list.append(marker)

    print(f"Inside Function (End) - ID: {id(sequence_list)} | Data: {sequence_list}")


# Driver code
dna_database = ["AATCCG", "TGGCTA"]

print(f"Global Scope (Before) - ID: {id(dna_database)} | Data: {dna_database}")

analyze_sequence(dna_database, "CGAT")

print(f"Global Scope (After) - ID: {id(dna_database)} | Data: {dna_database}")


# ----- SLICE EXPERIMENT -----

dna_database = ["AATCCG", "TGGCTA"]
print(f"Global Scope (Before) - ID: {id(dna_database)} | Data:{dna_database}")

analyze_sequence(dna_database[:], "CGAT")      # Creates a new list

print(f"Global Scope (After) - ID: {id(dna_database)} | Data: {dna_database}")


# ----- BONUS: REASSIGNMENT -----

def analyze_sequence_rebind(sequence_list, marker):
    print(f" Inside (Start) - ID :{id(sequence_list)}")

    sequence_list = sequence_list + [marker]   # Creates a new list

    print(f" Inside (End) - ID :{id(sequence_list)} | Data: {sequence_list}")


# --------------------EDGE CASES ------------------------------
dna_database = ["AATCCG", "TGGCTA"]

analyze_sequence_rebind(dna_database, "CGAT")

print("Original:", id(dna_database), dna_database)
