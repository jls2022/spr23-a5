!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

#checks that the program outputs "3" for an input of "1 - 1"
assert run("1 - 1").output == "0"
# Checks that the program fails (correctly errors) for input "1 & 2"
assert run("1 & 2").exit_status != 0


###

print("All tests passed!")
