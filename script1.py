import subprocess

stripsize = ['8', '16', '32', '64', '128', '256', '512', '1024']

def info_raid(self):
    for size in stripsize:
        create = subprocess.Popen(['hpssacli', 'ctrl', 'slot=0', 'create', 'type=ld', 'drives=1I:1:3', 'raid=0', 'stripsize='+size, 'ssdoverprovisioningoptimization=off' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create.communicate()
        print(stdout)
        print(create)

        delete = subprocess.Popen(['hpssacli', 'controller', 'slot=0', 'array', 'B', 'delete', 'forced' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = delete.communicate()
        print(stdout)

info_raid(stripsize)