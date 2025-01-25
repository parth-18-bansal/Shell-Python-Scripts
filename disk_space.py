import shutil
import subprocess

#Run the 'df /' command and capture its output
# output = subprocess.check_output(["df", "/"]).decode("utf-8")

# print(output)

# Process the output to extract the disk usage percentage
# for line in output.splitlines():
#     if "/" in line:  # Look for the line containing the root filesystem
#         usage = line.split()[4]  # Extract the 5th column (Use%)
#         current_usage = int(usage.replace("%", ""))  # Remove '%' and convert to integer
#         break

# print(f"Current disk usage: {current_usage}%")

usage = shutil.disk_usage("/")

print(usage)

total = usage.total
used = usage.used
free = usage.free

print(used/total)

if used/total > 0.02:
    print("WARNING: Disk usage is high")
