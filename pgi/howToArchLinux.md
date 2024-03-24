# How To Install Arch Linux on MacSilicon

## Prerequisits

1. Go to https://archboot.com/#iso and download the ARM - aarch64 file
2. Download and install UTM with `brew install utm`

## UTM VM Initialization

1. Open UTM
2. Select **Create a new VM**
3. Select **Virtualize**
4. Select **Linux**
5. Select **Browse** and search for the _.iso_ file downloaded previsously
6. Set around 4GiB of memory
7. Set around 20GB of diskspace
8. Choose a name
9. **Create**

## VM Setup

The installation guide: https://wiki.archlinux.org/title/installation_guide#

1. Start VM
2. Select **Archboot Arch Linux AA64**
3. Hit `CTRL + c` to enter the bash promt
4. Type `loadkeys de-latin1`
5. Type `setfont Lat2-Terminus16`
6. Type `timedatectl set-ntp true`
7. Type `timedatectl set-timezone Europe/Berlin`
8. Type `fdisk -l` and identify your disk (/dev/sda, /dev/nvme0n1 or /dev/mmcblk0)
9. Type `fdisk /dev/your-identified-drive` probably `fdisk /dev/sda`

10. Press `g` to create a GPT partition
11. Press `n` to set the partition number to 1 and to set the first sector
12. Type `+512M` and press `enter` to set the last sector

13. Press `t` to config a new partition of type given
14. Press `L` to list all available types (at the bottom of this list are some aliases)
    - `gg` brings you to the top
    - `G` brings you to the bottom
    - `CTRL + u` brings you a half page up
    - `CTRL + d` brings you a half page down
    - (These are common among many programs)
15. Type `uefi` to create a UEFI partition
16. Repeat steps 11, 12

17. Press `t` to config a new partition of type given
18. Type `swap` to create a swap partition for the memory
19. Press `n` and config the partition
20. Press `enter` to default all options

21. Press `t` to config a new partition of type given
22. Type `linux` to create a swap partition for the memory
23. Press `w` to save the changes

24. Type `fdisk -l` to show the partitions
25. Type `mkfs.ext4 /dev/vda3` to initialize the root filesystem
26. Type `mkswap /dev/vda2` to initialize the swap file system
27. Type `mkfs.fat -F 32 /dev/vda1` to create the boot filesystem

28. Type `mount /dev/vda3 /mnt` to mount the root partition
29. Type `mount --mkdir /dev/vda1 /mnt/boot` to mount the boot partition
30. Type `swapon /dev/vda2` to activate the swap

31. Type `pacstrap -K /mnt base base-devel linux linux-firmware e2fsprogs dhcpcd networkmanager mkinitcpio vim neovim man-db man-pages texinfo` to install all needed packages for your system
32. Type `genfstab -U /mnt >> /mnt/etc/fstab` populate the fstab file

33. Type `arch-chroot /mnt` to change into the main system

## System settings setup

1. Type `ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime` to link the timezone
2. Type `hwclock --systohc` to set the hardwareclock
3. Type `vim /etc/locale.gen` and uncomment the `de_DE` and `en_US` utf-8 and iso lines
   - Save the file with `:wq`
4. Type `locale-gen` to generate language locales

5. Type `vim /etc/locale.conf` and write:
   - `LANG=de_DE.UTF-8`
   - Save the file with `:wq`
6. Type `vim /etc/vconsole.conf` and write:
   - `KEYMAP=mac-de-latin1` (You can find keymaps with the `localectl list-keymaps` command)
   - `FONT=Lat2-Terminus16`
   - Save the file with `:wq`
7. Type `vim /etc/hostname` and write the name of your system e.g your name (`niklas`)
8. Type `vim /etc/hosts` and write:
   - `127.0.0.1    localhost`
   - `::1          localhost`
   - `127.0.0.1    yourChosenHostname`
   - Save the file with `:wq`
9. Type `mkinitcpio -P` to build arch
10. Type `passwd` and set a password for the root user
11. Type `pacman -S grub efibootmgr` to download a bootloader
12. Type `grub-install --efi-directory=/boot --bootloader-id=GRUB` to install the bootloader
13. Type `grub-mkconfig -o /boot/grub/grub.cfg` to generate the grub configs
14. Type `exit`
15. Type `umount -R /mnt`
16. Type `poweroff`
17. Remove the installation file from the UTM VirtualMachine
18. Start the machine

## Linux setup

1. Login via `root` and your previously set password
2. Type `systemctl start NetworkManager`
3. Test network connection via ping or curl
4. Type `pacman -S neofetch` to download neofetch
5. Type `neofetch` to see your system information
   timestamp: 29:50
