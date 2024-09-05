/** @odoo-module **/

import { rpc } from 'web.rpc';
import { Dialog } from 'web.Dialog';

document.addEventListener('DOMContentLoaded', function () {
    const confirmBtn = document.getElementById('confirm_booking_btn');
    
    if (confirmBtn) {
        confirmBtn.addEventListener('click', function (event) {
            event.preventDefault();

            Dialog.confirm(this, 'Are you sure you want to confirm this booking?', {
                confirm_callback: function () {
                    const bookingId = document.querySelector('[name="id"]').value;

                    rpc.query({
                        model: 'travel.booking',
                        method: 'confirm_booking',
                        args: [parseInt(bookingId)],
                    }).then(function (result) {
                        if (result) {
                            window.location.reload(); // Reload the page after confirmation
                        }
                    });
                }
            });
        });
    }
});
