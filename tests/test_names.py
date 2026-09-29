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

# scenario 4
# Three or more participants: commas between names, with an ampersand before the last one.
def test_three_names_ampersand_between_last_two_names():
    assert names(["Bart", "Lisa", "Maggie"]) == "Bart, Lisa & Maggie"

# scenario 5
# Four or more participants: commas between names, with an ampersand before the last one.
def test_more_than_three_names_comma_between_names_ampersand_between_last_2():
    assert names(["Homer", "Bart", "Lisa", "Maggie"]) == "Homer, Bart, Lisa & Maggie"