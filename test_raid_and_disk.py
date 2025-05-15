import subprocess, os
from pathlib import Path
from typing import Callable
import time

#Динамические параметры конфига
block = [4, 8, 4096]
queue = [1, 32,128]
threads = [1, 4]
test_type = ['read', 'randread', 'write', 'randwrite' ]

#Статические параметры конфига
stactic_param = "\nruntime=10 \ndirect=1 \nfilename=/mnt/pve/test/write \nioengine=libaio \nsize=1G"

# Диретктории и параметры файлов
format_file ='json'
out_dir = './out'
cfg_dir = './fioconfig/'

# Параметры рейда
stripsize = ['8', '16', '32', '64', '128', '256', '512', '1024']
#Создать рейд 0 из диска с параметром страйпа и без оверпровиженинга
def cr_raid(self):
        create_raid = subprocess.Popen(['hpssacli', 'ctrl', 'slot=0', 'create', 'type=ld', 'drives=1I:1:3', 'raid=0', 'stripsize='+size, 'ssdoverprovisioningoptimization=on' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create_raid.communicate()
        print('Create Raid' + stdout)
        print(stderr)

# Создать на диске файловую систему ext4
def create_fs_ext4(self):
        create_fs = subprocess.Popen(['mkfs.ext4', '/dev/sdb' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create_fs.communicate()
        print('sucsess' + stdout)
        print(stderr)

# Создать на диске файловую систему xfs
def create_fs_xfs(self):
        create_fs = subprocess.Popen(['mkfs.xfs', '/dev/sdb' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = create_fs.communicate()
        print('sucsess' + stdout)
        print(stderr)

# Смонтировать диск
def mount_disk(self):
        mount = subprocess.Popen(['mount', '/dev/sdb', '/mnt/pve/test'])
        print('mounted to /mnt/pve/test')

# Отмонтировать диск, отчистить фс, удалить рейд.
def del_raid(self):
        umount = subprocess.Popen(['umount', '/dev/sdb', '/mnt/pve/test'])
        print('umounted to /mnt/pve/test')
        wipefs = subprocess.Popen(['wipefs', '-a', '/dev/sdb' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = wipefs.communicate()
        print('wipe fs\n' + stdout)
        print(stderr)
        delete_raid = subprocess.Popen(['hpssacli', 'controller', 'slot=0', 'array', 'B', 'delete', 'forced' ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = delete_raid.communicate()
        print('sucsess\n' + stdout)
        print(stderr) 

# Создание директорий для файлов
Path(cfg_dir).mkdir(exist_ok=True)
Path(out_dir).mkdir(exist_ok=True)

#Генерация конфигов fio
def create_files(*args): # проходим циклом по параметрам и создаем файлы сподставлением параметров в файл
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
            
        for b in block:
            open(out_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".json" ,'w+',encoding='utf-8')
            with open(cfg_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                testname = str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) 
                my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + "\nblocksize=" + str(b) + "k \niodepth=" + str(q) +"\nnumjobs=" + str(t) + stactic_param)
                my_file.close()
                
            for t in threads:
                open(out_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".json" ,'w+',encoding='utf-8')
                with open(cfg_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                    testname = str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t)     
                    my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) + " \nblocksize=" + str(b) + "k \niodepth=" +str(q) + "\nnumjobs=" + str(t) + stactic_param)
                    my_file.close()
                    
                for q in queue:
                    open(out_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".json" ,'w+',encoding='utf-8')    
                    with open(cfg_dir + str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) +".cfg",'w+',encoding='utf-8') as my_file:
                        testname = str(ty) + "_B" + str(b) + "_Q" + str(q) + "_T" + str(t) 
                        my_file.write( "[test] \nrw=" + str(ty) + "\nname=" + str(testname) +  " \nblocksize=" + str(b) + "k \niodepth=" + str(q) + "\nnumjobs=" + str(t) + stactic_param )
                        my_file.close()
    print('configs create')   
                        
# Func to create out files
def create_out_files(cfg_dir:str, out:str) : #Перебираем директорию с конфигами и на основе имени конфига создаем файл для выходных данных в json в другой директории
    for entry in os.listdir(cfg_dir):
        full_path = os.path.join(cfg_dir, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            Path(out + "/" + Path(full_path).stem + '.' + format_file).touch()
            print(out + "/" + Path(full_path).stem + '.' + format_file)

# Сравниваем имена файлов, что бы при тесте писать в выходной файл с именем конфига
def process_testing_disk(  
    dir1: str,
    dir2: str,
    processing_func: Callable[[str, str], None],
    extension_filter: tuple = None
):
 
    # Получаем списки файлов в обеих директориях
    files1 = _get_files_without_extensions(dir1, extension_filter)
    files2 = _get_files_without_extensions(dir2, extension_filter)
    
    # Находим общие имена файлов
    common_names = set(files1.keys()) & set(files2.keys())
    
    if not common_names:
        print("Нет файлов с совпадающими именами.")
        return
    
    # Передаём каждый совпадающий файл в функцию обработки
    for name in common_names:
        processing_func(files1[name], files2[name])

#Возвращает словарь {имя_без_расширения: полный_путь}
def _get_files_without_extensions(directory: str, extensions: tuple = None) -> dict:
    path = Path(directory)
    files = {}
    
    for item in path.iterdir():
        if item.is_file():
            if extensions is None or item.suffix.lower() in extensions:
                files[item.stem] = str(item.absolute())
    
    return files

#Функция тестирования диска
def fio_test(file1: str, file2: str):
        fio = subprocess.Popen(['fio', file1, '--output-format=' + str(format_file), '--output=' + file2],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
        stdout,stderr = fio.communicate()
        print("test in proccess\n" + str(stdout))
        print(str(stderr))         

# Основная программа
if __name__ == "__main__":
    # Можно указать конкретные расширения для фильтрации (None - все файлы)
    allowed_extensions = ('.cfg', '.json')  # или None
    
    start_time = time.time()
    for stripe in stripsize:
        cr_raid
        print("create raid0 with stripe " + stripe)
        create_fs_xfs
        print("create xfs jn disk")
        mount_disk
        print("Mount in /mnt/pve/test")
        create_files(queue, threads, block, test_type)
        print("Create config diles")
        out = out_dir + stripe
        Path(out).mkdir(exist_ok=True)
        print('Create dir ' + out)
        create_out_files(cfg_dir, out)
        process_testing_disk(
            dir1=cfg_dir,
            dir2=out,
            processing_func=fio_test,
            extension_filter=allowed_extensions
                         )
        del_raid
        print("delete raid0 with stripe " + stripe)

print("--- %s seconds ---" % (time.time() - start_time))