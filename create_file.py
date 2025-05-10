block = [4, 8, 16, 64, 128, 4096]
queue = [1, 4, 8, 16, 32, 64, 128]
threads = [1, 2, 4]
test_type = ['read', 'randread', 'write', 'randwrite' ]
stactic_param = "\nruntime=20 \ndirect=1 \nfilename=/mnt/pve/test/write \nioengine=libaio"
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

#create_conf(block, threads)