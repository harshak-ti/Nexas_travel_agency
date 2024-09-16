/** @odoo-module **/

import {Component} from "@odoo/owl";
import Counter from "./Counter"

class App extends Component{
    static template='app';
    static components={Counter}

    mounted(){
        this.counter=this.createComponent(Counter,{
            initialCount:5
        });
        this.counter.on('count-changed',(count)=>{
            console.log(`Count changed to ${count}`);
        })
    }
}