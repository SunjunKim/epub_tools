import glob
import ruamel.std.zipfile as zipfile
import re
import os.path
import os
import shutil

originalDir = 'Original'
reducedDir = 'Reduced'

files = glob.glob(originalDir+'/**/*.*', recursive='True')

fontsDict = {}


for filename in files:
    #print(filename)
    newfile = os.path.normpath(os.path.join(reducedDir, filename))
    newDir = os.path.dirname(newfile)

    if os.path.isdir(filename):
        continue

    if not os.path.exists(newDir):
        os.makedirs(newDir)
    
    print("Processing", filename)

    if filename.endswith('epub'):
        zin = zipfile.ZipFile (filename, 'r')
        zout = zipfile.ZipFile (newfile, 'w')
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            if (item.filename[-4:] != '.ttf') and (item.filename[-4:] != '.otf'):
                zout.writestr(item, buffer)
        zout.close()
        zin.close()
    else:
        shutil.copy2(filename, newfile)
    


#filename = '682000733.epub'
#zipfile.delete_from_zip_file(filename, pattern='.*.ttf')




# import subprocess
# import zipfile

# z = zipfile.ZipFile(zip_filename)

# files_to_del = filter( lambda f: f.endswith('exe'), z.namelist()]

# cmd=['zip', '-d', zip_filename] + files_to_del
# subprocess.check_call(cmd)

# # reload the modified archive
# z = zipfile.ZipFile(zip_filename)