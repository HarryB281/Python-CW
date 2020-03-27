def display_menu(): #A basic menu displayed using a print statement clearly stating to the user what options they can choose.
    menu = """Menu:
    1. Upload New Candidates
    2. Cast Votes
    3. Count Votes
    4. Visualise Results
    5. Exit
    6. Hackathon Task 8
    7. Hackathon Task 1"""
    print(menu)
#Function created by Harry Barnard 00106041-8.

def select_menu(): #A series of 'if' statements determining what option the user has chosen from the menu, depending on the option, the correct function is called or class is initiated.
    select = int(input("Select an option from the menu > "))
    if select == 1:
        upload = Upload("", "")
        upload.add_new_candidates()
    elif select == 2:
        voting = Voting("", "")
        voting.castvotes()
    elif select == 3:
        count = Counting("", "", "")
        count.countvotes()
    elif select == 4:
        visresult()
    elif select == 5:
        exit()
    elif select == 6:
        hack_8()
    elif select == 7:
        hack_1()
    else:
        print("Please select a valid option") #If the user enters an invalid option, they are prompted with an error message and then the function is re-called to restart the selection.
        select_menu()
#Function created by Harry Barnard 00106041-8.

def hack_1():
    print("""Positions:
    1. President
    2. Faculty
    3. GSU Officer""")
    position = int(input("Enter which position you would like to add a description for > "))
    description = input("Enter the job description > ")

    with open ("GSU_job_descriptions.txt","a+") as file:
        if position == 1:
            position = "President"
        elif position == 2:
            position = "Faculty"
        elif position == 3:
            position = "GSU Officer"
        file.write(position+","+description+"\n")
        file.close()
#Function created by Louremil Gomes Jen Choi 001086468-7 during Hackathon.

def hack_8():
    """
    This program is meant to:-
        1 - Read in the file fred.csv
        2 - Display all the records in the console.
        3 - Display just the details of the third person in the console.
        4 - Please ensure that the resulting file is fully PEP8 compliant.
        5 - Please find the logic errors as well as the syntax errors.

        =============================================================
        The output in the console should look like this:-

        1 Total Votes = 1805
        2 Total Votes = 1666
        3 Total Votes = 2432
        4 Total Votes = 2565
        5 Total Votes = 1696
        6 Total Votes = 2699
        7 Total Votes = 1330
        8 Total Votes = 2029
        9 Total Votes = 2428
        10 Total Votes = 2116
        11 Total Votes = 2144
        12 Total Votes = 1320
        =====================
        ['3', 'Lorrie', 'Nowlan', 'GSU Officer', '956', '666', '310', '500']

        Process finished with exit code 0
        =============================================================

        "A computer lets you make more mistakes faster than any invention in human
         history - with the possible exceptions of handguns and tequila." - Mitch Ratcliffe
    """

    #import os  # There was an unnecessary space between the 'o' and the 's' of os. Also, the module 'os' is not needed for this piece of code.
    import csv  # The csv module needs to be imported in order to use the'.reader' command.

    def Find_Row(row_no):
        i = 0
        # 'this_row = array()' this line is not needed since 'array()' is not required to be used anywhere else in the code.
        #'print('=====================')' This print statement creates an extra bar of '=' signs which is not needed.
        for line in fred:
            if i == row_no:  # There was a missing colon after 'row_no'.
                this_row = line
            i = i + 1
        return i

    with open('fred.csv', 'r') as file:
        fred = list(csv.reader(file))
        for row in fred:
            try:
                print(row[0], 'Total Votes =', int(row[4]) + int(row[5]) + int(row[6]) + int(row[7]))
                # In the above print statement, commas were used instead of '+' resulting in the int values not being added together.

            except ValueError:
                pass
        print('=====================')
        print(fred[
                  3])  # These two print statements were missing from the code so the third person in the file was not being displayed.

    # print(Find_Row(3)) #There was a missing bracket after the '3)'.
    Find_Row(
        3)  # if you use a print statement to call the function it returns the value of i and prints it, this is not in the desired output
#Function created by Harry Barnard 00106041-8 during Hackathon.

