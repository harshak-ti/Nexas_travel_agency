from odoo import models, fields, api
from lxml import etree as ElementTree
import logging 
_l=logging.getLogger(__name__)
class CrmLead2OpportunityPartner(models.TransientModel):
    _name = 'crm.lead2opportunity.partner'
    _inherit = 'crm.lead2opportunity.partner'

    
    action = fields.Selection([

        ('create', 'Create a new customer'),

        ('exist', 'Link to an existing customer')

    ], string='Related Customer', compute='_compute_action', readonly=False, store=True, compute_sudo=False)