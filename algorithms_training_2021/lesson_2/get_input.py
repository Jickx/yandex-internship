import os


def get_input(name):
    path = os.path.join('input', name)
    with open(path, 'r') as f:
        input_lines = f.read().strip().split('\n\n\n')
    return input_lines
