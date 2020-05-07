QA1=[["1. Which command is used to move to the system state defined by ‘graphical.target’?","a. stopx","b. systemctl isolate graphical.target","c. systemctl isolate multi-user.target","d. systemctl start graphical.target","e. systemctl stop multi-user.target","b"],
    ["2. Which of the following process is considered the first, or root, process on CentOS:","a. start","b. systemd","c. rootd","d. syslogd","e. SysVinit","b"],
    ["3. What command can you use to list what units must be started before the GUI can be started?","a. systemctl show-dependencies multi-user.target","b. systemctl show-dependencies graphical.target","c. systemctl list-dependencies multi-user.target","d. systemctl list-dependencies graphical.target","e. systemctl isolate multi-user.target","d"],
    ["4. Which command is used to view systemd logs?","a. logctl","b. systemctl show-log","c. cat /var/log/messages","d. journalctl","e. dmesg","d"],
    ["5. What is the absolute path of the file to be used to change GRUB2 configuration?","a. /etc/grub2.cfg","b. /etc/mtab","c. /etc/os-release","d. /etc/fstab","e. /etc/default/grub","e"],
    ["6. Which directory contains the files needed to boot the system","a. /var","b. /etc","c. /opt","d. /run","e. /boot","e"],
    ["7. Which command can be used to view only kernel log messages?","a. dmesg","b. kmesg","c. logger","d. logmsg","e. journald","a"],
    ["8. Issuing the following command will ensure that the “cupsd” service starts when the machine boots up.","a. systemctl start cupsd.service","b. systemctl enable cupsd.service","c. on-startup yes cupsd.service","d. chkconfig cupsd.service","e. None of the above, you must edit a configuration file","b"],
    ["9. What is the Linux Kernel?","a. The heart of the operating system","b. Code responsible for allocating hardware resources","c. Code responsible for low-level scheduling","d. All of the above","e. None of the above","d"],
    ["10. What command can you use to generate the configuration file for GRUB2?","a. mkconfig","b. grub-install","c. boot-config","d. grub2-install","e. grub2-mkconfig","e"],
    ]

QA2=[["1. Which of the following files would be the network configuration file for the `wlp0s20u14` network interface?","a. ifdown-wlp0s20u14","b.wlp0s20u14.lease","c. ifup-wlp0s20u14","d. /etc/wlp0s20u14","e. ifcfg-wlp0s20u14","e"],
     ["2. Which of these files, if created, prevents login by non-root users?","a. /sbin/nologin","b. /etc/issue","c. /etc/nologin","d. /etc/passwd","e. /etc/motd","c"],
     ["3. Which of these utilities will display the message 'This account is currently not available'","a. userdel","b. nologin","c. issue","d. motd","e. passwd","b"],
     ["4. Which of these utilities can help you discover all the network hops between the system you are on and a destination host on the Internet?","a. tracepath","b. ifconfig","c. route","d. ping","e. ip","a"],
     ["5. Which directory would a configuration file named ‘ifcfg-eno777365’ be stored in?","a. /etc","b. /etc/sysconfig/network-scripts","c. /sys","d. /run","e. /etc/NetworkManager","b"],
     ["6. A new home directory is populated with the contents of ___________ .","a. /etc/skel","b. /etc/home","c. /home","d. ~","e. /skel","a"],
     ["7. Which of the following commands will assign a static IP address to an interface called 'eno16777736':","a. addr 192.168.0.5/24 dev eno16777736","b. ip addr add 192.168.0.5/24 dev eno16777736","c. ip add 192.168.0.5/24 dev eno16777736","d. ip a set 192.168.0.5/24 dev eno16777736","e. None of the above","b"],
     ["8. What would running the command 'ip addr' do?","a. Shows addresses assigned to all active network interfaces","b. Show the current machine ip address","c. The command will fail because it is missing parameters","d. Assign a static IP on a network interface","e. None of the above","a"],
     ["9. What is the full command to change your network interface 'eno16777736' to the IP address '10.5.4.100' with subnet mask of '/26' ?","a. ip addr add 10.5.4.100 255.255.255.128 dev eno16777736","b. ip addr 10.5.4.100/26 dev eno16777736","c. ip addr add 10.5.4.100/26 dev eno16777736","d. ip add 10.5.4.100/26 dev eno16777736","e. ip addr add 10.5.4.100 255.255.255.192 dev eno16777736","c"],
     ["10. Which utility could you use to find the IP address associated with the web server www.algonquincollege.com?","a. route","b. ss","c. ip","d. ipcalc","e. dig","e"]
     ]

