#!/usr/bin/python3
"""
This Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import *
from os.path import exists
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    Creates and distributes archive to the web servers.
    """
    new_archive = do_pack()
    if new_archive is None:
        return False

    return do_deploy(new_archive)
