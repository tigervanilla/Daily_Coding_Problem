def longest_absolute_path(filesystem):
    max_path_length = 0
    files_n_folders = filesystem.splitlines()
    print(files_n_folders)
    depth = {}  # To store the length at each depth
    for item in files_n_folders:
        item_depth = item.count('\t')
        if item.find('.') == -1:
            # item is a folder
            # need not include '\t' here as it can be counted as depth of file later
            length = len(item) - item_depth
            depth[item_depth] = length
        else:
            # item is a file
            # include item_depth ie \t so because we need to count '/' in the path
            cur_len = len(item) + sum([depth[i] for i in range(item_depth)])
            if cur_len > max_path_length:
                max_path_length = cur_len
    return max_path_length


# Driver code:
fs_list = [
    'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext',
    'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
]

for fs in fs_list:
    print(longest_absolute_path(fs))
