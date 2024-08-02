from abc import ABC, abstractmethod


class SqlTable(ABC):
    @abstractmethod
    def _dict_converter(self, dictionary: dict):
        pass

    @classmethod
    def dicts_converter(cls, subclass, dictionaries: list[dict]):
        rows = []
        for row in dictionaries:
            sql_table_row = subclass._dict_converter(row)
            rows.append(sql_table_row)
        return rows
