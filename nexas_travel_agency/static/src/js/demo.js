odoo.define('nexas_travel_agency.travel_booking_custom_button', function (require) {
    "use strict";

    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');

    // Extend ListController to handle the custom button action
    var TravelBookingListController = ListController.extend({
        buttons_template: 'Custom_ListView.buttons',
        events: _.extend({}, ListController.prototype.events, {
            'click .o_button_custom_action': '_onCustomAction',
        }),

        // Action triggered when the custom button is clicked
        _onCustomAction: function () {
            console.log("Custom button clicked!");
            // Add your custom logic here
        },
    });

    // Extend ListView to use the custom controller
    var TravelBookingListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: TravelBookingListController,
        }),
    });

    // Register the custom ListView
    viewRegistry.add('travel_booking_tree', TravelBookingListView);
});
