# --*-- utf-8 --*--

from openerp import models, api, fields

class Purchase_Order(models.Model):

    _inherit = 'purchase.order'
    
    responsible = fields.Many2one('res.users', string="Responsible", required=True, default=lambda self: self.env.user.id)
    company = fields.Many2one('res.company', string="Company", required=True, default=lambda self: self.env.user.company_id)
    
