# card-counter
 
Laptop:

5. Install RealVNC viewer to remote into both RaspberryPis
6. Check you are able to connect to both Pis



Spy Controller RaspberryPi 4:

1. Put Ubuntu OS on SD card
2. Install VNC Server for remote access
	- Open Terminal
	- sudo apt update
	- sudo apt upgrade
	- Head to RealVNC to download server for Raspberry Pi
	- sudo dpkg -i [download file of RealVNC Server].deb
	- You may need to turn off gnome from startup
5. Download the source code - 
6. Edit outbound_transmission.py and change receiver_ip variable to IP of the 2nd RaspberryPi 
7. Run outbound_transmission.py
	
	

Tethered RaspberryPi 3:

3. Utilize RaspberryPi OS
4. Install VNC Server for remote access (Optional - Both raspberry Pis should be on the same WIFI network)
	- Open Terminal
	- sudo apt update
	- sudo apt upgrade
	- Head to RealVNC to download server for Raspberry Pi
	- sudo dpkg -i [download file of RealVNC Server].deb
5. Download the source code - 
6. Run receiver.py 
	- Terminal: hostname -I
	- IP 192.168.86.26
	- Port 1069
