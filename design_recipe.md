## 1 problem - user story
```
As a member of a group chat,
I want the chat's participants shown as a single readable line,
so that I can see at a glance who's in the conversation.
```

```
Acceptance criteria:

No participants: the line is empty.
[] => ""

One participant: just their name.
["Bart"] => "Bart"

Two participants: joined with an ampersand.
["Bart", "Lisa"] => "Bart & Lisa"

Three or more participants: commas between names, with an ampersand before the last one.
["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"

Order is kept: names appear in the same order they were given.
```
## 2 function signature
```python
# Parameters:
# - participants, list eg. ["Bart", "Lisa"]
# Return type:
# - string, eg. "Bart & Lisa"
# Side Effects:
# - 
def names(participants):
    pass
```

## 3 exampples
```python
# scenario 1
# No participants: the line is empty.
assert names([]) => ""

# scenario 2
# One participant: just their name.
# ["Bart"] => "Bart"
assert ["Bart"] => "Bart"

# scenario 3
# Two participants: joined with an ampersand.
assert ["Bart", "Lisa"] => "Bart & Lisa"

# scenario 4
# Three or more participants: commas between names, with an ampersand before the last one.
assert ["Bart", "Lisa", "Maggie"] => "Bart, Lisa & Maggie"
```