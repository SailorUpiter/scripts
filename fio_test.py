import subprocess, os
from pathlib import Path


block = [4, 8, 4096]
queue = [1, 32,128]
threads = [1, 4]
test_type = ['read', 'randread', 'write', 'randwrite' ]
runtime = '10'
file_path = '/mnt/pve/test/write'
file_size = '1G'
stactic_param = "\nruntime=" + str(runtime) +" \ndirect=1 \nfilename=" + file_path + " \nioengine=libaio" + " \nsize=" + file_size

format_file ='json'
out_dir = '/home/ubadmin/script/out/'
cfg_dir = '/home/ubadmin/script/fioconfig/'

# Create directory for config file
Path(cfg_dir).mkdir(exist_ok=True)
Path(out_dir).mkdir(exist_ok=True)

#Func to generate FIO config files
def create_files(*args):
    b=4
    q=1
    t=1
    ty='read'
    testname = str(ty) + "_B" + str(b) + "_Q" +str(q) + "_T" + str(t)
    for ty in test_type:
        open(out_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".json" ,'w+',encoding='utf-8')
        with open(cfg_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg" ,'w+',encoding='utf-8') as my_file:
            testname = str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t)  
            my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + "\nblocksize=" + str(b) + "k \niodepth=" + str(q) + "\nnumjobs=" + str(t) + stactic_param )
            my_file.close()
            print("file add")
        for b in block:
            open(out_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".json" ,'w+',encoding='utf-8')
            with open(cfg_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                testname = str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) 
                my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + "\nblocksize=" + str(b) + "k \niodepth=" + str(q) +"\nnumjobs=" + str(t) + stactic_param)
                my_file.close()
                print("file add")
            for t in threads:
                open(out_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".json" ,'w+',encoding='utf-8')
                with open(cfg_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                    testname = str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t)     
                    my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + " \nblocksize=" + str(b) + "k \niodepth=" +str(q) + "\nnumjobs=" + str(t) + stactic_param)
                    my_file.close()
                    print("file add")
                for q in queue:
                    open(out_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".json" ,'w+',encoding='utf-8')    
                    with open(cfg_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                        testname = str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) 
                        my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) +  " \nblocksize=" + str(b) + "k \niodepth=" + str(q) + "\nnumjobs=" + str(t) + stactic_param )
                        my_file.close()
                        print("file add")


def fio_test(*args):
        fio = subprocess.Popen(['fio', str(conf), '--output-format=' + str(format_file), '--output=' + str(out_dir)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = fio.communicate()
        print('sucsess' + str(stdout))
        print('error' + str(stderr)) 

create_files()

for file in os.listdir(cfg_dir):
    filename = os.fsdecode(file)
    if filename.endswith(".cfg"):
        conf = os.path.join(cfg_dir, filename)
        fio_test(conf)
        print(os.path.join(cfg_dir, filename))
        continue


