import pyclamd
import  os

cd  = pyclamd.ClamdUnixSocket()


def  scan_file ( file_path ):
    try:
        result = cd.scan_file(file_path)
        if result is None:
            print ( f'File {file_path} is safe' )
        else:
            print ( f'A virus was detected in file {file_path} : {result[file_path][ 1 ]} ' )
    except Exception as e:
            print ( f' Error scanning file {file_path} : {e} ' )



def scan_directory (directory_path):
    for root, _, files in os. walk (directory_path):
        for file in files:
            file_path = os.path. join (root, file)
            scan_file (file_path)    


directory_to_scan = '/path/to/directory' 
scan_directory(directory_to_scan)        