# Packaging Lab 
## Raspberry PI Camera Monitoring

Clone this repo to /home/packaging 
where username and password are both "packaging"
## Device Setup
get IP address for ssh
`hostname -I`

allow ssh
`sudo raspi-config`

copy files 
`scp -r ~/pathto/packaging-lab RASPI-IP-ADDRESS:/home/packaging/

run install script in /packaging-lab
`sh setup.sh`

In `File Manager > Edit > Preferences` click `Open files with one click`

## Run main program

run program
`python3 camera.py`

## Desktop Icon

`chmod +x camera.py`

Put `camera.desktop` in desktop

`chmod +x camera.desktop`