def longest_absolute_path(filesystem):
    max_abs_path_length = 0
    files_n_folders = filesystem.splitlines()
    depth = {}  # To store the length at each depth
    for item in files_n_folders:
        item_depth = item.count('\t')
        if item.find('.') == -1:
            # item is a folder
            # need not include '\t' here as it can be counted as depth of file later
            # \t is a single character
            length = len(item) - item_depth
            depth[item_depth] = length
        else:
            # item is a file
            # include item_depth ie \t so because we need to count '/' in the path
            cur_abs_path_len = len(item) + sum([depth[i] for i in range(item_depth)])
            if cur_abs_path_len > max_abs_path_length:
                max_abs_path_length = cur_abs_path_len
    return max_abs_path_length


# Driver code:
fs_list = [
    'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext',
    'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
]

for fs in fs_list:
    print(longest_absolute_path(fs))


# Explanation:
# First of all split the given string at '\n'.
# This will give a list of all the files and folders in the system

# Initialize max_abs_path_length = 0
# because if there is no file in the system then max_abs_path_length should be 0

# Depth (or level) of a file/folder can be detetrmined by the number of tabs '\t' in it.

# In the dictionary, store the depth as key and length as value for each folder
# Note: length of a folder means number of chars in its name minus numbr of '\t' in it
# Note: In python \t is a single character

# For each file, calculate its absolute path length as follows:
# cur_abs_path_len = lenth of filename include \t + sum of the length of folders at depths 0 to filedepth-1
# Note: this time we include number of \t because we counts number of '/' in absolute path length
# If cur_abs_path_len > max_abs_path_length then update max_abs_path_length
