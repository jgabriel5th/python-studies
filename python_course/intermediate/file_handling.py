'''
Learning file handling in Python.

Opening a file in Python:
- The file must be in the same folder.
- Python provides a built-in function named open() to open a file. It returns the file object that can be used to do several file operations later.
- Syntax to open the file: file_object = open(file_name, access_mode)

Definitions:
file_object is the variable or object that is going to accept and represent the file.
file_name is one of the parameters which will contain obviously the file name and its extension. It's possible to add the absolute path of the file.
access_mode is the way the file will be opened. There are three ways to acess the file: Read Mode, Write Mode and Append Mode.

Read Mode:
r - Read-only mode, file pointer placed at the beginning of the file, default mode.
rb - Reading only in binary format, file pointer at the beginning of the file as well.
r+ - Opens a file for reading and writing. File pointer at the beginning.
rb+ - Opens a file for reading and writing in binary format. File pointer at the beginning.

Built-in methods to read a file:
read() - Reads the content until it reaches the end of the file.
read(size) - The "size" is a passed parameter in number of bytes to be read.
readline() - Reads one single line of the file at a time.
readlines() - Reads all the lines till it reaches the end of the file.

Write Mode:
w - Write-only mode. It will overwrite the file if the file exists, if not it will create a new one for writing.
wb - The same as "w" but binary.
w+ - Quite similar to "w", however it serves for writing and reading. if the file doesn't exist, it creates a new one for reading and writing.
wb+ - Also as w+, but binary.

Built-in method to write a file:
write() - It writes any string to an open file. Python string can have binary data and not just text.
file_object.write(data) - Syntax used to write the contents to a file.

Append Mode: differently from write mode that overwrite the existing file, the append mode will continue writing the data.
a - Opens a file for appending. The file pointer is at the end of the file if the file exists, if not it creates a new one for writing.
ab - The same as "a" but binary.
a+ - Similar  to "a", but for both appending and reading. If the file doesn't exist, it creates a new one for reading and writing.
ab+ - Basically a+ but binary.

Built-in method to append:
write() - just like Write Mode.
'''

# Testing Read Mode and its methods:
archive = open("python.txt", 'r')
archive2 = open("python.txt", 'r')
archive3 = open("python.txt", 'r')
archive4 = open("python.txt", 'r')
print(archive.read())
print(archive2.read(6))
print(archive3.readline())
print(archive4.readlines())

# Testing Write Mode and its method:
archive5 = open("python2.txt", "w")
archive5.write("Python has been helping me a lot in college.")

# Testing Append Mode and its method:
archive6 = open('python2.txt', 'a')
archive6.write('\nBesides, this knowledge will help me to understand JavaScript, PHP, Dart.')

'''
Closing a file
- It is important to close the file when the file handling is finished to free up resources.
- Python automatically closes a file when the object of a file is reassigned to another file or not in use.
- However, it is a good practice to manually close a file.

The close() method:
- A built-in method provided by Python that closes the file object.
- Syntax: file_object.close()
'''

# Closing all the files I opened:
archive.close()
archive2.close()
archive3.close()
archive4.close()
archive5.close()
archive6.close()

'''
Manipulating Pointer: methods to change and check the pointer's position.
tell() - It tells the current pointer's position within the file.
seek(position, from) - seek() method changes the current file position. The "position" argument indicates the number of bytes to be moved.
The "from" argument that is not mandatory, specifies the reference position from where the bytes are going to be moved.
'''

# Testing tell():
archive = open('python.txt', 'r')
print(f'Pointer position before reading is: {archive.tell()}')
print(archive.read())
print(f'Pointer position after reading is: {archive.tell()}')

# Testing seek():
archive2 = open('python2.txt', 'r')
print(f'Pointer position is: {archive2.tell()}')
archive2.seek(5)
print(f'Pointer position after manipulating is: {archive2.tell()}')