import sys
import os


dir_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
dir_path_abs = os.path.abspath(dir_path)
sys.path.append(dir_path_abs)