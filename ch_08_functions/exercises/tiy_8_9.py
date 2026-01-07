# ### 8-9
# msgs = ['Hello', 'How are you?', "Nasilisiniz", "How have you been?"]

# def show_messages(msgs):
#     """Print messages."""
#     for msg in msgs:
#         print(msg)

# show_messages(msgs)

# ### 8-10, 8-11
# def send_messages(messages, sent_messages):
#     """Print messages and move to new list."""

#     while messages:
#         msg = messages.pop()
#         print(msg)
#         sent_messages.append(msg)

# msgs = ["Hello", "How are you?", "Nasilisiniz", "How have you been?"]
# sent_ms = []
# send_messages(msgs[:], sent_ms)
# print("Original list: ")
# print(msgs)
# print("New list: ")
# print(sent_ms)