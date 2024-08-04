#!/usr/bin/python3
"""
This script distributes an archive to the web servers.
"""
from fabric.api import env, run, put
from os.path import exists

env.hosts = ['100.25.171.73', '54.210.174.198']

def do_deploy(archive_path):
    """
    Uploads and uncompresses the archive on the web servers.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split('/')[-1]
        no_extention = file_name.split('.')[0]
        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}'.format(path, no_extension))
        run('tar -xzvf /tmp/{} -C {}{}/'.format(file_name, path, no_extension))
        run('rm -r /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_extension))
        run('rm -rf {}{}/web_static'.format(path, no_extension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_extension))
        return True
    except:
        return False
        
