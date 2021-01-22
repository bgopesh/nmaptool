import nmap
from pprint import pprint

while True:
    print("""\n choose what you want to do\n
       1. Get info about your network
       2. scan network
       e. exit application\n""")
      
    userInput = input("Ente the option: ")
    
    #Handle user options
    if userInput == "1":
        mynmap = nmap.PortScanner()

        ip = input("Enter the ip address to scan: \n")

        print("This may take a couple of minutes\n")

        scan  = mynmap.scan(ip, '1-1024','-v -sS -sV -O -A -e eno1')

        print("General Info\n")

        #mac address
        mac = scan['scan'][ip]['addresses']['mac']
        print("\n Mac Address" .format(mac))
        continue

    elif userInput == "2":
         #Initializing the port scanner
         mynmap = nmap.PortScanner()
         print("\nThis may take a couple of minutes...\n")

         #Scanning the device
         scan = mynmap.scan(ports = '1-1024')
         #pprint(scan)
         for device in scan['scan']:
             print("\nPorts open on {}:".format(device))
             for port in scan['scan'][device]['tcp'].items():
                 if port[1]['state'] == 'open':
                     print("-->" + str(port[0]) + "|" + port[1]['name'])

         continue

    elif userInput == "e":
        print("Exiting Program\n")
        break
    else:
        print("Invalid input\n")
        continue


#End








