# Create a list
events =  ['1 січня', '2 січня', '3 січня', '4 січня', '5 січня']

# Create an alias to the list
dubl = events

# We now have two references (aliases) to the SAME list
events[0] = 42
dubl[1] = 99
print(events)
print(dubl)
