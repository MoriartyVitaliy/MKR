from read import *
from write import *

def compare_both_files(filepath1, filepath2):
    file1 = read_file(filepath1)
    file2 = read_file(filepath2)
 
def same_files(file1, file2):
    same_content = file1.intersection(file2)
    write_file("same.txt", same_content)

def same_files(file1, file2):
    diff_content = (file1 - file2) | (file2 - file1)
    write_file("diff.txt", diff_content)