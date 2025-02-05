#!/usr/bin/env python3


import random
import json
import string


def generate_random_json(depth=3, max_value=255, max_length=128):
    """
    Generate a reandom json
    :param depth: (int) Depth/levels
    :param max_value: (int) max number for numeric values
    :param max_length: (int) max string length
    :return:
    """
    if depth == 0:
        data_type = random.choice((0, 1, 3))
        if data_type == 1:
            return random.randint(1, max(1, max_value))  # Random integer
        elif data_type == 2:
            return random.uniform(0, 1)  # Random float
        elif data_type == 3:
            return ''.join(
                random.choice(string.ascii_lowercase) for _ in range(random.randint(3, max(3,max_length))))  # Random string
    else:
        # Generate a random JSON object with random key-value pairs
        num_keys = random.randint(1, 2)  # Random number of keys per object
        json_data = {}
        for _ in range(num_keys):
            key = ''.join(
                random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 10)))  # Random key name
            value = generate_random_json(depth=depth - 1, max_value=max_value, max_length=max_length)
            json_data[key] = value
        return json_data


# Generate random JSON data with a specified depth
random_json = generate_random_json(depth=10, max_value=256, max_length=64)

# Pretty-print the JSON
print(json.dumps(random_json, indent=2))
