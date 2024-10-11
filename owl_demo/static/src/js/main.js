/** @odoo-module */


import { Component, onWillStart, onWillUpdateProps } from "@odoo/owl";
import { registry } from "@web/core/registry";

class ColorPill extends Component {
    static template = 'OWLColorPill';
    pillClicked() {
        this.props.onClickColorUpdated(this.props.color);
    }
}

export class OWLCategColorField extends Component {
    static supportedFieldTypes = ['integer'];
    static template = 'OWLFieldColorPills';
    static components = { ColorPill };
    
    setup() {
        this.totalColors = [1, 2, 3, 4, 5, 6];  // Define colors
        onWillStart(async () => {
            await this.loadCategInformation();
        });
        onWillUpdateProps(async () => {
            await this.loadCategInformation();
        });
    }

    colorUpdated(value) {
        this.props.record.update({ [this.props.name]: value });
    }

    async loadCategInformation() {
        const self = this;
        self.categoryInfo = {};
        const resModel = self.env.model.root.resModel;
        const domain = [];
        const fields = ['priority'];
        const groupby = ['priority'];
        
        const categInfoPromise = await self.env.services.orm.readGroup(
            resModel,
            domain,
            fields,
            groupby
        );

        console.log(categInfoPromise)
        
        categInfoPromise.forEach((info) => {
            self.categoryInfo[info.category] = info.category_count;
        });
    }
}

// Register the widget to be used for integer fields
registry.category("fields").add("category_color", {
    component: OWLCategColorField
});
