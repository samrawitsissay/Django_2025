#  3, Write a script that logs user activity.
#      When the program runs
#      Write "User logged in" to a file called log.txt.
#      Then read the file and print the full log history.
with open("log.txt", "a") as log_file:
    log_file.write("User logged in\n")
with open("log.txt", "r") as log_file:
    log_history = log_file.read()
print("Log history:")
print(log_history)