from frappe.utils import getdate, sum, flt, precision
from erpnext.service import get_value, get_cached_value, throw
from erpnext.utils import format

class TaxCalculator:
    def __init__(self, account_currency):
        self.account_currency = account_currency

    def get_tax_rate(self):
        """Get tax rate from get_value method."""
        return get_value('Tax Rate', {'account_currency': self.account_currency})

    def get_tax_amount(self, amount):
        """Calculate tax amount based on tax rate and amount."""
        tax_rate = self.get_tax_rate()
        if tax_rate:
            tax_amount = flt(amount) * tax_rate
            return precision(tax_amount, self.account_currency)
        return 0

    def validate_taxes(self, amount):
        """Validate taxes on amount and throw error if any."""
        tax_amount = self.get_tax_amount(amount)
        return amount + tax_amount == amount

    def calculate_taxes(self, amount):
        """Calculate taxes on amount and return total amount."""
        if self.validate_taxes(amount):
            return amount + self.get_tax_amount(amount)
        else:
            throw("Invalid tax rate")

    def update_taxes(self, amount, new_amount):
        """Update taxes on amount."""
        self.calculate_taxes(amount)
        if new_amount != self.calculate_taxes(amount):
            throw("Invalid tax rate")
        return self.calculate_taxes(new_amount)