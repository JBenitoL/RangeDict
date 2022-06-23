import re

class RangeDic(dict):
    """If there are key values (at any level) with a range name as """

    def __getitem__(self, item):
        if isinstance(item, int) or isinstance(item, float):
            for key in self:
                value = self.__is_range(key)
                if value:
                    if value(item):
                        return super().__getitem__(key)
                value = self.__is_final(key)
                if value:
                    if value(item):
                        return super().__getitem__(key)
        else:
            if "custom" in item:
                return None
            value = super().__getitem__(item)
            if isinstance(value, dict):
                return RangeDic(value)
            return value

    def choices(self, *args):
        dic = self
        for arg in args:
            dic = dic[arg]
        choices = []
        for key in dic:
            choices.append((key, key))
        return choices

    @staticmethod
    def __is_final(txt):
        pattern = "([<>])([=]{,1})([0-9\.]+)"
        match = re.match(pattern, txt)
        if match:
            if match.group(2):
                if match.group(1) == "<":
                    return float(match.group(3)).__ge__
                if match.group(1) == ">":
                    return float(match.group(3)).__le__
            else:
                if match.group(1) == "<":
                    return float(match.group(3)).__gt__
                if match.group(1) == ">":
                    return float(match.group(3)).__lt__

    @staticmethod
    def __is_range(txt):
        pattern = "([\(\[]{,1})([0-9\.]+)-([0-9\.]+)([\)\]]{,1})"
        match = re.match(pattern, txt)
        if match:
            if match.group(1) == "[" or not match.group(1):
                if match.group(4) == ")" or not match.group(4):
                    return lambda x: float(match.group(2)) <= x and float(match.group(3)) > x
                else:
                    return lambda x: float(match.group(2)) <= x and float(match.group(3)) >= x
            else:
                if match.group(4) == ")" or not match.group(4):
                    return lambda x: float(match.group(2)) < x and float(match.group(3)) > x
                else:
                    return lambda x: float(match.group(2)) < x and float(match.group(3)) >= x

                

