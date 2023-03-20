import os
import shutil
import  errno, stat

cert_dir = ".\HelloWorld"
key_dir = 'ID_99'

def handleRemoveReadonly(func, path, exc):
    excvalue = exc[1]
    if excvalue.errno == errno.EACCES:
        print("Do you see me!")
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        print("I got here!")
        # os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        # func(path)
        raise

def LRWC_cleanUp(LRWC_devices: list= None) -> None:
    # Delete certificate directories
    print("\nDeleting Certificate directories..")
    try:
        shutil.rmtree('.\ID_98', ignore_errors=False, onerror=handleRemoveReadonly)
                
    except Exception as e:
        print("Error deleting files!")
        exit(e)


path = os.path.join(cert_dir, key_dir)

if not os.path.isdir(path):
    print("Key directory doesn't exist, creating..")
    os.mkdir(path)
else:
    print("Key directory exists!")

LRWC_cleanUp()


