#python programm to demonstrate command line arguments
import getopt.sys
#remove 1st argument from the list of command line argumens
agumentList=sys.argv[1:]
#options
options="hmo:"
#long options
long_options=["Help","My_file","Output="]
try:
    #Parsing argument
    arguments,values= getopt.getopt(argumentList,options,long_optipns)
    #checking each argument
    for currentArgument,currentValue in arguments:
if currentArgument in ("-h","--help"):
    print("Displayig Help")

    elif currentArgument in ("-m","--My_file"):
        print("Displaying file_name:",sys.argv[0])
    elif currentArgument in("-o","--Output"):
        print(("()"
