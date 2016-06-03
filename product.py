# --*-- utf-8 --*--

from openerp import fields, models, api

class on_change_function(models.Model):

    _inherit = 'product.template'
    
    @api.onchange('list_price')
    def _cal_sale_price(self):
        self.standard_price = self.list_price + 10
