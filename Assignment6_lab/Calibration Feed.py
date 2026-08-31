calibration_feed = [
    [201, 6.0, 9.5, "IGNORE", 4.0],
    [],
    [202, 11.2, "FAULT", 7.8, 5.5],
    [203, 14.0, 3.5, 8.25],
    [204, 2.75, "HALT", 6.0]
]

feed_cursor = 0
total = 0
maximum = None
minimum = None
checksum = 0
shutdown = False


while (current_slice := calibration_feed[feed_cursor:feed_cursor + 1]):

    batch = current_slice[0]

    # Check empty batch
    if not batch:
        print("BATCH", feed_cursor, "is EMPTY. Proceeding.")
        feed_cursor += 1
        continue

    # Calibration ID
    batch_id = batch[0]

    print("Evaluating Batch", feed_cursor,
          "(ID :", batch_id, ")...")


    # Find length manually
    batch_length = 0

    for i in batch:
        batch_length += 1


    # SUM
    batch_sum = 0.0


    # Read from right to left
    for i in range(1, batch_length):

        index = batch_length - i
        reading = batch[index]


        # IGNORE
        if reading == "IGNORE":
            print("Signal IGNORE encountered at batch", batch_id)
            continue


        # FAULT
        if reading == "FAULT":
            print("Signal FAULT detected. Suppressing batch", batch_id)
            break


        # HALT
        if reading == "HALT":
            print("Signal HALT detected. Executing emergency protocol.")
            shutdown = True
            break


        # Number Reading
        if isinstance(reading, float):

            batch_sum = batch_sum + reading
            total = total + 1


            # Find maximum
            if maximum is None:
                maximum = reading

            elif reading > maximum:
                maximum = reading


            # Find minimum
            if minimum is None:
                minimum = reading

            elif reading < minimum:
                minimum = reading


    # This else belongs to the FOR loop
    else:

        if batch_id % 2 == 0:
            batch_sum = batch_sum * 1.5

        else:
            batch_sum = batch_sum * 0.8

        checksum = checksum + batch_sum


    # Stop everything if HALT found
    if shutdown:
        break

    feed_cursor += 1


# Final output
print()
print("========================================")

if shutdown:
    print("CALIBRATION COMPLETE : EMERGENCY TERMINATION")

else:
    print("CALIBRATION COMPLETE : NORMAL COMPLETION")

print("========================================")

print("Total Valid Readings Processed :", total)
print("Global Calibration Checksum :", checksum)
print("Maximum Reading Encountered :", maximum)
print("Minimum Reading Encountered :", minimum)
