"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    elif number < 10:
        conclusion = 'Number is between one and ten'
    elif number < 100:
        conclusion = 'Number is between ten and one hundred'
    else:
        conclusion = 'Number bigger than or equal to one hundred'

    assert conclusion == 'Number is between ten and one hundred'

        conclusion = 'Number bigger than or equal to one'
    if number > 10 and number < 20:
        conclusion = 'Number is between ten and twenty'
    assert conclusion == 'Number is between ten and twenty'


def test_nested_conditions():
    """Test nested if statements."""
    age = 20
    has_license = True
    conclusion = ''

    if age >= 18:
        if has_license:
            conclusion = 'Allowed to drive'
        else:
            conclusion = 'License required'
    else:
        conclusion = 'Too young'

    assert conclusion == 'Allowed to drive'



def test_multiple_elif_branches():
    """Test multiple elif branches for grade classification."""
    score = 85
    conclusion = ''

    if score >= 90:
        conclusion = 'A'
    elif score >= 80:
        conclusion = 'B'
    elif score >= 70:
        conclusion = 'C'
    elif score >= 60:
        conclusion = 'D'
    else:
        conclusion = 'F'

    assert conclusion == 'B'
