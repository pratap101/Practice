# --*-- utf-8 --*--

from openerp import models, api, fields

class Purchase_Order(models.Model):

    _inherit = 'purchase.order'
    
    responsible = fields.Many2one('res.users', string="Responsible", required=True, default=lambda self: self.env.user.id)
    company = fields.Many2one('res.company', string="Company", required=True, default=lambda self: self.env.user.company_id)
    
    #state_selection = fields.Selection([
     #                                 ('draft_po','Draft Po'),
      #                                ('rfa','RFQ'),
       #                               ('bid_received','Bid Received'),
        #                              ('awaiting_finance_approval','Awaiting Finance Approval'),
         #                             ('Purchase Confirmed','purchase_confirmed'),
          #                            ('cancelled','Cancelled')], 'state', default='draft_po')
