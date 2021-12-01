class DateDestructurer:
    @staticmethod
    def format_day(dayton):
        if 10 <= int(dayton) <= 20:
            return dayton + "th"
        elif int(dayton) % 10 == 1:
            return dayton + "st"
        elif int(dayton) % 10 == 2:
            return dayton + "nd"
        elif int(dayton) % 10 == 3:
            return dayton + "rd"
        else:
            return dayton + "th"