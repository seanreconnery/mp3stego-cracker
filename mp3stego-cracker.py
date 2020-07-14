import os, sys, subprocess, time

mp3 = sys.argv[1]               # file path to the mp3
pwlist = sys.argv[2]		    # file path to a list of passwords


with open(pwlist) as pw:  # open the password list
    passlist = pw.readlines()  # read in the passwords
    cnt = 1  # set our COUNTER to the 1st position

    for pword in passlist:

        # build our command as an array of values
        comm = ['decode', '-X', '-P', pword, mp3]

        # output the progress to our user
        print("Try # {}: Password:  {} \n".format(cnt, pword))

        # run our command and pipe the output back to a tuple we'll call RESULT and ERROR
        procs = subprocess.Popen(comm, stdout=subprocess.PIPE)
        result, error = procs.communicate()

        if str(error).find("unexpected end") > 1:
            # print("wrong password.")
            cnt += 1  # increase the counter
            print(cnt)

        elif str(result).find("is finished") > 0:
            # holy crap, we found something!!
            if os.path.isfile(mp3):
                print("")
                print("------- !!!FOUND PASSWORD!!! -------")
                print("")
                print("Password:   [  " + str(pword).strip() + "  ]")
                print("Try # " + str(cnt))
                print("")

                break

        elif str(result).find("ERROR") > 1:
            # print("wrong password.")
            cnt += 1  # increase the counter

        elif str(error).find("ERROR") > 1:
            cnt += 1

        else:
            cnt += 1

        time.sleep(0.3301)

print("------- CRACKING COMPLETE -------")
