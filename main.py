import os

Allfiles_list = os.listdir("Allfiles/labs")
labs_list = []
for file in Allfiles_list:
    
    labs_list.append(os.listdir(f"Allfiles/labs/{file}"))
    print(labs_list)