class Login: #Creating and initialising a class to take in the information from a text document and assign each column to variable.
    def __init__(self,name, userid, password):
        self.name = name
        self.userid = userid
        self.password = password

    def logging_in(self): #Defining a function for logging in and passing in 'self' which contains all three variables needed by the class.
        userIDinp = input ("Enter your userID > ") #User is prompted for their userID and password to login to the system.
        userpassinp = input("Enter your password > ")
        user_info = [] #A blank array is created so that the information from the text file can be stored and manipulated within the program.
        users = open("StudentVoters.txt","r") #Text file is opened in read format.
        i = 0 #initialising an incrementing count in order to create a loop of the 'if' statement below it.
        for line in users:
            if i > 0:
                self.name, self.userid, self.password = line.split(",") #For every line in the text document, split the line into the three variables defined in the class.
                if "\n" in self.password:
                    self.password = self.password[:-1] #Remove the '\n' from the end of the password, '\n' indicates a new line however it is read as part of the line.
                user_info.append([self.name, self.userid, self.password])
            i += 1 #Append the information to the empty array and then increment the count so it loops over.
        found = False
        for j in range(len(user_info)): #For every item in the user_info array, ask if the userID that was inputted exists, if it exists, check that the password matches.
            if userIDinp in user_info[j]:
                if userpassinp in user_info[j]:
                    print("Login Successful, you are eligible to vote!") #If the userID and password match, indicate a successful login and break out of the selection statement.
                    found = True
                    break
        if not found: #If the userID and password do not exist or the password was incorrectly entered, indicate an unsuccessful login and restart the login process.
            print("Unfortunately you are not eligible to vote, please try to login again")
            login.logging_in()
#Function created by Harry Barnard 00106041-8.

class Upload: #Creating and initialising a class to assign columns of a text document to variables.
    def __init__(self, position, candidatename):
        self.position = position
        self.candidatename = candidatename

    def add_new_candidates(self): #Define the function to add new candidates to the system.
        self.candidatename = input("Enter the name of the candidate you would like to upload > ") #Prompt the user to input the name of the candidate and the position they are running for.
        self.position = input("Enter the position they are running for (President, Faculty(A-P), GSU(A-C)")
        with open("GSUCandidates.txt") as candidates: #Open the text document as the variable name 'candidates'.
            if self.candidatename in candidates.read(): #If the candidate entered by the user is already in the text file, indicate that the candidate is already running for a position.
                print("This candidate is already running for a position!")
                candidates.close() #Close the text file to save it.
                return #Exit the function.
            else:

                newcandidate = Upload(self.position,self.candidatename) #If the candidate is not running for a position already, open the file in append plus format, meaning reading as well.
                candidates2 = open("GSUCandidates.txt","a+")
                candidates2.write(self.position+","+self.candidatename+"\n") #Write the candidates name and position to the text file, this should be at the end.
                candidates2.close()
                print("Candidate successfully entered!") #Close the file to save it and indicate that the process was a success to the user.
#Class created by Harry Barnard 00106041-8.

class Voting: #Creating and initialising the class used for casting votes.
    def __init__(self,candidatename,position):
        self.candidatename = candidatename
        self.position = position


    def castvotes(self): #Defining a new function which runs the code for the user to cast votes.
        import datetime
        from datetime import date #Importing date and time modules to allow us to compare and use dates.

        today = date.today() #Assigning a variable called 'today' to be the actual date of the day the code is running.
        votingperiod1 = datetime.date(2020,1,27) #Assigning a variable for the opening of the voting period and the following for the closing of the period.
        votingperiod2 = datetime.date(2020,1,30)

        if today >= votingperiod1: #Seeing whether the current date is within the voting period.
            if today <= votingperiod2:
                candidates = open("GSUCandidates.txt","r") #Open the file containing the current candidates in order to read them in and display to the user when required.
                candidate_info = []
                print("""Positions:
                President
                Faculty(A-P)
                GSU(A-C)""")
                choice = input("Please enter which position you would like to vote for > ")
                x = 0
                options = ["President","FacultyA","FacultyB","FacultyC","FacultyD","FacultyE","FacultyF","FacultyG","FacultyH","FacultyI","FacultyJ","FacultyK","FacultyL","FacultyM","FacultyN","FacultyO","FacultyP","GSUA","GSUB","GSUC"]

                for line in candidates: #Splitting the file into two variables separated by comma.
                    if x > 0:
                        self.position, self.candidatename = line.split(",")
                        if "\n" in self.candidatename: #Removing the "\n" from the end of each line in the file.
                            self.candidatename = self.candidatename[:-1]
                            candidate_info.append([self.position,self.candidatename]) #Append candidate data to an empty list.
                    x += 1
                if choice in options: #Display the candidates running for the position specified by the user.
                    for j in range(len(candidate_info)):
                        if choice in candidate_info[j]:
                            print(candidate_info[j])

                else:
                    print("Not a valid position, please try again!")
                    voting.castvotes() #If the position is not one of the positions that are valid, display that the position isn't real.


                votes1 = open("Votes1.txt","a+")
                votes2 = open("Votes2.txt", "a+")
                votes3 = open("Votes3.txt", "a+")
                votes4 = open("Votes4.txt", "a+") #Open all voting files ready for appending the new votes to.

                votecount1 = []
                votecount2 = []
                votecount3 = []
                votecount4 = [] #Create 4 empty lists which will contain information about the votes for each preference.

                n = 1

                while n<=4: #Repeat the loop 4 times because there are only 4 preferences, this ensures that the code will not loop and allow the user to vote more times.
                    if n == 1:
                        votepref = input("Enter who you would like to be your number "+str(n)+" choice > ") #Enter the information for the candidate you would like for your first, second, third and fourth choice.
                        votecount1.append([choice,votepref])
                        for element in votecount1:
                            votes1.write(str(element)+"\n") #Append the voting information to the associated list and then write it to the appropriate file.
                        print(votecount1)
                    elif n == 2:
                        votepref = input("Enter who you would like to be your number "+str(n)+" choice > ")
                        votecount2.append([choice,votepref])
                        for element in votecount2:
                            votes2.write(str(element)+"\n")
                        print(votecount2)
                    elif n == 3:
                        votepref = input("Enter who you would like to be your number "+str(n)+" choice > ")
                        votecount3.append([choice,votepref])
                        for element in votecount3:
                            votes3.write(str(element)+"\n")
                        print(votecount3)
                    elif n == 4:
                        votepref = input("Enter who you would like to be your number "+str(n)+" choice > ")
                        votecount4.append([choice,votepref])
                        for element in votecount4:
                            votes4.write(str(element)+"\n")
                        print(votecount4)
                    n += 1
