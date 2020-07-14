import os, sys, subprocess, time, shutil

mp3 = sys.argv[1]               # file path to the mp3
pwlist = sys.argv[2]		    # file path to a list of passwords

### TO DO:
##          - clean up all the .tmp & .1tmp files that MP3Stego outputs
##          - clean up the file.mp3.pcm after cracking is complete


print('''

          ~
         /:\        Thats_A_wRAPper!
        /;:.\         MP3Stego password
        \\\\;:. \         cracking wrapper
        ///;:.. \\
  __--"////;:... \\"--__   @_Luke_Slytalker
--__   "--_____--"   __--
    """--_______--"""

''')

print("Cracking started @ " + time.ctime())
print("")

with open(pwlist) as pw:  # open the password list
    passlist = pw.readlines()  # read in the passwords
    cnt = 1  # set our COUNTER to the 1st position

    for pword in passlist:

        # build our command as an array of values
        comm = ['decode', '-X', '-P', pword, mp3]

        # output the progress to our user
        print("")
        print("Try # {}: Password:  {} \n".format(cnt, pword))

        # run our command and pipe the output back to a tuple we'll call RESULT and ERROR
        procs = subprocess.Popen(comm, stdout=subprocess.PIPE)
        result, error = procs.communicate()

        #if str(error).find("unexpected end of cipher message") > 1:
        #    # print("wrong password.")
        #    cnt += 1  # increase the counter
        #    print(cnt)

        if str(result).find(" is finished") > 0 and str(result).find("The decoded PCM output file name is ") > 0:
            # holy crap, we found something!!
            if os.path.isfile(mp3 + ".txt"):
                print("")
                print("------- !!! FOUND PASSWORD !!! -------")
                print("")
                print("Password:   [  " + str(pword).strip() + "  ]    Try # " + str(cnt) )
                print("")

                shutil.copy(mp3 + '.txt', mp3[:-4] + "_" + str(pword).strip() + ".txt")
                print("     Output file re-named to:  " + mp3[:-4] + "_" + str(pword).strip() + ".txt")


        elif str(result).find("unexpected end of cipher") > 1:
            # print("wrong password.")
            cnt += 1  # increase the counter

        elif str(error).find("unexpected end of cipher") > 1:
            cnt += 1

        else:
            # wrong password
            cnt += 1

        time.sleep(0.3301)
        for tmp in os.listdir(os.curdir):
            if tmp.endswith(".tmp"):
                os.remove(tmp)
            elif tmp.endswith(".1tmp"):
                os.remove(tmp)


print("Cleaning up..")

if os.path.isfile(mp3 + ".pcm"):
    os.remove(mp3 + ".pcm")


print("Cracking completed at [ " + time.ctime() + " ]")

print("------- CRACKING COMPLETE -------")
