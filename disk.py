import subprocess

def info_raid(self):
        create = subprocess.Popen(['hpssacli', 'ctrl', 'slot=0', 'create', 'type=ld', 'drives=1I:1:3', 'raid=0', 'stripsize='+size, 'ssdoverprovisioningoptimization=off' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create.communicate()
        print(stdout)
        print(create)

def del_rais(self):
        delete = subprocess.Popen(['hpssacli', 'controller', 'slot=0', 'array', 'B', 'delete', 'forced' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = delete.communicate()
        print(stdout) 

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
