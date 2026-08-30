telemetry_stream = [
    [22.5,23.0,22.8],
    [25.1,"ERR",24,9],
    [30.2,35.5,40.1],
    [22.0,22.1,"STOP"],
    ]
shutdown = False
for i in range(len(telemetry_stream)):
    batch = telemetry_stream[i]
    print(f"---Auditing batch {i} : {batch}---")

    previous_value = None

    for reading in batch:
        if reading == "STOP":
            print(f"Emergency Shutdown at Batch {batch}:")
            shutdown = True
            break
        if reading == "ERR":
            print(f"Noise ignored at{i} ,(ERR)")
            continue
        if isinstance(reading ,(int,float)):
            if reading > 35.0:
                print("Anomaly Detected at Batch",i,":",reading)
                if previous_value is not None:
                    delta = abs(reading - previous_value)
                    if delta > 5.0:
                        print(f"Spike detected at {i} :" f"{previous_value} -> {reading}  " f"Delta{delta:.1f}")
            previous_value = reading
    if shutdown:
        break
else:
    print("Audit complete: No sysytem-wide failures")
