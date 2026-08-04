# with open("servers.txt", "w") as f:
#     f.write("web1\n")
#     f.write("web2\n")
#     f.write("web3\n")
# print("File written")

# with open("servers.txt", "r") as f:
#     content = f.read()
# print("Here's what I read:")
# print(content)
"""
Challenge of the day

You've got a log file. Read it, and count how many lines contain the word ERROR.

First, create the log file (run this once to set it up):

python
with open("app.log", "w") as f:
    f.write("INFO: server started\n")
    f.write("ERROR: connection failed\n")
    f.write("INFO: retrying\n")
    f.write("ERROR: timeout\n")
    f.write("INFO: recovered\n")
"""
with open("app.log", "w") as f:
    f.write("INFO: server started\n")
    f.write("ERROR: connection failed\n")
    f.write("INFO: retrying\n")
    f.write("ERROR: timeout\n")
    f.write("INFO: recovered\n")

with open("app.log", "r") as f:
    error_count = 0
    for line in f:
        if "ERROR" in line:
            error_count += 1
print(f"Found {error_count} error lines")

