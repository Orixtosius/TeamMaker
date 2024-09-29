class DictionaryOperator:

    def __init__(self):
        self._obj_dict = dict()

    def add_into_dictionary(self, **kwargs) -> None:
        if "assign" in kwargs:
            self._obj_dict = kwargs["p"]
        else:
            if "key" in kwargs and "value" in kwargs:
                item_key = kwargs["key"]
                self._obj_dict[item_key] = kwargs["value"]

    def get_dictionary(self) -> dict:
        return self._obj_dict