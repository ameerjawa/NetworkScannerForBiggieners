import threading
from Getipaddress import *
from Saveinfile import *



def get_ipaddress():
    ip = os.popen("ipconfig")
    for line in ip.readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start + 2:end]
    return output


class Activehosts(object):


    ### function that show the active hosts on your lan network
    @staticmethod
    def showalivedevices():
        clients = []
        threads = []
        ip = get_ipaddress()
        network = ip[:ip.rfind(".") + 1]
        for item in range(1, 30):
            test = network + str(item)
            t = threading.Thread(target=Activehosts.scanner, args=(test, clients,))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()
        Saveinfile.saveresult(clients)
        return clients

    ############

    # helper for showalivedevices function
    def scanner(ipaddress, clients):

        result = os.popen("ping {0} -n 1 ".format(ipaddress)).read()
        if "TTL" in result:

            clients.append(ipaddress)
