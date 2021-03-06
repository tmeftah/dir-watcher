import os
import sys
import glob
from datetime import datetime
import time
import shutil
import configparser
import logging
import ctypes
import rsa
import subprocess


hash_key = b'c1210f11653341ab971f49e948ed3902'


logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
config = configparser.ConfigParser(allow_no_value=True)
config.read('conf.cfg')
timeinterval = int(config.get('SETTING', 'timeinterval'))
src_path = config.get('SETTING', 'src_path')
dist_path = config.get('SETTING', 'dist_path')
operation = config.get('SETTING', 'operation')


# only for windows OS
sb = subprocess.run(["wmic","csproduct", "get" ,"'UUID'"], capture_output=True, text=True)
uuid = str(sb.stdout.split()[1]) # get windows uuid

# set title of the console window
ctypes.windll.kernel32.SetConsoleTitleW("Dir-Watcher by Tarek Meftah")


try:
    with open('license.key','rb') as f:
        signature = f.read()
except:
    print('no license key found !!!!')
    sys.exit(1)


try:
    with open('public.pem','rb') as f:
        keydata = f.read()
except:
    print('no public.pem file found !!!!')
    sys.exit(1)


try:
    pubkey = rsa.PublicKey.load_pkcs1(keydata)
except :
    print('public.pem is not valid')
    sys.exit(1)

try:
    rsa.verify(uuid.encode('utf-8')+ hash_key, signature, pubkey)
except rsa.VerificationError:
    # invalid license key - refuse to start
    print(f'invalid license, please send this code {uuid}  to ...')
else:
    # start application  
    logging.info(100*'*')
    logging.info('start watching')
    logging.info(f'src_path = {src_path}')
    logging.info(f'dist_path = {dist_path}')
    logging.info(f'operation = {operation}')
    logging.info(100*'*')

    print()
    print()
    print(100* '*')
    print()
    print('      created by Tarek Meftah ')
    print('      watch folder for changes and copy or move files to another distination folder.')
    print()
    print(100* '*')
    print()
    print()
    print(f'     +    watching folder {src_path} for change ')
    while True:
        try:
            file_list = glob.glob(src_path) # get all files in scr_path folder

            for file in file_list:
                file_datetime = datetime.fromtimestamp(os.path.getctime(file))
                filename = os.path.basename(file)    
                now = datetime.now()
                diff = now - file_datetime

                if diff.seconds > timeinterval :

                    if operation == "copy":
                        file_exist = os.path.isfile(os.path.join(dist_path,filename))                    
                        if  file_exist:
                            next
                        else:
                            try:
                                shutil.copy(file,os.path.join(dist_path,filename))
                                logging.info(f'file {filename} is copied successfully')                                                       
                            except shutil.Error :
                                logging.error(f'copy file {filename} failed')
                                next

                    if operation == "move":
                        try:
                            shutil.move(file,os.path.join(dist_path,filename))
                            logging.info(f'file {filename} is moved successfully')
                        except shutil.Error:
                            logging.error(f'moving file {filename} failed')
                            next

            time.sleep(1)
        except KeyboardInterrupt:    
            confirm = input('Enter "yes" to cancel or "no" to keep running [yes/no]:').strip().lower()
            if confirm == 'yes' or confirm == "y":            
                logging.info(47* '*'+' Exit '+47* '*' +'\n')            
                break

            elif confirm == 'no' or confirm == "n":
                print("     + Keep runnning!")
                continue
            else:
                print ('    + Sorry, no valid answer...')
                continue
        except Exception as e:
             logging.error(f'error: {e.message} ')
