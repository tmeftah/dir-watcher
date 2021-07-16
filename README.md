# dir-watcher
watch folder for changes and copy or move files to another distination folder.

![Alt text](/Screenshot.png?raw=true "Screenshot")

# How to use
open the "conf.cfg" file and change the variable as desired.

* **timeinterval** =  how many minutes old show the file be
* **src_path** = the source path where to look for the specific file patern 
* **dist_path** = the distination folder, where files have to be moved/copied to
* **operation** = *'copy'* for copy/paste or *'move'* to cut/past

the search pattern on *src_path* are set according pathon package "glob.glob". for more infomation please see https://docs.python.org/3/library/glob.html
after you setup the conf.cfg file you can start the "app.py" file
```python
python app.py
```
or generate an executable with pyinstaller.

## copy mode
```txt
[SETTING]
timeinterval =  10
src_path = /dir_to_watch/*.txt
dist_path = /dir_to_save_to/test
operation = copy
```
## move mode
```txt
[SETTING]
timeinterval =  10
src_path = /dir_to_watch/*.txt
dist_path = /dir_to_save_to/test
operation = move
```



# Pyinstaller command
you have to install pyinstaller on your system

```python
pip install pyinstaller
```
after installion you can now generate executable of dir-watcher
```python
# -F = onefile, -c = console, -i name of icon, -n name of application
pyinstaller -F -c -i icon.ico -n Watchdir app.py 

# -D = onedir, -w = windowed, -i name of icon, -n name of application
pyinstaller -D -w -i icon.ico -n Watchdir app.py 
```
