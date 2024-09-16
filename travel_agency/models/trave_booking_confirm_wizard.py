from odoo import fields,models
import logging
_l=logging.getLogger(__name__)

class TravelBookingConfirmWizard(models.TransientModel):
    _name="travel.booking.confirm.wizard"
    _description="this is wizard"
    


    def validate_action_confirm(self):
        ids=self.env.context.get('active_ids',[])
        _l.info(f"------------------> Active ids : {ids}")
        sale_ids=self.env['sale.order'].browse(ids)
        _l.info(f"------------------> sale ids : {sale_ids}")
        sale_ids=sale_ids.with_context(validate_not_click = False)
        # self=self.with_context(validate_not_click = False)
        _l.info(f"----------> wizard context : {self._context}")
        return sale_ids.action_cancel()