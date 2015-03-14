__author__ = 'sapphire'
import usb
dev = usb.core.find(idVendor=0x1cbe,idProduct=0x00fd)
print dev