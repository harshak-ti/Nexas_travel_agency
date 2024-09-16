from odoo import fields,models,api
import logging
_l=logging.getLogger(__name__)
class SaleOrder(models.Model):
    _inherit='sale.order'

    status=fields.Selection([('pending','Pending'),('confirmed','Confirmed'),('cancelled','Cancelled')],string="Status",default='pending')

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
            self.status='cancelled'

    def confirm_booking(self):
        self.ensure_one()
        self.status = 'confirmed'
        return True
    
