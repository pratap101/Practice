# this py file is not related to this module.
# Only for learning purpose

# for generating sequence no in old api when click on save button
@api.onchange('name_')
@api.depends('name_')    
def create(self, cr, uid, vals, context=None):
    if context is None:
        context = {}
    
    vals['name_'] = self.pool.get('ir.sequence').get(cr, uid, 'call.sequence') or '/'
    ctx = dict(context or {}, mail_create_nolog=True)
    self._name = super(CallForBids, self).create(cr, uid, vals, context=ctx)
    return new_id

# structure of onchange method that return a value in old api      
def _on_change_price(self, cr, user, ids, list_price, context = None):
    res = {}

    total = list_price + 10
    res = {
        'value':{
            'standard_price' : total  
            }
        }
    return res