QA3=[["1. Which of these files, if created, prevents login by non-root users?","a. /sbin/nologin","b. /etc/issue","c. /etc/motd","d. /etc/passwd","e. /etc/nologin"],
     ["2. Which command can you use to add a group manually?","a. groupadd","b. /etc/group","c. usermod","d. addgr","e. gpasswd","d"],
     ["3. A new home directory is populated with the contents of ___________ .","a. /etc/skel","b. /etc/home","c. /home","d. ~ ","e. /skel","a"],
     ["4. What are the default permissions for a file created with the 'user' account?","a. read and write for non-root accounts read and write for the 'user' account and accounts in the 'user' group, but readonly for other non-root accounts","b. the 'user' account and accounts in the 'user' group can read, write and execute. Other non-root accounts have no access","c. the 'user' account and accounts in the 'user' group can read, write and execute. Other non-root accounts can only read and execute the file","d. read-only for non-root accounts","e. non of the above","b"],
     ["5. Which file contains a list of shells used by different user accounts?","a. /etc/chown","b. /etc/passwd","c. /etc/chgrp","d. /etc/group","e. /etc/shadow","b"],
     ["6. Which of these utilities will display the message 'This account is currently not available.'","a. userdel","b. nologin","passwd","issue","useradd","b"],
     ["7. Which file contains a list of groups?","a. /etc/group","b. /etc/passwd","c. /etc/chgrp","d. /etc/shadow","e. /etc/chown","a"],
     ["8. What command can you use to become the root user?","a. su root","b. machinectl enable","c. chown root","d. su","e. elevate","d"],
     ["9. What file or command can be used to display a message to your users after they login?","a) /etc/motd","b) message","c) /etc/issue","d) motd command","e) none of above","a"],
     ["10. Which of these directories contains programs usable by ordinary users?","a. /sbin","b. /home","c. /usr/bin","d. /run","e. /usr/sbin","c"]
     ]

QA4=[["1. What command would you use to install a package called “tcsh” with yum?","a. yum search tcsh","b. yum install tcsh","c. yum install package=tcsh","d. yum -install tcsh","e. yum update tcsh","b"],
     ["2. Which command should you use to install and remove packages in CentOS 7?","a. yum","b. apt-get","c. tar","d. aptitude","e. wget","a"],
     ["3. Using yum, what command would you use to search name, description, and summaries for a given word?","a. yum list vim","b. yum search vim","c. yum lookup vim","d. none of the above","e. all of the above","b"],
     ["4. Using the “rpm” utility, what command would you use to display all installed packages?","a. rpm -qa","b. rpm -qi","c. rpm -ql","d. rpm --list","e. None of the above","a"],
     ["5. Running the command “rpm -e samba” will:  ","a. Expand the package called samba","b. Remove the package called samba","c. Examine the package file samba","d. Remove the package called samba as well as its dependencies","e. None of the above","b"],
     ["6. What is the result of running the command yum group install 'Administration Tools'?","a. Installation of the 'Administration Tools' package","b. Installation of all packages on the repository 'Administration Tools'","c. The package 'Administration Tools' gets flagged for installation upon next upgrade","d. Nothing","e. Installation of several packages relating to Administration Tools"],
     ["7. Which command would you give to update all installed packages using yum?","a. yum upgrade","b. yum install all","c. yum update","d. yum autoupdate=yes","e. yum go","c"],
     ["8. What is the path to the configuration file for the package manager in CentOS 7?","a. /etc/logrotate.conf","b. /etc/yum.conf","c. /etc/rsyslog.conf","d. /etc/ld.so.conf","e. /etc/mdadm.conf","b"],
     ["9. What command can you use to list all of the files in an installed package?","ls","export","rpm","menu.lst","yum"],
     ["10. What command will install a package group named 'Console Internet Tools'?","a)yum groups install 'Console Internet Tools'","b) rpm -gi 'Console Internet Tools'","c) yum install 'Console Internet Tools'","d) rpm -i 'Console Internet Tools'"],
     ]