#Class created by Harry Barnard 00106041-8.

class Counting: #Creating and initialising a class used for counting the votes.

    def __init__(self,candidatename,position,votecount):
        self.candidatename = candidatename
        self.position = position
        self.votecount = votecount

    def countvotes(self): #Creating a function used for counting the votes.

        first_place = open("Votes1.txt","r") #Opens all four voting text files, one is used for each preference (1st-4th).
        second_place = open("Votes2.txt","r")
        third_place = open("Votes3.txt","r")
        fourth_place = open("Votes4.txt","r")

        d = dict() #Create a dictionary to store information about the candidates and then a total incremented counter used to add up their votes.
        for line in first_place:
            line = line.strip()
            line = line.lower() #Strip the line and convert it to lower case so that if the user inputs a candidates name in caps or not it doesnt matter.

            words = line.split("\n") #Split line by the start of a new line.

            for word in words:
                word = word.replace("[","") #Removes unnecessary brackets and speech marks from the lines read in from the files.
                word = word.replace("'","")
                word = word.replace("]","")
                if word in d:
                    d[word] = d[word] + 1 #If the candidate is located in the line, increment the counter by 1.
                else:
                    d[word] = 1 #If it is not located in the line then leave the counter at 1.
        print("The vote counts for 1st choice are:") #Display to the user the total votes per candidate for each position.
        for key in list(d.keys()):
            print(key,":", d[key])

        e = dict() #Repeated code for each file, one for each position (1st to 4th).
        for line in second_place:
            line = line.strip()
            line = line.lower()

            words = line.split("\n")

            for word in words:
                word = word.replace("[", "")
                word = word.replace("'", "")
                word = word.replace("]", "")
                if word in e:

                    e[word] = e[word] + 1
                else:
                    e[word] = 1
        print("The vote counts for 2nd choice are:")
        for key in list(e.keys()):
            print(key, ":", e[key])

        f = dict()
        for line in third_place:
            line = line.strip()
            line = line.lower()

            words = line.split("\n")

            for word in words:
                word = word.replace("[", "")
                word = word.replace("'", "")
                word = word.replace("]", "")
                if word in f:

                    f[word] = f[word] + 1
                else:
                    f[word] = 1
        print("The vote counts for 3rd choice are:")
        for key in list(f.keys()):
            print(key, ":", f[key])

        g = dict()
        for line in fourth_place:
            line = line.strip()
            line = line.lower()

            words = line.split("\n")

            for word in words:
                word = word.replace("[", "")
                word = word.replace("'", "")
                word = word.replace("]", "")
                if word in g:
                    # print(word)
                    g[word] = g[word] + 1
                else:
                    g[word] = 1
        print("The vote counts for 4th choice are:")
        for key in list(g.keys()):
            print(key, ":", g[key])
#Class created by Harry Barnard 00106041-8.

def hack_3():
    def search_list(elem):
        if len(elem) == 2:
            return True;
        else:
            return False;


    def main():

        find_in_string = ['Jon Description Found', 'Job Description Not Found']


        print(find_in_string)


        if 'Job Description' in find_in_string:
            print("Yes, 'Job Description' found in List : ", find_in_string)


        if 'Job Description' not in find_in_string:
            print("No, 'Job Description' NOT found in List : ", find_in_string)


        if find_in_string.count('Job Description') > 0:
            print("Yes, 'Job Description' found in List : ", find_in_string)


        result = any(len(elem) == 2 for elem in find_in_string)

        if result:
            print("Yes, job description found")


        result = any(search_list for elem in find_in_string)

        if result:
            print("Yes, Job Description Found")


    if __name__ == '__main__':
        main()
#Muhammad Siddek Miah ID: 000995670-0


login = Login("","","")
login.logging_in()
display_menu()
hack_3()
select_menu()