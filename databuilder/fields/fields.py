from numpy.random import normal, rand
from brule import full_name, first_name, last_name
from names import get_full_name, get_first_name, get_last_name

from datetime import datetime, timedelta, time, date
from random import choice, randint
from string import ascii_lowercase
from uuid import uuid4
from re import split as re_split



#------------------------#
#                        #
#   Abstracted Classes   #
#                        #
#------------------------#

class _Numeric():
    def __init__(self, precision=0):
        self.precision = precision


#-------------------#
#                   #
#   Numeric Types   #
#                   #
#-------------------#

class UniformDist(_Numeric):

    # TODO
    # weird data patterns? when precision is None

    def __init__(self, low, high, precision=None):
        super().__init__(precision)
        self.low = low
        self.high = high

    def to_series(self, n):
        return [round((rand() * (self.high - self.low) + self.low), self.precision) for _ in range(n)]


class NormalDist(_Numeric):
    
    def __init__(self, mean, sd, precision=None):
        super().__init__(precision)
        self.mean = mean
        self.sd = sd

    def to_series(self, n):
        return [round(normal(self.mean, self.sd), self.precision) for _ in range(n)]


#------------------#
#                  #
#   String Types   #
#                  #
#------------------#

class Name():
    
    def __init__(self, first_only=False, last_only=False, brule=False):
        self.first_only = first_only
        self.last_only = last_only
        self.brule = brule

    # def to_series(self, n, relations=None):
    def to_series(self, n, src=None, dest=None):

        if dest and dest != 'gender':
            print('WARNING: not able to apply relation transformation')
            dest = None

        # choose which functions to use
        if self.brule:
            funcs = {'full': full_name, 'first': first_name, 'last': last_name}
        else:
            funcs = {'full': get_full_name, 'first': get_first_name, 'last': get_last_name}
        
        if dest:
            src = src.apply(lambda x: 'male' if x.lower()[0] == 'm' else 'female')

            if self.first_only:
                func = funcs['first']
                return [func(gender=src[i]) for i in range(n)]
            if self.last_only:
                func = funcs['last']
                return [func() for _ in range(n)]
            
            # else
            func = funcs['full']
            return [func(gender=src[i]) for i in range(n)]     

        else:
            if self.first_only:
                func = funcs['first']
                return [func() for _ in range(n)]
            if self.last_only:
                func = funcs['last']
                return [func() for _ in range(n)]
            
            # else
            func = funcs['full']
            return [func() for _ in range(n)]  


class Email():

    def __init__(self, suffix="@mail.com"):
        self.suffix = suffix

    def to_series(self, n, src=None, dest=None):
        pass


#--------------------#
#                    #
#   DateTime Types   #
#                    #
#--------------------#

class Date():
    
    def __init__(self, start, end):

        # clean args
        if not isinstance(start, (date, datetime)):
            try:
                start = self._parse_date(start)
            except:
                raise ValueError("Unable to parse start date, see `help(Date)` for info")

        if not isinstance(end, (date, datetime)):
            try:
                end = self._parse_date(end)
            except:
                raise ValueError("Unable to parse end date, see `help(Date)` for info")

        # set attributes
        self.start = start
        self.end = end


    def _parse_date(self, date_string):
        parts = re_split(r'(-|/|\.|\s)', date_string)
        parts = [p for p in parts if p not in ('-', '/', ':', ' ', '.')]

        if len(parts) == 3:
            return date(*list(map(int, parts)))
        
        else:
            raise ValueError(f"Unable to parse date: {date_string}")

    
    def to_series(self, n):
        diff = self.end - self.start
        return [self.start + timedelta(days=randint(0, diff.days)) for _ in range(n)]


class DateTime():
    
    # add option for biz hours only?

    def __init__(self, start, end, unix=False):
        
        if not isinstance(start, datetime):
            try:
                start = self._parse_date(start)
            except:
                raise ValueError("Unable to parse start date, see `help(DateTime)` for info")

        if not isinstance(end, datetime):
            try:
                end = self._parse_date(end)
            except:
                raise ValueError("Unable to parse end date, see `help(DateTime)` for info")

        # set attributes
        self.start = start
        self.end = end
        self.unix = unix


    def _parse_date(self, date_string):
        parts = re_split(r'(-|/|:|\.|\s)', date_string)
        parts = [p for p in parts if p not in ('-', '/', ':', ' ', '.')]

        # [year, mon, day, hour, min, sec]
        # [year, mon, day, hour, min]
        if len(parts) >= 5:
            return datetime(*list(map(int, parts)))
        
        else:
            raise ValueError(f"Unable to parse date: {date_string}")


    def to_series(self, n):
        diff = self.end - self.start
        if self.unix:
            return [int((self.start + timedelta(seconds=randint(0, diff.total_seconds()))).timestamp()) for _ in range(n)]
        else:
            return [self.start + timedelta(seconds=randint(0, diff.total_seconds())) for _ in range(n)]


class Time():
    
    def __init__(self, start, end):
        
        if not isinstance(start, time):
            try:
                start = self._parse_time(start)
            except:
                raise ValueError("Unable to parse start time, see `help(Time)` for info")

        if not isinstance(end, time):
            try:
                end = self._parse_time(end)
            except:
                raise ValueError("Unable to parse end time, see `help(Time)` for info")

        self.start = start
        self.end = end        


    def _parse_time(self, time_string):
        parts = re_split(r'(-|/|:|\.|\s)', time_string)
        parts = [p for p in parts if p not in ('-', '/', ':', ' ', '.')]

        if len(parts) >= 2:
            return time(*list(map(int, parts)))
        
        else:
            raise ValueError(f"Unable to parse time: {time_string}")


    def to_series(self, n):
        form = '%H:%M:%S'
        d1 = datetime.strptime(self.start.strftime(form), form)
        d2 = datetime.strptime(self.end.strftime(form), form)
        diff = d2 - d1
        return [(d1 + timedelta(seconds=randint(0, diff.total_seconds()))).strftime(form) for _ in range(n)]


#-----------------#
#                 #
#   Group Types   #
#                 #
#-----------------#

class Group():

    def __init__(self, groups):
        self.groups = groups

    def to_series(self, n):
        
        # check if custom probabilites were provided
        if isinstance(self.groups[0], (list, tuple)):
            
            if sum([x[1] for x in self.groups]) != 1:
                raise ValueError("Probabilites don't add to 1")

            series = []
            for _ in range(n):
                r = rand()
                for label, prob in self.groups:
                    r -= prob
                    if r <= 0:
                        series.append(label)
                        break
            return series

        # if no probabilities were given, use a uniform dist
        else:
            return [choice(self.groups) for _ in range(n)]


#--------------#
#              #
#   ID Types   #
#              #
#--------------#

class ID():

    def __init__(self, start=1):
        self.start = start
        
    def to_series(self, n):
        return [x for x in range(self.start, n+self.start)]


class GUID():

    def __init__(self, format="str"):
        self.format = format

    def to_series(self, n):
        if self.format == "hex":
            return [uuid4().hex for _ in range(n)]
        elif self.format == "int":
            return [uuid4().int for _ in range(n)]
        else:
            return [uuid4() for _ in range(n)]