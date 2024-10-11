from odoo import api, fields, models

class Lead2OpportunityPartnerInherited(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    actions = fields.Selection([
        ('create', 'Create a new customer'),
        ('exist', 'Link to an existing customer'),
    ], string='Related Customer (Custom)', compute='_compute_actions', readonly=False, store=True, compute_sudo=False)

    @api.depends('lead_id')
    def _compute_actions(self):
        """ This method computes the new 'actions' field based on the parent 'lead_id' """
        for convert in self:
            if not convert.lead_id:
                convert.actions = False
            else:
                partner = convert.lead_id._find_matching_partner()
                if partner:
                    convert.actions = 'exist'
                elif convert.lead_id.contact_name:
                    convert.actions = 'create'
                else:
                    convert.actions = False

    

    def _convert_and_allocate(self, leads, user_ids, team_id=False):
        """ Override the convert and allocate logic to use 'actions' """
        self.ensure_one()

        for lead in leads:
            if lead.active :  
                self._convert_handle_partner(
                    lead, self.actions, self.partner_id.id or lead.partner_id.id)

            lead.convert_opportunity(lead.partner_id, user_ids=False, team_id=False)

        leads_to_allocate = leads
        if not self.force_assignment:
            leads_to_allocate = leads_to_allocate.filtered(lambda lead: not lead.user_id)

        if user_ids:
            leads_to_allocate._handle_salesmen_assignment(user_ids, team_id=team_id)

    