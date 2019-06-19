from member import Member

class Team:
    def __init__(self,team_id):
        self.team_id=team_id
        self.members=[]

    def __repr__(self):
        return "Team Id : {}, Members : {}".format(self.team_id, self.members)

    def add_member(self):
        name = input("Enter the member's name: ")
        contact = input("Enter {}'s contact details: ".format(name))
        self.members.append(Member(name,contact,False))

    def print_member_list(self):
        for member in self.members:
            print("Name : {}, Contact : {}, Paid : {}\n".format(member.name,member.contact,member.paid))

    def set_member_paid(self,member_name):
        for member in self.members:
            if member.name == member_name:
                member.paid=True

    def delete_member(self,member_name):
        self.members=list(filter(lambda member: member.name!=member_name,self.members))

    def paid_members(self):
        paid_list=list(filter(lambda member: member.paid, self.members))
        for p in paid_list:
            print("Name : {}, Contact : {}, Paid : {}\n".format(p.name,p.contact,p.paid))


    def json(self):
        return {
            'teamID' :self.team_id,
            'members' : [
            member.json() for member in self.members
            ]
        }

    @classmethod
    def fromjson(cls,json_data):
        team=Team(json_data['teamID'])
        for member in json_data['members']:
            team.members.append(Member.fromjson(member))
        return team
