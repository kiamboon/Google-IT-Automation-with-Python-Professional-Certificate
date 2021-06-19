'''
2.4.3 Processing Log Files
'''

"""Filtering Log Files with Regular Expressions"""
import re

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            # continue keyword tells the loop to go to the next element
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result)


# Popped up Question:
# We're using the same syslog, and we want to display the date, time, and process id that's inside /
# the square brackets. We can read each line of the syslog and pass the contents to the /
# show_time_of_pid function. Fill in the gaps to extract the date, time, and process id from the /
# passed line, and return this format: Jul 6 14:01:23 pid:29440.


def show_time_of_pid(line):
  pattern = r"^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]"
  result = re.search(pattern, line)
  return f"{result[1]} pid:{result[2]}"


print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440