from analys_data import *
from generate_data import *
from filter_data import *

def start():
    flag_main = True
    while flag_main:
        print("Comands:filter, analys, read_data,gen_data, exit")
        a = input("Enter command:").lower().replace(' ' , '')
        if a == 'analys':
            candidates_votes()
            party_votes()
            candidate_votes_democrat()
            candidate_votes_republican()
            state_votes_democrat()
            state_votes_republican()
        elif a == 'filter':
            print(""" Filter
            1 - party
            2 - state
            3 - state_abbr
            4 - candidate
            5 - votes >
            6 - votes <
            7 - quit
            """)

            b = int(input("Enter command:"))
            if b == 7:
                break
            if b == 1:
                print("""1 - Republican 2 - Democrat""")
                c = int((input("Enter command:")))
                if c == 1:
                    filter_party("Republican")
                if c == 2:
                    filter_party("Democrat")
            if b == 2:
                c = input("Enter state:")
                filter_state(c)
            if b == 3:
                c = input("Enter st_abbr:")
                filter_st_abbr(c)
            if b == 4:
                c = input("Enter candidate:")
                filter_candidate(c)
            if b == 5:
                c = int(input("Enter gt votes:"))
                filter_votes_gt(c)
            if b == 6:
                c = int(input("Enter ls votes:"))
                filter_votes_ls(c)

            if (b < 1 or b > 7):
                print("Error number")
                flag_main = True

        elif a == "read_data":
            read_data()
        elif a == "gen_data":
            c = int(input("Enter count:"))
            generate_data(c)
        elif a == "exit":
            break

start()


#generate_data(5)
#filter_data('candidate',"Martin O'Malley")
#filter_candidate("Martin O'Malley")
#filter_party("Republican")
#filter_st_abbr("CA")
#filter_state("California")
#filter_votes_gt(10000)
#filter_votes_ls(5000)
