import mock
import pytest


from calucate_probability.main import main


@mock.patch('calucate_probability.main.process')
def test_main(process):
    """
    This function tests the main.py using pytest and the mock package.

    Args:
           process (function): the function which is the main function
           to input the parameters to calculate the probability of lose.

    """
    main(['-n', '30'])
    process(n='30')
