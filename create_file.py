block = [4, 8, 16, 64, 128, 4096]
queue = [1, 4, 8, 16, 32, 64, 128]
threads = [1, 2, 4]

filename = "./fioconfig/testfile_b"

def create_conf(block, threads):
    b=4
    q=1
    t=1
    for b in block:
        with open(filename + str(b) + "_q" +str(q) + "_t" + str(t),'w+',encoding='utf-8') as my_file:
            my_file.write( "[read] \nrw=read \nname=fiotest \nblocksize=" + str(b) + "k \nfilename=/mnt/pve/test/write \nioengine=libaio \niodepth=" +str(q) + "\nnumjobs=" + str(t) + "\nruntime=60 \ndirect=1" )
            my_file.close()
        for t in threads:
            with open(filename + str(b) + "_q" +str(q) + "_t" + str(t),'w+',encoding='utf-8') as my_file:
                my_file.write( "[read] \nrw=read \nname=fiotest \nblocksize=" + str(b) + "k \nfilename=/mnt/pve/test/write \nioengine=libaio \niodepth=" +str(q) + "\nnumjobs=" + str(t) + "\nruntime=60 \ndirect=1" )
                my_file.close()
            for q in queue:
                with open(filename + str(b) + "_q" +str(q) + "_t" + str(t),'w+',encoding='utf-8') as my_file:
                    my_file.write( "[read] \nrw=read \nname=fiotest \nblocksize=" + str(b) + "k \nfilename=/mnt/pve/test/write \nioengine=libaio \niodepth=" +str(q) + "\nnumjobs=" + str(t) + "\nruntime=60 \ndirect=1" )
                    my_file.close()

create_conf(block, threads)