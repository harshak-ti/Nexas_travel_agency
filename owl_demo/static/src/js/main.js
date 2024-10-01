/** @odoo-module */
import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class FilteredSelectionField extends Component {
    static template = 'FilteredSelectionFieldTemplate'; // Template definition
    
    // This is where we filter the options
    get filteredOptions() {
        return this.props.selection.filter(option => option[0] !== 'nothing');
    }
}

// Register the widget to be used in the view
registry.category("fields").add("status_selection", {
    component: FilteredSelectionField,
});
