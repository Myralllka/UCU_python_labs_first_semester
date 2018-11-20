events =  ['1 січня', '2 січня', '3 січня', '4 січня', '5 січня']

# Create an alias to the list
dubl = events

# Create a different list with the same elements
new_events = ['1 січня', '2 січня', '3 січня', '4 січня', '5 січня']

# events and dubl are references (aliases) to the SAME list
# new_events is a reference to a different but EQUAL list

print("initially:")
print("  events==dubl  :", events==dubl)
print("  events==new_events  :", events==new_events)
print("  events is dubl:", events is dubl)
print("  events is new_events:", events is new_events)

# Now changes to a also change b (the SAME list) but not c (a different list)
events[0] = 2015
print("After changing events[0] to 2015")
print("  events=",events)
print("  dubl=",dubl)
print("  new_events=",new_events)
print("  events==dubl  :", events==dubl)
print("  events==new_events  :", events==new_events)
print("  events is dubl:", events is dubl)
print("  events is new_events:", events is new_events)
