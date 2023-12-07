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
    try:
        number = int(number)
        if number < 1:
            number = 1
        with cd("/data/web_static/releases/"):
            with cd(".."):
                run("ls -1t | tail -n +{} | xargs rm -rf".format(number + 1))
        with cd("/data/web_static/releases/"):
            run("ls -1t | tail -n +{} | xargs rm -rf".format(number + 1))
