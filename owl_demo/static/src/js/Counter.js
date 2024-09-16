/** @odoo-module **/
import {Component} from "@odoo/owl"

class Counter extends Component{
    static template='counter';
    static components={};
    static props={
        initialCount:{type:Number,required:true}
    }
    state={
        count:0,
    }
    mounted(){
        this.state.count=this.props.initialCount;
    }
    increment(){
        this.state.count++;
        this.trigger('count-changed',this.state.count);
    }
    decrement(){
        this.state.count--;
        this.trigger('count-changed',this.state.count)
    }
}