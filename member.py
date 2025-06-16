"""
Member class. It is used for representing each member of the team.
"""
from datetime import datetime

class Member:
    def __init__(self, codname, name, surname1, surname2, company_init_date, team_init_date):
        """company_init_date and team_init_date must be in format dd-mm-yyyy"""
        self.codname = codname
        self.name = name
        self.surname1 = surname1
        self.surname2 = surname2

        # Dates require a specific format. If not provided, inicialized as None
        allowed_format = "%d-%m-%Y"

        try:
            self.company_init_date = datetime.strptime(company_init_date, allowed_format)
        except ValueError:
            self.company_init_date = None
            print("error: company_init_date format is not valid. Registered as None.")

        try:
            self.team_init_date = datetime.strptime(team_init_date, allowed_format)
        except ValueError:
            self.team_init_date = None
            print("error: team_init_date format is not valid. Registered as None.")
            

    def get_company_seniority(self):
        """Returns the seniority in company in months.
        In case the member doesn't have company_init_date, it returns '?'"""
        if self.company_init_date is None:
            print("error: company_init_date is not registered in this member.")
            return "?" 

        today = datetime.today()
        seniority = today - self.company_init_date
        seniority_in_months = seniority.days // 30
        return seniority_in_months

    def get_team_seniority(self):
        """Returns the seniority in the team in months.
        In case the member doesn't have team_init_date, it returns '?'"""
        if self.team_init_date is None:
            print("error: team_init_date is not registered in this member.")
            return "?"

        today = datetime.today()
        seniority = today - self.team_init_date
        seniority_in_months = seniority.days // 30
        return seniority_in_months

    def get_email(self):
        """Returns the corporative email"""
        return f"{self.codname}@corporative_email.com"

if __name__=="__main__":
    maria = Member("mgarcia", "maría", "garcía", "alejo", "03-04-2022", "3-5-25")
    print(maria.codname, maria.name, sep=" => ")
    print("Antigüedad company", maria.get_company_seniority())
    print("Antigüedad equipo", maria.get_team_seniority())
    print("Email", maria.get_email())