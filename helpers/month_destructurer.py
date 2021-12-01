class MonthDestructurer:
    @staticmethod
    def get_month(monthon):
        if int(monthon) == 1:
            return "January"
        elif int(monthon) == 2:
            return "February"
        elif int(monthon) == 3:
            return "March"
        elif int(monthon) == 4:
            return "April"
        elif int(monthon) == 5:
            return "May"
        elif int(monthon) == 6:
            return "June"
        elif int(monthon) == 7:
            return "July"
        elif int(monthon) == 8:
            return "August"
        elif int(monthon) == 9:
            return "September"
        elif int(monthon) == 10:
            return "October"
        elif int(monthon) == 11:
            return "November"
        elif int(monthon) == 12:
            return "December"
        else:
            return monthon + " wrong month"