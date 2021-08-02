import mock
import pytest
import sys
import os


sys.path.append("/home/wei-zhi/Programing Project/a-weichih-project/")
from calucate_probabiliry.main import main


@mock.patch('calucate_probabiliry.main.process')
def test_main(process):
    """
    This function tests the main.py using pytest and the mock package.

    Args:
           process (function): the function which is the main function
           to input the parameters to calculate the probability of lose.

    """
    main(['-n', '30'])
    process(n='30')
