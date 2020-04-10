import pickle
import bz2

# pickle a python object
dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
outfile = open('pickleOutput', 'wb')
pickle.dump(dogs_dict, outfile)
outfile.close()

# unpickle a python object
infile = open('pickleOutput', 'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print('new_dict == dogs_dict => ', new_dict == dogs_dict)
print(type(new_dict))

# compress file using bzip2
sfile = bz2.BZ2File('smallerfile', 'w')
pickle.dump(dogs_dict, sfile)