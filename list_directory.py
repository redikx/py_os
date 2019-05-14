import os

def list_directories(s):

    def list_dir(dir):
        nonlocal  tab_stops
        files = os.listdir(dir)

        for file in files:
            current_dir = os.path.join(dir,file)

            if os.path.isdir(current_dir):
                print("\t"*tab_stops +"└--" + current_dir)
                tab_stops += 1
                list_dir(current_dir)
                tab_stops -= 1
            else:
                print("\t"*tab_stops + "└--"+ file)

    tab_stops = 0
    if os.path.exists(s):
        print("Directory Listing of " + s)
        list_dir(s)
    else:
        print(s + " does not exist")

list_directories("C:\Python_dev\\fs_check")