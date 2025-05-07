import subprocess
from create_file import create_conf
from disk import *

block = [4, 8, 16, 64, 128, 4096]
queue = [1, 4, 8, 16, 32, 64, 128]
threads = [1, 2, 4]
stripsize = ['8', '16', '32', '64', '128', '256', '512', '1024']

#generate configs
create_conf(block, threads, queue)

