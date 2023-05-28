class DictionaryOperator:

    def __init__(self):
        self.__obj_dict = dict()

    def add_into_dictionary(self, **kwargs):
        if "assign" in kwargs:
            self.__obj_dict = kwargs["p"]
        else:
            if "key" in kwargs and "value" in kwargs:
                item_key = kwargs["key"]
                self.__obj_dict[item_key] = kwargs["value"]

    def get_dictionary(self):
        return self.__obj_dict