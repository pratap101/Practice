@api.onchange('name_')
@api.depends('name_')    
def _create(self, cr, uid, vals, context=None):
    if context is None:
        context = {}
    
    vals['name_'] = self.pool.get('ir.sequence').get(cr, uid, 'call.sequence') or '/'
    ctx = dict(context or {}, mail_create_nolog=True)
    self._name = super(CallForBids, self).create(cr, uid, vals, context=ctx)
    return new_id

