class Member:
    def __init__(self, name, contact,paid):
        self.name=name
        self.contact=contact
        self.paid = paid

    def __repr__(self):
        return "Name : {}, Contact : {}, Money Paid : {}".format(self.name,self.contact,self.paid)


    def json(self):
        return {
            'name':self.name,
            'contact':self.contact,
            'paid':self.paid
        }

    @classmethod
    def fromjson(self,json_data):
        return Member(**json_data)
