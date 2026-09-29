from lib.names import *

# scenario 1
# No participants: the line is empty.
def test_empty_list_returns_emptry_string():
    assert names([]) == ""

# scenario 2
# One participant: just their name.
# ["Bart"] => "Bart"
def test_one_name_in_list_returns_name():
    assert names(["Bart"]) == "Bart"

# scenario 3
# Two participants: joined with an ampersand.
def test_two_names_in_list_returns_names_with_ampersand():
    assert names(["Bart", "Lisa"]) == "Bart & Lisa"