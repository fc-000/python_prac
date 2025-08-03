# exercises no longer bases on codedex instructions
todo = []

print("---To-do List---") # user mag-input
task = input("What would you like to add? ")
todo.append(task)
print("Task added!")

print("Here is your to-do list: ") # code para lista
for item in todo:
  print("- " + item)


choice = input("Mark as done? (yes or no) ")
if choice == "yes":
  task_done = input("Which task did you finish?")
  if task_done in todo:
    todo.remove(task_done)
    print("✓ '" + task_done + "' marked as done and removed.") # removes tasks
  else:
    print("The task is not in the list.")
if choice == "no":
  print("---To-do List---") # prints list again
  for item in todo:
    print("- " + item)

