/** @odoo-module **/

import { Component, onWillStart, onWillUpdateProps } from "@odoo/owl";
import { registry } from "@web/core/registry";

// Parent component: OWLSelectionLimitedField
export class OWLSelectionLimitedField extends Component {
    static supportedFieldTypes = ['selection'];
    static template = 'OWLFieldLimitedSelection';
 

    setup() {
        this.filteredOptions = [];

        // Use lifecycle hooks to manage data
        onWillStart(() => {
            this.filterOptions();
        });

        onWillUpdateProps(() => {
            this.filterOptions();
        });
    }

    // Arrow function to bind the correct context
    optionSelected = (value) => {
        // Update the record when an option is selected
        console.log(this.props.record)
        this.props.record.update({ [this.props.name]: value });
    }

    filterOptions() {
        const field = this.props.record.fields[this.props.name];
        console.log(this.props.name)
        if (!field || !field.selection) {
            this.filteredOptions = [];
            return;
        }

        // Filter options to show
        this.filteredOptions = field.selection
            .filter((option, index) => index < 2 && option[0] !== 'nothing');
    }
}

// Register the widget for use in Odoo fields
registry.category("fields").add("limited_selection", {
    component: OWLSelectionLimitedField,
});
