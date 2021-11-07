def stringify(string):
    token = '\"'
    return token + string + token

# this ensures the script when run only runs this block of code
if __name__ == "__main__":
    header = "Football Manager lnc File Editor"
    print(header)

    # Creates a new file
    newfile = open("test1.lnc", "w")
    newfile.write("# Created by " + header + "\n")
    # newfile.close()

    # "CLUB_LONG_NAME_CHANGE" 680 "Manchester United" ""

    # Menu selection
    # print("Choose your option: \n" + "1. Club Long Name\n" + "2. Club Short Name\n")
    print("Choose your option: \n" + "1. Club Long Name\n" )
    selection = input()

    # if statement - choose long name
    if selection == "1":
            clnc = stringify("CLUB_LONG_NAME_CHANGE")
            tid = input("Team ID: ")
            tmnm = stringify(input("Team Name: "))
            lang = stringify(" ")

            newfile.write(clnc + " " + tid + " " + tmnm + " " + lang)
            newfile.close()