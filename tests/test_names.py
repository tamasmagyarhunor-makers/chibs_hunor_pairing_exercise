from lib.names import *

# scenario 1
# No participants: the line is empty.
def test_empty_list_returns_emptry_string():
    assert names([]) == ""

def test_one_name_in_list_returns_name():
    assert names(["Bart"]) == "Bart"