QA5=[["1. Which of these commands would be the first one you would use if you wanted to pool several physical volumes together with the intention of making a logical volume spanning all of them?","a. pvcreate","b. vgcreate","c. lvcreate","d. lvextend","e. vgscan","b"],
     ["2. Which of the following is created by LVM?","a. /dev","b. /sys","c. /run","d. /dev/mapper","e. /proc","d"],
     ["3. Before it can be used with LVM, a hard drive partition must be formatted as ______________ .","a. a RAID array","b. ext2","c. a physical volume","d. a volume group","e. a logical volume","c"],
     ["4. Which of the following commands can be used to disable a swap partition?","a. swapmkfs","b. mkfs.swap","c. swapoff","d. swapon","d. mkswap","swapon","c"],
     ["5. Which of the following filesystems differ only in that one uses a journal and the other does not?","a. ext2, ext3","b. ext4, XFS","c. ext3, ext4","d. ext2, FAT32","e. ext3, XFS","a"],
     ["6. Which of the following commands allows you to tune the parameters of the ext3 filesystem?","a. e2fsck","b. tune2fs","c. lvextend","d. ede2fs","e. fsck","b"],
     ["7. Which of the following is a Linux file system?","a. CUSFS","b. RAID","c. LVM","d. ASUFS","e. BTRFS","e"],
     ["8. Which of these commands extracts information about an XFS filesystem?","a. xfsrestore","b. xfs_debug","c. xfsdump","d. xfs_repair","e. xfs_info","e"],
     ["9. Which of the following files is a hard drive?","a. /dev/sr0","b. /dev/sda","c. /dev/md127","d. /dev/disk","e. /dev/sr1","b"],
     ["10. Which of these commands will work only if no LVs have been configured within the VG?","a. vgscan","b. vgcreate","c. vgremove","d. vgreduce","e. vgextend","c"]
     ]

def show_questions(array_in_use):
    c=0
    d=0
    number_of_questions=len(array_in_use)
    while d<number_of_questions:
        number_of_entries=len(array_in_use[d])
        a=0
        while a<number_of_entries-1:
            print(array_in_use[d][a])
            a=a+1

        answer= input("What is your answer: ")
        if answer==array_in_use[d][number_of_entries-1]:
            print("You are correct!\n")
            c=c+1
        else:
            print("You are incorrect!")
            print("The correct answer is: ",array_in_use[d][a],"\n")
        d=d+1
    print("Your score is ",c,"/10")
    print("Congratulations! You have done the Lesson \n")

print("-----------------------------------Quiz Master-----------------------------------")
print("---------------------------------Linux Lesson 1----------------------------------")
print("---------------------------------System Logging----------------------------------\n")
show_questions(QA1)

print("-----------------------------------Quiz Master-----------------------------------")
print("---------------------------------Linux Lesson 2----------------------------------")
print("------------------------------------Networking----------------------------------\n")
show_questions(QA2)

print("-----------------------------------Quiz Master-----------------------------------")
print("---------------------------------Linux Lesson 3----------------------------------")
print("------------------------------Installing Software--------------------------------\n")
show_questions(QA3)

print("-----------------------------------Quiz Master-----------------------------------")
print("---------------------------------Linux Lesson 4----------------------------------")
print("--------------------------------Users and Groups---------------------------------\n")
show_questions(QA4)

print("-----------------------------------Quiz Master-----------------------------------")
print("---------------------------------Linux Lesson 5----------------------------------")
print("-------------------------Partitionning and File Systems--------------------------\n")
show_questions(QA5)


