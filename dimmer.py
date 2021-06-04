#!/usr/bin/env python3

import argparse
from datetime import datetime, timedelta
import subprocess
from time import sleep

import keyboard

class Trigger:
    def __init__(self, timeout, trigger, reset):
        self.timeout = timeout
        self.trigger_action = trigger
        self.reset_action = reset
        self.reset()
        
    def try_triggering(self):
        if self.is_ready and datetime.now() > self.triggertime:
            self.trigger()
        
    def reset(self):
        self.triggertime = datetime.now() + \
                           timedelta(seconds=self.timeout)
        self.is_ready = True
        subprocess.run(self.reset_action, shell=True)
        return self.triggertime

    def trigger(self):
        subprocess.run(self.trigger_action, shell=True)
        self.is_ready = False


parser = argparse.ArgumentParser(
    'Trigger some action after a period of keyboard inactivity')
parser.add_argument('--timeout', '-t', default=10, type=int,
                    help='Time in seconds to wait before triggering. The default is 10.')
parser.add_argument('--trigger-action', '-a',
                    help='Program to call when triggering. Must be provided.')
parser.add_argument('--reset-action', '-r',
                    help='Program to call when the trigger is reset. Must be provided.')
args = parser.parse_args()

if not args.trigger_action:
    print("Trigger action must be provided.")
    exit(1)

if not args.reset_action:
    print("Reset action must be provided.")
    exit(2)

dimmer = Trigger(args.timeout, args.trigger_action, args.reset_action)
keyboard.on_release(lambda keyEvent: dimmer.reset())
while True:
    sleep(1)
    dimmer.try_triggering()
