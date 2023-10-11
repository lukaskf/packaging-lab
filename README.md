# Packaging Lab 
## Raspberry PI Camera Monitoring

## Device Setup
get IP address for ssh
`hostname -I`

allow ssh
`sudo raspi-config`

copy files 
`scp -r ~/pathto/packaging-lab RASPI-IP-ADDRESS:/home/packaging/

run install script in /packaging-lab
`sh setup.sh`

run program
`python3 camera.py`
