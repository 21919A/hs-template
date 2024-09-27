#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from high_stakes.events import *

config_open_log()


def driver_function():
    pass


def autonomous_function():
    pass


init_event_handling()

# register the competition functions
competition = Competition(driver_function, autonomous_function)
