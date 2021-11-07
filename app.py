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

    # 1. Club Long Name
    # 2. Club Short Name
    # 3. Stadium Name Change
    # 4. City Name Change
    # 5. Fake National Team
    # 6. Disable Player Pics
    # 7. Person name change

    # Menu selection
    print("Choose your option: \n" + "1. Club Long Name\n" +
          "2. Club Short Name\n" +
          "3. Stadium Name\n" +
          "4. City Name Change\n" +
          "5. Fake National Team\n" +
          "6. Disable Player Pics\n" +
          "7. Person Name Change\n")

    selection = input()

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
            stnm = stringify(input("Stadium Name: "))
            lang = stringify(" ")

            newfile.write(stnc + " " + sid + " " + stnm + " " + lang + '\n')
            newfile.close()

            # if statement - choose city name
    if selection == "4":
            ctnc = stringify("CITY_NAME_CHANGE")
            cid = input("City ID: ")
            ctnm = stringify(input("City Name: "))
            lang = stringify(" ")

            newfile.write(ctnc + " " + cid + " " + ctnm + " " + lang + '\n')
            newfile.close()

            # if statement - Fake National Team
    if selection == "5":
            fknt = stringify("FAKE_NATIONAL_TEAM")
            nid = input("Nation ID: ")
            onoff = input("On/Off (Type 1 for On, 0 for off): ")

            newfile.write(fknt + " " + nid + " " + onoff + "  " + '\n')
            newfile.close()

            # if statement - Disable Player Pics
    if selection == "6":
            dspp = stringify("DISABLE_PLAYER_PICS")
            pid = input("Person ID: ")
            onoff = input("On/Off (Type 1 for On, 0 for off): ")

            newfile.write(dspp + " " + pid + " " + onoff + "  " + '\n')
            newfile.close()

            # if statement - Person Name Changes
    if selection == "7":
            psnm = stringify("CHANGE_PLAYER_NAME")
            pid = input("Person ID: ")
            finm = stringify(input("First Name: "))
            cmnm = stringify(input("Common Name: "))
            sunm = stringify(input("Surname: "))

            newfile.write(psnm + " " + pid + " " + finm + " " + cmnm + " " + sunm + '\n')
            newfile.close()