from team import Team
import os
import json

max_team_limit = 5


def menu():
    team_id = input("Enter the Team ID: ")
    if os.path.isfile(team_id):
        with open(team_id,'r') as f:
            json_data=json.load(f)
            team =Team.fromjson(json_data)

    else:
        team = Team(team_id)

    while(1):
        print("Menu")
        print("1# To add a Member's name,")
        print("2# To see the list of Members,")
        print("3# To set a Member as paid,")
        print("4# to delete a Member,")
        print("5# to see the list of paid Member,")
        print("6# to save the changes in a Json file,")
        print("0# to quit.")

        choice = int(input("Please, Enter your choice: "))

        if choice == 1:
            rep = int(input("Enter the total number of member's you want to enter: "))
            if max_team_limit >= rep+len(team.members):
                for r in range(rep):
                    team.add_member()
            else:
                print("Reached Maximum limit, no more members can be added in the team")
        elif choice == 2:
            team.print_member_list()

        elif choice == 3:
            member_name=input("Enter the member's name you want to set as paid: ")
            team.set_member_paid(member_name)
        elif choice == 4:
            member_name=input("Enter the member's name you want to delete: ")
            team.delete_member(member_name)

        elif choice == 5:
            team.paid_members()

        elif choice == 6:
            with open(team.team_id,'w') as f:
                json.dump(team.json(),f)
        elif choice == 0:
            break



menu()
