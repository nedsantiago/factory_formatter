import pytest
import formatter
from re import sub

def remove_php(string:str):
    string = sub(r"[Pp]hp",r"", string)
    return string

def remove_comma(string:str):
    string = sub(r"[,]", r"", string)
    return string

def convert_to_float(string:str):
    float_value = float(string)
    return float_value

class test_encapsulate():
        
    def test1(self):
        list_format = [remove_php, remove_comma]
        format_engine = formatter.FactoryFormatter(list_format)
        result = format_engine.format("Php 53,000.00")
        assert result.strip() == "53000.00"
    
    def test2(self):
        list_format = [remove_php, remove_comma, convert_to_float]
        format_engine = formatter.FactoryFormatter(list_format)
        result = format_engine.format("Php 53,000.00")
        assert result == 53000.00

def test_convert_to_string_num():
    tester = test_encapsulate()
    tester.test1()

def test_convert_to_float_num():
    tester = test_encapsulate()
    tester.test2()