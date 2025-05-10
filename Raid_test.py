import subprocess, os
from create_file import create_conf
from disk import *

stripsize = ['8', '16', '32', '64', '128', '256', '512', '1024']

#generate configs
create_conf(test_type, block, threads, queue)

# Add directory to output files

for stripe in stripsize:
        cr_raid(stripe)
        create_fs()
        mount_disk()