import re
import json
import pkg_resources as res

from geom2d import Point

def parse_points():
    return (
        __point_from_string(input()),
        __point_from_string(input()),
        __point_from_string(input())
    )


def __point_from_string(string: str):
    matches = re.match(r'(?P<x>-?\d+)\s(?P<y>-?\d+)', string.strip())
    if matches:
        return Point(
            int(matches.group('x')), 
            int(matches.group('y'))
        )
    else:
        raise ValueError(f"Invalid input string: {string}")
    
def read_config():
    config = res.resource_string(__name__, 'config.json')
    return json.loads(config)
    