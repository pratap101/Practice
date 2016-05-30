# --*-- utf-8 --*--

from openerp import fields, models, api

class on_change_function(models.Model):

    _inherit = 'product.template'
    
    @api.onchange('list_price')
    def _cal_sale_price(self):
       # res = {}
        print "----------------------------------"
        self.standard_price = self.list_price + 10
        #res = {
                #'standard_price' : total
        #}
        #res['standard_price'] = total
        #print "------------------------------------"
        #print res
        #return res
        #setattr(self, 'standard_price', total)
        #setattr(self, 'weight', total)
        
    #def _on_change_price(self, cr, user, ids, list_price, context = None):
        
     #   res = {}
        
      #  total = list_price + 10
       # res = {
        #    'value':{
        #         'standard_price' : total  
         #   }
        #}
        #return res    
    
    
    
    
