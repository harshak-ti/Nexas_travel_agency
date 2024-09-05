/** @odoo-module **/

odoo.define('nexas_travel_agency.custom_button_action', function (require) {
    "use strict";

    var ListController = require('web.ListController');

    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            var self = this;
            if (this.$buttons) {
                var custom_button = this.$buttons.find('.btn-primary');
                custom_button && custom_button.on('click', function () {
                    self.do_action({
                        type: 'ir.actions.act_window',
                        res_model: 'travel.booking',
                        name: 'Custom Action',
                        views: [[false, 'form']],
                        target: 'new',
                    });
                });
            }
        },
    });
});
