# file_and_error handling exercise
sent_message = 'Hey there! This is a secret message.'

with open('./file_input-output_handling/sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('./file_input-output_handling/sent_message.txt', 'r+') as file:
  original_message = file.read

  file.seek(0)

# r+ allows reading and writing of the file

unsent_message = 'This message has been unsent.'

with open('./file_input-output_handling/sent_message.txt', 'r+') as file:
  file.truncate(len(unsent_message))

with open('./file_input-output_handling/sent_message.txt', 'w') as file:
  file.write(unsent_message)

print('Origianl message', sent_message)
print('Unsent Message:', unsent_message)

