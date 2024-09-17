from odoo import fields,models,api
import logging
_l=logging.getLogger(__name__)
class SaleOrder(models.Model):

    _inherit='sale.order'

    status=fields.Selection([('pending','Pending'),('confirmed','Confirmed'),('cancelled','Cancelled')],string="Status",default='pending')


    name=fields.Char(readonly=False)

    def action_confirm(self):
        for rec in self:
            self.status='confirmed'
    

  
    
    def action_cancel(self):
        _l.info(f"----------> Sale.Order context : {self._context}")
        if self.env.context.get('validate_not_click',True):
            return {
            'type': 'ir.actions.act_window',
            'name':'action.validate.cancel',
            'res_model':'travel.booking.confirm.wizard',
            'view_mode':'form',
            'target':'new'
        }
        for rec in self:
            self.button_click_method()

    def confirm_booking(self):
        self.ensure_one()
        self.status = 'confirmed'
        return True
    

    def button_click_method(self):
        if self.env.context.get('user_clicked',False):
            self.status='confirmed'
            self.func1()
        else:
            self.status='cancelled'


    def func1(self):
        self=self.with_context(a=20,b=10)
        _l.info(f"---------------> \n Value of a = {self.env.context.get('a')}\n Value of b = {self.env.context.get('b')}")

        _l.info(f'-------->func1 before context is {self._context}')

        self=self.func2()

        _l.info(f'-------->func1 after context is {self._context}')

        _l.info(f"---------------> \n Value of a = {self.env.context.get('a')}\n Value of b = {self.env.context.get('b')}")
    
    def func2(self):
        _l.info(f"---------------> \n Func2 Value of a = {self.env.context.get('a')}\n Value of b = {self.env.context.get('b')}")
        _l.info(f'-------->func2 before context is {self._context}')
        # self=self.with_context(a=300,b=200)
        context=dict(self.env.context)
        context.pop('b',None)
        self=self.with_context(context)
        _l.info(f'-------->func2 after context is {self._context}')
        return self


