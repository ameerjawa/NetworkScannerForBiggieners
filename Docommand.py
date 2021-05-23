import os
class Docommand(object):
    ##########
    # function get command and execute it
    #########

    def executecommand(command):
        result = os.popen("{0}".format(command)).read()
        print(result)
