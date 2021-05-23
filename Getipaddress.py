import os
class Getipaddress(object):

    ##############
    # method that get the ip address
    #####
    def get_ipaddress(self):
        ip = os.popen("ipconfig")
        for line in ip.readlines():
            if "IPv4 Address" in line:
                start = line.find(":")
                end = -1
                output = line[start + 2:end]
        return output