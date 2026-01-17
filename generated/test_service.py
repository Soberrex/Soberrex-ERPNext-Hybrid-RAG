import pytest
from erpnext.service import get_value
from erpnext.utils import throw
from tax_calculator import TaxCalculator

def test_get_tax_rate():
    tax_calculator = TaxCalculator('INR')
    tax_rate = tax_calculator.get_tax_rate()
    assert tax_rate is not None

def test_get_tax_amount():
    tax_calculator = TaxCalculator('INR')
    amount = 100
    tax_amount = tax_calculator.get_tax_amount(amount)
    assert tax_amount > 0

def test_validate_taxes():
    tax_calculator = TaxCalculator('INR')
    amount = 100
    assert tax_calculator.validate_taxes(amount)

def test_calculate_taxes():
    tax_calculator = TaxCalculator('INR')
    amount = 100
    total_amount = tax_calculator.calculate_taxes(amount)
    assert total_amount > amount

def test_update_taxes():
    tax_calculator = TaxCalculator('INR')
    amount = 100
    new_amount = 120
    tax_calculator.update_taxes(amount, new_amount)
    assert tax_calculator.calculate_taxes(new_amount) == new_amount