## Installation and Setup Instructions

There are many schools of thought, for example: install tools as stand-alone on host system: Windows -or- Linux -or- Mac. 
In some of the forums Users suggest dual boot -or- install over existing system.  

There are operating systems designed for penetration testing, the one I am very familiar with is **Kali Linux** (originally *BackTrack Linux*) which is a free, open-source operating system that's designed for penetration testing, security auditing, and other information security activities.  

I installed **Kali Linux** in a Virtual Machine (VBox) environment on a i7-9750H CPU @ 2.6 GHz, 16GB RAM running Winows 11. Listed in section **Basic hardware recommendations**, are those, I think will work well, especially if you are into:
1. **Bug Bounty** programs -or-
2. running **Active Scans** on a handful of sub-domains or individual domains -or-
3. on internal CIDR (Classless Inter-Domain Routing) networks -or-
4. brute-forcing directory listings -or-
5. usernames & passwords cracking and a few others

### Basic hardware recommendations:
* 8GB RAM - you can start with 2GB -to- 4GB to try out if the host system is still working well
* 500GB SSD -to- 1TB - especially if your base system is Windows
* NVidia GPU - if password cracking 
* vbox -or- vmware - I use Oracl Virutal Box
* minimum i7  - 3.4GHz - higher number of cores is better

### Steps to install Kali Linux
1. Download for Windows Oracle [Virutal Box](https://www.virtualbox.org/wiki/Downloads)
2. Download Kali Linux [Virtual Machine image](https://www.kali.org/get-kali/#kali-platforms) for Virutal Box and unpack zip file  
3. Install Virutal Box, after installation setup up Network - select *Host-only Networks*  
   a. In *Adapter* TAB -> select *Configure Adapter Manually*  
   b. In *IPv4 address* field enter "192.168.x.x" where *x* is a range between 1 and 255. For more information execute a Google search on what is 192.168.x.x  
   c. In the *IPv4 Network Mask* field enter 255.255.255.0 -or- the subnet range from *ipconfig* in Window command prompt  
   ![VirtualBox Host-Only Ethernet Adapter](/images/VBox-Adapter-setup.jpg)   
   d. In *DHCP Server* TAB -> select *Enable Server* and enter values in "Server Address", "Server Mask", "Lower Address Bound", and *Upper Address Bound*  
   ![VirtualBox Host-Only Ethernet Adapter](/images/VBox-DHCP-setup.jpg)   
   d. **Note:** did not set any values *NAT Networks* and *Cloud Networks* parent TABs  
4. In *Oracle VM VirtualBox Manager* select **+ Add** and select **kali-linux....vbox** image and install  
5. Select **kali-linux** -> **Settings** under this:
6. Select **System**. In this section make changes to *Motherboard* and *Processor* values. Here are the values I set:  
  ![Kali-Linux-Motherboard-setup](/images/Kali-Linux-Motherboard-setup.jpg)  
  ![Kali-Linux-Processor-setup](/images/Kali-Linux-Processor-setup.jpg)  
7. Select **Display** -> **Screen** selected *Enable 3D Acceleration* since host machine is GPU enabled, did not edit the other TABs  
   ![Kali-Linux-Display-Screen-setup](/images/Kali-Linux-Display-Screen-setup.jpg)  
8. Select **Network**. In here I setup two **Adapters**, Adpater1 attached to *NAT* and Adapter2 attached to *Host-only Adapter*. **Adapter2** setting is very important. For **Adapter1** you can set it to either NAT or *Bridged Adapter*. Adapter1 setting is used to connect to internet for downloads, updates.  
    ![Kali-Linux-Network-Adapter1-setup](/images/Kali-Linux-Network-Adapter1-setup.jpg)  
    ![Kali-Linux-NetworkAdapter2-setup](/images/Kali-Linux-Network-Adapter2-setup.jpg)  
9. If you have any folders to share from **host system** you can set in **Shared Folders** selection  
    ![Kali-Linux-Shared-Folders-setup](/images/Kali-Linux-Shared-Folders-setup.jpg)  

### Hardening base system - Kali Linux
#### DO NOT GET OWNED  
* Change hostname from **kali**
  % sudo hostnamectl set-hostname <new-host-name>  # change name of system -> old-name -to- new-host-name
  *change in /etc/hosts,  and /etc/host\* files*
* create new user and drop kali  
    % sudo adduser <new-user>  
  - add user to sudo group  
    % sudo adduser <new-user> sudo # to add *new-user* to *sudo* group  
    % edit /etc/sudoers and add *new-user* after *root* -OR-  
    % sudo usermod -a -G sudo <new-user>  
  - drop user kali  
    % sudo deluser kali sudo (remove *kali* from *sudo* group)  
  - to remove *kali* completely from system  
    % sudo gpasswd -d <user> sudo  
    % sudo deluser --remove-home <user>  
* disable NetBios (if you don't need it)  
* update & upgrade Kali Linux  
  % sudo apt update && sudo apt upgrade  
* After upgrade execute **kali-tweaks** and select *hardening* system  
  % sudo kali-tweaks  

### Creating Vulnerable VirutalBox Machines
1. [**Metasploitable2**](https://sourceforge.net/projects/metasploitable/) from *sourceforge* for VirutalBox  
2. After download setup in VirtualBox. Similar setup for OWASP BAP  
3. For **Network** -> Select *Adapter1* and *Host-only Adapter*  
  ![Vulnerable-Network-Adapter1-setup](/images/Vulnerable-Network-Adapter1-setup.jpg)  
4. For [**OWASP BWA**](https://sourceforge.net/projects/owaspbwa/) we will use all defaults that come with the VirtualBox image. For **Network** same settings as other vulnerable applications.  
5. **NOTE:** DO NOT **update _NOR_ upgrade** vulnerable applications - defeats the very purpose of crearing vulnerable applications to train oneself in penetration testing skills.  
  
### Firefox Add-ons - think similar add-ons exist for Chrome  
  - FoxyProxy  
    - https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard  
  - Wappalyzer  
    - https://addons.mozilla.org/en-US/firefox/addon/wappalyzer  
  - BuiltWith  
    - https://addons.mozilla.org/en-US/firefox/addon/built-with  

*Please let me know if anything is incorrect*  





