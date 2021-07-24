# Given a particular react project(created using npm and not bable etc..)
# this clears all unnecessary files instead of the user having to delete the files manually.
import os

def main():
    url = get_url()
    remove_files(url)
    create_dir(url)


def get_url():
    file_name = input("Enter name of file: ")
    file_name = file_name.strip(" ")
    base_url = 'C:/Users/ACER/OneDrive/Documents/programming/Web_projects/react_projects'
    return os.path.join(base_url,file_name)

def remove_files(url):
    files = ["App.test.js","logo.svg","reportWebVitals.js","setupTests.js"]

    for i in range(len(files)):
        path = os.path.join(url,"src",files[i])
        if os.path.isfile(path):
            os.remove(path)
        else:
            print("file doesnt exist/already deleted.")
    return

def create_dir(url):
    create = input("Do you want to create a components directory? yes/no: ")

    if create == "yes":
        path = os.path.join(url,"src","Components")
        os.mkdir(path)
        return
    else:
        return




if __name__ == "__main__":
    main()
    print("File removal and directory creation complete.")
