# --*-- utf-8 --*--
import time
from openerp import models, api, fields

class CallForBids(models.Model):
    
    _rec_name = 'name_'
    _name = 'call.for.bids'
    
    def get_current_date(self):
        return time.strftime("%Y-%m-%d"); 
    
    #@api.onchange('name_')
    #@api.depends('name_')    
    #def _create(self, cr, uid, vals, context=None):
     #   if context is None:
      #      context = {}
        
       # vals['name_'] = self.pool.get('ir.sequence').get(cr, uid, 'call.sequence') or '/'
        #ctx = dict(context or {}, mail_create_nolog=True)
        #self._name = super(CallForBids, self).create(cr, uid, vals, context=ctx)
        #return new_id
    
    def _get_name(self):
        print "------------------------"
        model = self.env['ir.sequence'].next_by_code('call.sequence') 
        print type(model)
        return model

    #@api.onchange('name_')
    #def _get_change(self):
        #print "hello"
        #val = self.name_
        #print val
        #model = self.env['purchase.order'].browse(self.ids)    
        #rec = super(PurchaseOrder, self).create(val['partner_ref'])
        #print rec        
    
    @api.multi
    def set_to_draft(self):
        self.write({'state':'rfq'})
        return True
        
    @api.multi
    def send_by_rfq(self):
        self.write({'state':'send_by_email'})
        return True
        
    @api.multi
    def send_for_app(self):
        self.write({'state':'send_for_approval'})
        return True
    
    @api.multi
    def confirm_order(self):
        self.write({'state':'confirm_order'})
        return True  
    
    @api.multi
    def cancel(self):
        self.write({'state':'cancel'})
        return True  
                    
 
    
    name_ = fields.Char('Call for Bids Reference', required=True, readonly=True, default=lambda self: self._get_name())
    user_id = fields.Many2one('res.users', string="Responsible", required=True, default=lambda self: self.env.user.id)
    creation_date = fields.Date('Creation date', required=True, default=lambda self: self.get_current_date(), readonly=True)
    bids = fields.One2many('call.for.bids.line', 'bids_id', 'Bids') 
    state = fields.Selection([
                            ('draft','Draft'),
                            ('send_by_email','Send By Email'),
                            ('rfq','Rfq'),
                            ('send_for_approval','Send For Approval'),
                            ('confirm_order','Confirm Order'),
                            ('cancel','Cancelled')
                            ], default='draft')
    
        
class Call_For_Bids_Line(models.Model):
    _name = 'call.for.bids.line'
    
    bids_id = fields.Many2one('call.for.bids')
    product = fields.Many2one('product.product', string="Product")
    quantity = fields.Float( compute="_get_quantity", string="Quantity", readonly=False, default=10)
    u_o_m = fields.Many2one('product.uom', 'Product Unit of Measure')
    
    @api.depends('quantity')
    @api.onchange('quantity')
    def _get_quantity(self):
        print type(self.quantity)
        print "-----------------------------"
        print self.quantity
        print "-----------------------------"
        for record in self:
            if record.quantity < 10:
                record.quantity = record.quantity + 20
            else:
                record.quantity = record.quantity
    
    
         
               
