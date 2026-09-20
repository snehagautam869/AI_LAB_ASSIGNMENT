"""
Coding for AI - Problem Set 7
Project: The Autonomous Payload Packet Parser

Name: Sneha Gautam
Date: 14/09/2026
"""

# / makes the parameters before it positional-only.
# * makes the parameters after it keyword-only.
# Slicing creates a new list, and the comprehension builds the
# corrected values without changing the original sensor list.

def parse_payload(raw_packet: list, delimiter: str, /, *, correction_offset: int = 0) -> tuple:
    status_tokens = raw_packet[2].split(delimiter)

    corrected_sensors = [
        value if "ERROR" in status_tokens else value + correction_offset
        for value in raw_packet[1][:]
    ]

    return raw_packet[0], corrected_sensors


raw_packet1 = [501, [12.5, 13.0, 11.8], "NOMINAL|CALIBRATED"]
result1 = parse_payload(raw_packet1, "|", correction_offset=2)

print("Test 1 ->", result1[0], result1[1])

assert raw_packet1[1] == [12.5, 13.0, 11.8]
assert id(result1[1]) != id(raw_packet1[1])

print("Test 1 side-effect assertions passed.")


raw_packet2 = [502, [9.0, 8.5], "ERROR|SENSOR FAULT"]
result2 = parse_payload(raw_packet2, "|", correction_offset=5)

print("Test 2 ->", result2[0], result2[1])

assert raw_packet2[1] == [9.0, 8.5]
assert id(result2[1]) != id(raw_packet2[1])

print("Test 2 side-effect assertions passed.")


raw_packet3 = [503, [1.0, 2.0], "NOMINAL"]
result3 = parse_payload(raw_packet3, "|")

print("Test 3 (default offset) ->", result3[0], result3[1])


try:
    parse_payload(raw_packet1, delimiter="|")
except TypeError as e:
    print("Test 4 passed. TypeError raised as expected:", e)


try:
    parse_payload(raw_packet1, "|", 2)
except TypeError as e:
    print("Test 5 passed. TypeError raised as expected:", e)


raw_packet4 = [504, [], "NOMINAL"]
result4 = parse_payload(raw_packet4, "|", correction_offset=5)

print("Test 6 ->", result4[0], result4[1])

assert result4[1] == []
assert id(result4[1]) != id(raw_packet4[1])

# ============================================================
# EDGE CASE 1: Multiple status codes
# ============================================================

raw_packet_4 = [504, [10.0, 20.0, 30.0], "NOMINAL|CALIBRATED|LOW POWER"]

result_4 = parse_payload(raw_packet_4, "|", correction_offset=3)

assert result_4 == (504, [13.0, 23.0, 33.0])

print("Edge Case 1 passed:", result_4)


# ============================================================
# EDGE CASE 2: Empty sensor list
# ============================================================

raw_packet_5 = [505, [], "NOMINAL"]

result_5 = parse_payload(raw_packet_5, "|", correction_offset=10)

assert result_5 == (505, [])

print("Edge Case 2 passed:", result_5)


# ============================================================
# EDGE CASE 3: Explicit 0 vs omitted offset
# ============================================================

raw_packet_6 = [506, [5.0, 6.0], "NOMINAL"]

result_6a = parse_payload(raw_packet_6, "|")
result_6b = parse_payload(raw_packet_6, "|", correction_offset=0)

assert result_6a == result_6b

print("Edge Case 3 passed:", result_6a)


print("\nAll tests passed successfully!")


