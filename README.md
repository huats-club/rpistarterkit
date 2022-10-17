# EGL314starterkit
This repository contains the resources needed to kick start your EGL314 journey. Have fun and all the best! YWFU

## Hardware 
1. Single Board Computer: Raspberry Pi 4 Model B
2. Operating System: Raspbian Buster Full 

## Setting up the Raspberry Pi (first initial boot)
1. **Secure Shell (SSH)** into **Raspberry Pi** using **Putty**.
```
Hostname: pi@ip_address
Port: 22
Password: (student_defined)
```
2. Once logged in, **update** the **Raspberry Pi**
```
sudo apt update
sudo apt upgrade 
```
3. **Configure** Raspberry Pi
### Enabling SSH
**SSH** is a network communication protocol that enables two computers to communicate and share data.
<br>
To **enable** SSH, type the following
```
sudo raspi-config
```
Select `3 Interface Options` <br>
Select `P2 SSH` <br>
**Enable SSH**

### Enabling Virtual Network Computing (VNC)
**VNC** is a cross-platform screen sharing system that can be used to remotely control another computer. 
<br>

To **enable** VNC, type the following
```
sudo raspi-config
```
Select `3 Interface Options` <br>
Select `P3 VNC` <br>
Select  **Enable VNC**

### Enable HDMI 
