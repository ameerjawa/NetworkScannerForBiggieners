
class Saveinfile(object):

    #################
    # write in result.txt from client list
    #############

      def saveresult(clients):
          for client in clients:
            fd = open("result.txt", "a")
            fd.write("\n Host-> {0}\n".format(client))
            fd.close()

    #################
    # write in result.txt from portscanner
    #############
      def saveports(str):
        fd = open("result.txt", "a")
        fd.write("\n {0}".format(str))
        fd.close()