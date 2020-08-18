# Managing System Files

* directory support on bootflash:, external flash memory
    + slot0:
    + usb1:/usb2:
* files can be accessed
    + bootflash:
    + volatile:
    + slot0:
    + usb1:/usb2:
* debug file system can used for debug log files specified in the __debug__ _logfile_ command
* system image files, from remote servers using FTP, SCP, SFTP, and TFTP can be downloaded


NX-OS Software consists of three images:

* kickstart image that contains linux kernal, basic drivers, and initial file system
* system image contains system software, infrastructure, and L4-7
* Erasable Programmable Logic Device (EPLD) image: EPLDs are found on the N7k currently shipping I/O modules

## Examples

> show version module 7 epld

> show version fan

> show version fan 7 epld



