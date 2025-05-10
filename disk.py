import subprocess

def cr_raid(self):
        create_raid = subprocess.Popen(['hpssacli', 'ctrl', 'slot=0', 'create', 'type=ld', 'drives=1I:1:3', 'raid=0', 'stripsize='+size, 'ssdoverprovisioningoptimization=off' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create_raid.communicate()
        print('sucsess' + stdout)
        print('error' + stderr)

def del_raid(self):
        delete_raid = subprocess.Popen(['hpssacli', 'controller', 'slot=0', 'array', 'B', 'delete', 'forced' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = delete_raid.communicate()
        print('sucsess' + stdout)
        print('error' + stderr) 

def create_fs(self):
        create_fs = subprocess.Popen(['mkfs.ext4', '/dev/sdb' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create_fs.communicate()
        print('sucsess' + stdout)
        print('error' + stderr)

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
        print('sucsess' + stdout)
        print('error' + stderr)
