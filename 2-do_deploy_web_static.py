#!/usr/bin/python3
"""
This script distributes the archive on the web servers.
"""
from fabric.api import *
from os.path import exists

# Web servers IP addresses
env.hosts = ['100.25.171.73', '54.210.174.198']


def do_deploy(archive_path):
    """
    Uploads and Uncompresses the web static archive on the
    web servers.
    """
    if exists(archive_path) is False:
        # returns false if file at archive path does not exist.
        return False

    # remove absolute path before the filename
    filename = archive_path.split('/')[-1]

    # folder to uncompress archive
    no_extension = '/data/web_static/releases/' + '{}'.format(filename.split('.')[0])

    tmp = '/tmp/' + filename

    try:
        # upload archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # create the folder to uncompress the archive
        run('mkdir -p {}'.format(no_extension))
        
        # uncompress the archive into the folder
        run('tar -xzvf {} -C {}'.format(tmp, no_extension))
        
        # deleting the archive from the web server
        run('rm {}'.format(tmp))
        run('mv {}/web_static/* {}/'.format(no_extension, no_extension))
        run('rm -rf {}/web_static/'.format(no_extension))
        
        # delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # create a new the symbolic link /data/web_static/current on the web server
        run('ln -s {}/ /data/web_static/current'.format(no_extension))
        return True
    except Exception as e:
        return False
