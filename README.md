# Packaging Lab 
#### Raspberry PI Camera Monitoring

## Device Setup

In `File Manager > Edit > Preferences` click `Open files with one click`

Open Terminal
1) clone this repo `git clone https://github.com/lukaskf/packaging-lab.git`
2) move into repo `cd packaging-lab`
3) run install script `sh setup.sh`

## Dev
Clone this repo to /home/packaging 
where username and password are both "packaging"

get IP address for ssh
`hostname -I`

allow ssh
`sudo raspi-config`

copy files 
`scp -r ~/pathto/packaging-lab RASPI-IP-ADDRESS:/home/packaging/

run install script in /packaging-lab
`sh setup.sh`

## Run main program

run program
`python3 camera.py`

`chmod +x camera.desktop`
