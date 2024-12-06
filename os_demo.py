import os
import sys


# posix   ->   Unix/Linux/macOS
# nt      ->   windows
# os2     ->   OS/2
# ce      ->   Windows CE
# jave    ->   Java platform, run in Jython
# riscos  ->   RISC OS
print("Current operation system: ", os.name)  # posix(linux)/nt(windows) 

current_work_path = os.getcwd()
print("current work path: ", os.getcwd())  

current_python_file_path = os.path.dirname(__file__)  # method 1
# current_python_file_path = os.curdir                  # method 2

# /home/fogsalary/Code/py_code/example_code
print("Current python file path: ", os.path.dirname(__file__))

current_folder_name = os.path.basename(current_python_file_path)
print("Current python file folder name: ", os.path.basename(current_python_file_path))

# /home/fogsalary/Code/py_code
current_parent_path = os.path.dirname(current_work_path)
os.chdir(current_parent_path)
print("After change directory current path: ", os.getcwd())


print(os.curdir)  # a string representing the current directory (always '.')
print(os.pardir)  # a string representing the current parent (always '..')


print("pathname separator: ", os.sep)               # '/' or '\\'
print("extension separator: ", os.extsep)           # '.'
print("alternate pathname separator: ", os.altsep)  # None or '/'
print("component separator used in $PATH: ", os.pathsep)  # ":"
print("line separator in text files: ", os.linesep)  # 'r' or '\n' or '\r\n'
print("default search path for executables: ", os.defpath)  # /bin:/usr/bin
print("file path of the null device: ", os.devnull)  # '/dev/null'