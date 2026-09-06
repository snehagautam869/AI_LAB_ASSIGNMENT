def shift(coords):
    coords[0] += 1
# accidental side effect on a list!
location = [28.6139, 77.2090]
shift(location)
print(location)

#tuple
gps_location = (28.6139, 77.2090)
# (latitude, longitude)
print(gps_location[0])

#sets
tags = {"ai","ml","ai","nlp","ml"}
print(tags)
empty = set() # {} - create dict not set
print(type(empty))

#sets operation
python_dev = {"prateek", "ira","rishi"}
ml_dev = {"kabir","rishi"}
print(python_dev | ml_dev) # | = union
print(python_dev & ml_dev) # & = intersection
print(python_dev - ml_dev) # - = difference

#set arithmetic without loops
common = []
for name in python_dev:
    if name in ml_dev:
        common.append(name)

print(common,type(common))
common = python_dev & ml_dev
print(common,type(common))

#speed advantage of sets - sets use hashing that give directly answer
valid_ids = {1042,5871,9723}
user_ids = 1042
if user_ids in valid_ids:
    print("acess granted")

article_1_tags = {"python", "ai", "tutorial"}
article_2_tags = {"python", "ml", "tutorial", "beginner"}
shared = article_1_tags & article_2_tags
all_tags = article_1_tags | article_2_tags
only_in_1 = article_1_tags- article_2_tags
print("Shared tags:", shared)
print("All tags", all_tags)
print("Unique to article 1:", only_in_1)

#practice questions
morning = {"tea","toast","news"}
evening = {"tea","walk","reading"}
print("activities done at both sides",morning&evening)
print("Distinct activitie " ,morning | evening)
print("Activities only done in morning " ,morning-evening)

today =(6,9,2026)
print("today date",today)
# A tuple is the right choice because the date values are fixed and should not be changed accidentally.
