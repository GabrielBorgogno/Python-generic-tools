
import os


find_path=input(str('Type the path:'))
find_file=input(str('What do you want to find?:'))
count=0



def format_size(size):
    base=1024
    kilo=base
    mega=base ** 2
    giga=base ** 3
    tera=base ** 4
    peta=base ** 5
    if size < kilo:
        size= base
        text='B'
    elif size < mega:
        size /= kilo
        text='K'
    elif size < giga:
        size /= mega
        text='M'
    elif size < tera:
        size /= giga
        text='G'
    elif size < peta:
        size /= tera
        text='T'
    else:
        size /= peta
        text='P'
    size =round(size,2)
    return f'{size}{text}'.replace('.',',')

for root_folder,path,files in os.walk(find_path):
    for file in files:
        if find_file in file:
         try:
            count+=1
            full_path=os.path.join(root_folder,file)
            Name_file,ext_file=os.path.splitext(file)
            size=os.path.getsize(full_path)
            print('file:',file)
            print('Path:',full_path)
            print('Name:',Name_file)
            print('Extension:',ext_file)
            print('size:',format_size(size))
         except PermissionError as e:
           print('Without permission!.')
         except FileNotFoundError as e:
            print('file not found!.')
         except Exception as error:
            print('Unknown Error',e)
            print('e')
         if count <= 1 :
                print(f'{count} file Exists!')
         else:
                print(f'{count} files Exists!')
