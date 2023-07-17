from inspect import isfunction

class FactoryFormatter():
    """This class formats numbers using the factory OOP concept.
    The class takes a list of functions of a consistent format. 
    Whereby, each function must take in one parameter as a value
    and returns only one parameter. When running the format, the 
    process will apply each method based on the provided list's 
    sequence."""

    def __init__(self, list_of_formatters:list) -> None:
        """This function initialized the class with 
        a formatter list"""

        # check if the type of the input is a list
        assert type(list_of_formatters) is list, "Please insert a list"
        # check if it is a list of funtions
        for f in list_of_formatters:
            assert isfunction(f) is True, "Each item must be a function"
        # create a private value of list of formatters
        self._list_of_formatters = list_of_formatters
        # initialize the result
        self.result = None
    
    def format(self, value):
        """This function runs the formatter list in sequence"""

        # iterate over the whole list
        for f in self._list_of_formatters:
            # apply the format of this item
            value = f(value)
        # save the result
        self.result = value
        # return the result
        return self.result
