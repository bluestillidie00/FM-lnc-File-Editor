def stringify(string):
    token = '\"'
    return token + string + token

# this ensures the script when run only runs this block of code
if __name__ == "__main__":
    header = "Football Manager lnc File Editor"
    print(header)

    # Creates a new file
    newfile = open("test1.lnc", "a")
    # newfile.write("# Created by " + header + "\n")
    # newfile.close()

    # "CLUB_LONG_NAME_CHANGE" 680 "Manchester United" ""

    # Menu selection
    print("Choose your option: \n" + "1. Club Long Name\n" + "2. Club Short Name\n" + "3. Stadium Name")
    selection = input()

    # 1. Club Long Name
    # 2. Club Short Name
    # 3. Stadium Name Change
    # 4. City Name Change

    # if statement - choose long name
    if selection == "1":
            clnc = stringify("CLUB_LONG_NAME_CHANGE")
            tid = input("Team ID: ")
            tmnm = stringify(input("Team Name: "))
            lang = stringify(" ")

            newfile.write(clnc + " " + tid + " " + tmnm + " " + lang + '\n')
            newfile.close()

            # if statement - choose short name
    if selection == "2":
            csnc = stringify("CLUB_SHORT_NAME_CHANGE")
            tid = input("Team ID: ")
            tmnm = stringify(input("Team Name: "))
            lang = stringify(" ")

            newfile.write(csnc + " " + tid + " " + tmnm + " " + lang + '\n')
            newfile.close()

            # if statement - choose stadium name
    if selection == "3":
            stnc = stringify("STADIUM_NAME_CHANGE")
            sid = input("Stadium ID: ")
            stnm = stringify(input("Stadium Name Name: "))
            lang = stringify(" ")

            newfile.write(stnc + " " + sid + " " + stnm + " " + lang + '\n')
            newfile.close()