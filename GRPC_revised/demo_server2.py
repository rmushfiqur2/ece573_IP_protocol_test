# go to the directory.....
# cd 573_Project1/src
# run.......
# python demo_server2.py


import lib
port = 8898

if __name__ == '__main__':
    lib.FileServer().start(port)

