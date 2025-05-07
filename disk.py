import subprocess

def create_fs(self):
        create = subprocess.Popen(['mkfs.ext4', '/dev/sdb' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create.communicate()
        print(stdout)
        print(stderr)

def mount_disk(self):
    mount = subprocess.Popen(['mount', '/dev/sdb', '/mnt/pve/test'])
        print('mounted to /mnt/pve/test')

def umount_disk(self):
    umount = subprocess.Popen(['mount', '/dev/sdb', '/mnt/pve/test'])
        print('umounted to /mnt/pve/test')

def wipe_fs(self):
        wipefs = subprocess.Popen(['wipefs', '-a', '/dev/sdb' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = wipefs.communicate()
        print(stdout)
        print(stderr)

create_fs(1)
mount_disk(1)
umount_disk(1)
wipe_fs(1)