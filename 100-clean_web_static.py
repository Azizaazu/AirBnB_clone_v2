#!/usr/bin/python3
""" deletes out-of-date archives, using the function do_clean """

from fabric.api import run, env, local
from fabric.context_managers import cd
from datetime import datetime
import os

env.hosts = ['54.237.68.111', '100.25.159.174']
env.user = "ubuntu"

def do_clean(number=0):
    """
    Delete out-of-date archives in the versions and releases folders.
    """
      number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
