__author__ = 'sapphire'
import usb
import usb.core
import usb.util
dev = usb.core.find(idVendor=0x1cbe,idProduct=0x00fd)
interface=1
if dev is None:
    print "device not find"
if dev.is_kernel_driver_active(interface):
            print "but we need to detach kernel driver"
            dev.detach_kernel_driver(interface)
            print "claiming device"
            # usb.util.claim_interface(dev, interface)
            # print "release claimed interface"
            # usb.util.release_interface(dev, interface)
dev.set_configuration()
dev.reset()
# endpoint = dev[0][(1,0)][0]
# print endpoint
# while 1:
#     try:
#         print dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
#     except Exception:
#         print "wating.."


cfg = dev.get_active_configuration()
intf = cfg[(interface,0)]
epout0 = usb.util.find_descriptor(
    cfg[(0,0)],
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)
epout1 = usb.util.find_descriptor(
    cfg[(1,0)],
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)
epout2 = usb.util.find_descriptor(
    cfg[(2,0)],
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)
epout3 = usb.util.find_descriptor(
    cfg[(3,0)],
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)
epout1.write("hello")
epout2.write("hello")
#epout0.write("hello")
#print "intf is",intf
#print "epoutt is",epout
# epint =usb.util.find_descriptor(
#     intf,
#     # match the first OUT endpoint
#     custom_match = \
#     lambda e: \
#         usb.util.endpoint_direction(e.bEndpointAddress) == \
#         usb.util.ENDPOINT_IN)
# print "epout1 is",epout1
#
# while 1 :
#     try:
#         print epint.read(epint.wMaxPacketSize,10000)
#     except Exception:
#         pass
