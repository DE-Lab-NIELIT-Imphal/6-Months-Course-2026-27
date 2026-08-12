altitude_log = [10.2, 12.5, 15.0, 14.8, 13.1]

print(altitude_log)

altitude_log.append(16.3)  # add a new reading at the end
print(altitude_log)

altitude_log.insert(0, 0.0)  # insert the take-off reading at the start
print(altitude_log)

altitude_log.extend([17.0, 17.5])  # bulk-add a batch of new readings
print(altitude_log)

altitude_log.remove(13.1)  # discard one bad/misread value
print(altitude_log)

print(altitude_log.pop())  # remove & return the most recent reading
print(altitude_log)

print(altitude_log.index(15.0))  # find the position of a specific reading

print(altitude_log.count(17.0))  # how many times a reading repeats

altitude_log.sort()  # order readings ascending, in place
print(altitude_log)

altitude_log.reverse()  # replay the log backwards, in place

backup_log = altitude_log.copy()  # shallow copy - back up before clearing
print(altitude_log)
print(backup_log)
altitude_log.clear()  # wipe the log once the drone has landed
print(altitude_log)

