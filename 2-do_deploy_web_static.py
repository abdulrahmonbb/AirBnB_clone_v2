#!/usr/bin/python3
"""
This Fabric script (based on the file 1-pack_web_static.py) 
distributes an archive to the web servers
using the function do_deploy
"""
from fabric.api import *
from os.path import exists

env.hosts = ['100.25.171.73', '54.210.174.198']

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    # Check if file exists in path, return False if not
    if exists(archive_path) is False:
        return False

    # Get the file name
    filename = archive_path.split('/')[-1]

    # Remove extension from filename and build folder name
    no_ext = '/data/web_static/releases/' + filename.split('.')[0]
    
    # Create file path to tmp
    tmp = '/tmp/' + filename

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Create the folder that will contain uncompressed files
        run('mkdir -p {}'.format(no_ext))

        # Uncompress the archive to the created folder
        run('tar -xzf {} -C {}'.format(tmp, no_ext))

        # Delete the archive from the web server
        run('rm {}'.format(tmp))
        run('mv {}/web_static/* {}/'.format(no_ext, no_ext))
        run('rm -rf {}/web_static'.format(no_ext))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link on the web server linked to the new version of the code
        run('ln -s {} /data/web_static/current'.format(no_ext))
        return True
    except Exception as e:
        return False
