# --*-- utf-8 --*--
import time
from openerp import models, api, fields

class CallForBids(models.Model):
    
    _rec_name = 'name_'
    _name = 'call.for.bids'
    
    def get_current_date(self):
        return time.strftime("%Y-%m-%d"); 
        
    def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        
        vals['name_'] = self.pool.get('ir.sequence').get(cr, uid, 'call.sequence') or '/'
        ctx = dict(context or {}, mail_create_nolog=True)
        new_id = super(CallForBids, self).create(cr, uid, vals, context=ctx)
        return new_id
        
    name_ = fields.Char('Call for Bids Reference', readonly=True)
    user_id = fields.Many2one('res.users', string="Responsible", required=True, default=lambda self: self.env.user.id)
    creation_date = fields.Date('Creation date', required=True, default=lambda self: self.get_current_date(), readonly=True)
    bids = fields.One2many('call.for.bids.line', 'bids_id', 'Bids') 
    
        
class Call_For_Bids_Line(models.Model):
    _name = 'call.for.bids.line'
    
    bids_id = fields.Many2one('call.for.bids')
    product = fields.Many2one('product.product', string="Product")
    quantity = fields.Float('Quantity', default="1", compute='_get_quantity')
    u_o_m = fields.Many2one('product.uom', 'Product Unit of Measure')
    
    @api.depends('quantity')
    def _get_quantity(self):
        
        if self.quantity < 10:
            self.quantity = self.quantity + 20

    
    
         
               
