import os


def setup_pythonpath():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    pythonpath = os.getenv('PYTHONPATH', '')
    os.environ['PYTHONPATH'] = ':'.join([pythonpath, cur_dir])
