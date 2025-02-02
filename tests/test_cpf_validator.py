import pytest
from function_app import validate_cpf

def test_valid_cpf():
    assert validate_cpf("529.982.247-25") == True
    assert validate_cpf("52998224725") == True

def test_invalid_cpf():
    assert validate_cpf("111.111.111-11") == False
    assert validate_cpf("123.456.789-00") == False
    assert validate_cpf("abc.def.ghi-jk") == False
    assert validate_cpf("") == False
    assert validate_cpf("123") == False