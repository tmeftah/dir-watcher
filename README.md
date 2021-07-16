# dir-watcher
watch folder for changes and copy or move files to another distination folder.

![Alt text](/Screenshot.png?raw=true "Screenshot")

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
