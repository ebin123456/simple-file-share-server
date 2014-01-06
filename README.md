simple-file-share-server
========================

Simple and quick file share server

## what is simple-file-share-server?

This application creates a temporary http server to host given file.
This file is downloadable from any system within the network

## How use it?
```bash

git clone https://github.com/ebin123456/simple-file-share-server test
cd test
python main.py --file main.py
```
Now open http://localhost:8000  in your browser. You can download main.py via browser

##How stop server

Press CTRL+C

## why use this

Suppose Two system accessing internet from same router and move a large file from system 1 to system 2. Then just install this application in system 1 and run like this
```bash
python main.py --file largefile.avi
```
After running this command application will print your lan ip and server port
Let  this 192.168.1.44:8000

open http://192.168.1.44:8000  from system 2 using browser. Thats all!!!!

##Advanced options

python main.py --file largefile.avi --port 8888 --password  test_pass --downloads 2

--port argument is used to set port number
--downloads  argument is used to  limit number of download. 2 means server automatically down after 2 download(default is infinity)
-- password  argument is used to authenticate download . in above command password is test_pass. 
so user need to open http://192.168.1.44:8000/test_pass to download largefile.avi

## Install
WINDOWS
setupfile available in dist directory

Linux

```bash
sudo cp main.py /usr/bib/fserver
sudo chmod 777 /usr/bib/fserver

```

then enter

```bash
fserver --help 
```
in your terminal



