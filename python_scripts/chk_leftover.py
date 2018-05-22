



from my_module import np, os


iyr = 2000


# Get all files
with open("mod35_chk_{}.txt".format(iyr), 'r') as fin:
    tmp = fin.readlines()

files_server = [i.split(',')[0] for i in tmp]
sizes_server = [int(i.split(',')[1][:-2]) for i in tmp]


# Get downloaded files
folder_local = "/u/sciteam/smzyz/scratch/data/MODIS/MOD35/{}".format(iyr)
files_local = os.listdir(folder_local)
sizes_local = [os.path.getsize(os.path.join(folder_local, ifile)) for ifile in files_local]


# Cross check
files_new = []
for ifile, isize in zip(files_server, sizes_server):
    if (ifile in files_local):
        idx = files_local.index(ifile)
        
        if int(sizes_local[idx]) == int(isize):
            continue
        else:
            files_new.append(ifile)
    else:
        files_new.append(ifile)


# Write txt
with open('mod35_hdf_{}_left.txt'.format(iyr), 'w') as fout:
    for i in files_new:
        fout.writelines(i+'\n')
