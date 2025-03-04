from abc import ABC, abstractmethod


class BaseSearch(ABC):
    def __init__(self, data: list[any]) -> None:
        if not isinstance(data, list):
            raise TypeError("Ошибка! Должен быть передан список данных.")
        self.data = data

    @abstractmethod
    def _linear(self, search_element: any, key: any) -> int | None:
        pass

    @abstractmethod
    def _binary(self, search_element: any, key: any) -> int | None:
        pass

    def _searcher(self, search_element: any, key: any, mode: str = "linear") -> int | None:
        if mode == "linear":
            return self._linear(search_element, key)
        elif mode == "binary":
            return self._binary(search_element, key)
        else:
            raise ValueError(f"Некорректный режим поиска: {mode}")


class SearchByListTuple(BaseSearch):
    def _linear(self, search_element: any, key_tuple: int) -> int | None:
        for index, _tuple in enumerate(self.data):
            if _tuple and len(_tuple) > key_tuple and _tuple[key_tuple] == search_element:
                return index
        return None

    def _binary(self, search_element: any, key_tuple: int) -> int | None:
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid] is None or len(self.data[mid]) <= key_tuple:
                return None
            if self.data[mid][key_tuple] == search_element:
                return mid
            elif self.data[mid][key_tuple] < search_element:
                left = mid + 1
            else:
                right = mid - 1
        return None


class SearchByInstanceClasses(BaseSearch):
    def _linear(self, search_element: any, attribute_name: str) -> int | None:
        for index, obj in enumerate(self.data):
            if hasattr(obj, attribute_name) and getattr(obj, attribute_name) == search_element:
                return index
        return None

    def _binary(self, search_element: any, attribute_name: str) -> int | None:
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_obj = self.data[mid]
            if not hasattr(mid_obj, attribute_name):
                return None
            mid_value = getattr(mid_obj, attribute_name)
            if mid_value == search_element:
                return mid
            elif mid_value < search_element:
                left = mid + 1
            else:
                right = mid - 1
        return None



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person("Иван", 30), Person("Петр", 25), Person("Сергей", 35)]
search = SearchByInstanceClasses(people)
index = search._searcher("Сергей", key="name", mode="linear")
print(index)

def inner_loop(data):
    for item in data:
        yield item


def outer_loop(data_batches):
    for batch in data_batches:
        yield from inner_loop(batch)


data = [[1, 2, 3], [4, 5, 6]]

for result in outer_loop(data):
    print(result)





