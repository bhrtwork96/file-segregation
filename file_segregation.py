# for moving file
import shutil
# for handling paths of folder and filse
import os

# extensions 

file_folders = {
    'Documents': ['.docs', '.doc','.pdf','.xls','.xlsx','.txt'],
    'Image' : ['.jpg' , '.jpeg ', '.jfif' ,' .pjpeg ', '.pjp', '.png', '.svg','.webp'],
    'Video' : ['.mp4', '.mov','.avi','.wmv','.mkv','.flv']
}

# getting path of folder from user
folder_path = input("Enter folder path:- ")

# function for files finding and return list according extensions
def file_finder(folder_path,extension):
    return [file for file in os.listdir(folder_path) if file.endswith(extension)]

# creating folders and moving files

for folder, extensions in file_folders.items():
    # for extensions 
    for extension in extensions:
        files = file_finder(folder_path,extension)
        
        # checking folder existance
        if not os.path.exists(os.path.join(folder_path,folder)):
            os.mkdir(os.path.join(folder_path,folder))

        # moving files in folder
        for f in files:
            if f:
                print(os.path.join(folder_path,f))

                # if error
                try:
                    shutil.move(os.path.join(folder_path,f), os.path.join(folder_path,folder))
                except:
                    # file already exist
                    print(f'{f} is already exist if you want to overwirte then type y ')
                    answer = input("Type Y for yes and N for no :- ")
                    if answer.lower()=="y":
                        os.remove(os.path.join(folder_path,folder,f))
                        shutil.move(os.path.join(folder_path,f), os.path.join(folder_path,folder), copy_function=shutil.copy2)
                    elif answer.lower()=='n':
                        print(f"{f} not moved")
                    else:
                        print("Type y or n only")
        

        
    
               
        
    