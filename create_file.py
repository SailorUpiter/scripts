import os  


block = [4, 8, 4096]
queue = [1, 32,128]
threads = [1, 4]
test_type = ['read', 'randread', 'write', 'randwrite' ]
runtime = '10'
file_path = '/mnt/pve/test/write'
file_size = '1G'
stactic_param = "\nruntime=" + str(runtime) +" \ndirect=1 \nfilename=" + file_path + " \nioengine=libaio" + " \nsize=l" + file_size
# Create directory for config file
if not os.path.isdir("fioconfig"):
     os.mkdir("fioconfig")

#Func to generate FIO config files
def create_conf(*args):
    b=4
    q=1
    t=1
    ty='read'
    filename = "./fioconfig/"
    testname = str(ty) + "_B" + str(b) + "_Q" +str(q) + "_T" + str(t)
    for ty in test_type:
        with open(filename + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg" ,'w+',encoding='utf-8') as my_file:
            my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + "\nblocksize=" + str(b) + "k \niodepth=" + str(q) + "\nnumjobs=" + str(t) + stactic_param )
            my_file.close()
            print("file add")
        for b in block:
            with open(filename + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + "\nblocksize=" + str(b) + "k \niodepth=" + str(q) +"\nnumjobs=" + str(t) + stactic_param)
                my_file.close()
                print("file add")
            for t in threads:
                with open(filename + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                    my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + " \nblocksize=" + str(b) + "k \niodepth=" +str(q) + "\nnumjobs=" + str(t) + stactic_param)
                    my_file.close()
                    print("file add")
                for q in queue:
                    with open(filename + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                        my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) +  " \nblocksize=" + str(b) + "k \niodepth=" + str(q) + "\nnumjobs=" + str(t) + stactic_param )
                        my_file.close()
                        print("file add")
