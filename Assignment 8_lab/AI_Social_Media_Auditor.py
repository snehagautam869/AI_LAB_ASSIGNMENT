"""
AI Social Media Auditor

This program has two small parts:
1. Count words from a paragraph.
2. Compare followers from two social media platforms.

Before counting, I change words to lowercase and remove punctuation.
This makes words like "Python", "python" and "python," count as one word.

For followers:
&  means users present on both platforms
-  means users present only on one particular platform
^  means users present on exactly one of the two platforms
"""

import string


# ---------------- TASK 1: WORD COUNTER ----------------

text = """
AI is changing the world.ai is powering new tools,and AI is helping researches learn faster.THe world loves
loves AI ,and the world depends on it more each year. 
"""

word_counts = {}

for raw_word in text.split():

    # make every word lowercase and remove punctuation
    cleaned_word = raw_word.lower().strip(string.punctuation)

    if not cleaned_word:
        continue

    word_counts.setdefault(cleaned_word, 0)

    word_counts[cleaned_word] += 1


print("===== WORD FREQUENCY =====")

for word, count in word_counts.items():
    print(word, ":", count)


# ---------------- TASK 2: FOLLOWER COMPARISON ----------------

platform_a_followers = [
    "user101",
    "user102",
    "user103",
    "user104",
    "user105"
]

platform_b_followers = [
    "user103",
    "user104",
    "user106",
    "user107"
]

# Convert lists into sets
set_a = set(platform_a_followers)
set_b = set(platform_b_followers)

# Users present on both platforms
both_platforms = set_a & set_b

# Users only on Platform A
only_a = set_a - set_b

# Users only on Platform B
only_b = set_b - set_a

# Users present on exactly one platform
either_only = set_a ^ set_b


print("\n===== FOLLOWER REPORT =====")

print("Users on both platforms:", both_platforms)
print("Only Platform A:", only_a)
print("Only Platform B:", only_b)
print("Only one platform:", either_only)
