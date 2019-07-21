# ======================================================================================================================
# Enter team members here:
# Name: Dinesh Nanda
# ID: 1893551
# Name: Ankushpreet
# ID: 1893728
# ======================================================================================================================

import pytransact


def test_is_mastercard():
    input_output = [
        ("15555",False),
        ("1575556558555555", False),
        ("5444449444844484", True),
        ("5944449444844484", False),
        ("544444944484448A", False),
        ("544444944484448a",False),
        ("",False),
        (" -// //WG", False)
    ]
    for input, expected_output in input_output:
        output = pytransact.is_mastercard(input)
        assert output == expected_output, "{} -> {} (expected: {})".format(input, output, expected_output)

    print("text_is_mastercard: OK")
    ...


def test_is_valid_expiration():
    input_output = [
        ("02/23", True),
        ("02-23", True),
        ("02 23", True),
        ("2/23", False),
        ("2 23", False),
        ("2-23", False),
        ("02/3", False),
        ("02-3", False),
        ("02 3", False),
        ("02!23",False),
        ("13/23",False),
        ("13-23",False),
        ("13 23",False),
        ("02/100",False),
        ("02-100",False),
        ("02 100",False),
        ("13/100",False),
        ("13 100",False),
        ("13-100",False)
    ]
    for input, expected_output in input_output:
        output = pytransact.is_valid_expiration(input)
        assert output == expected_output, "{} -> {} (expected: {})".format(input, output, expected_output)

    print("text_is_valid_expiration: OK")
    ...


def test_random_mastercard():
    # Generate a random list of 100 mastercard credit card numbers
    outputs = []

    for _ in range(100):
        outputs.append(pytransact.random_mastercard())

    # Assert that all cards are valid
    # Assert that cards are random

    for card in outputs:
        assert pytransact.is_mastercard(card), "Error {} is a invalid card".format(card)

    assert outputs[0]!=outputs[1], "Error: Not Random"

    ...

    print("test_random_mastercard: OK")




if __name__ == "__main__":
    test_is_mastercard()
    test_is_valid_expiration()
    test_random_mastercard()
