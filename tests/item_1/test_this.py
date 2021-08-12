import mock
import pytest
import sys
import os


# Add the relative path for import the calucate_probability package
dir_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
dir_path_abs = os.path.abspath(dir_path)
sys.path.append(dir_path_abs)
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
