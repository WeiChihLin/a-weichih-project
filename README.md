# a-weichih-project

Author: WeiChihLin, albearo

This project is an example of calculating the probability of loss for toss n time coins.

## Getting Started
Clone this repo and its modules by running.
```
https://github.com/WeiChihLin/a-weichih-project.git
```

### Prerequisites
The framework has been developed and tested under Ubuntu 18.04. The requirement packages are as the following.
Requirements:
* python 3.7.11
* scipy  1.5.2
* mock   4.0.3
* numpy  1.19.1
* pytest 6.1.1
* python-dot 0.19.0

This project has been build by the anaconda. Please use the anaconda to build the environment with requirement.txt to run this project.
You can refer the following steps in the website to install the anaconda.
'''
https://conda.io/projects/conda/en/latest/user-guide/install/index.html
'''


### Installing

Install Requriements

Create a python 3.7 environment, eg:
```
codna create -n probability_env python=3.7
conda activate probability_env
```

Install other requirements with conda.
```
cd a-weichih-project
conda install --file requirement.txt
```
The main file locates at calcuate_probability. The function can execute as the following command.
```
python main.py
```
The default parameter n is setting as 30 in .env file.
n is the times toss the coins and the output is the probability of loss.

## Running the tests

This project uses the pytest to test the main function.
The test file locates at test/item_1 named test_this.py. This function can execute as the following command.
```
pytest tests/item_1/test_this.py
```
The coding style is following  REP8 in general. It uses black to format the script and uses pylint to check the script.


## Authors

* **WeiChihLin*  [WeiChihLin](https://github.com/WeiChihLin)

