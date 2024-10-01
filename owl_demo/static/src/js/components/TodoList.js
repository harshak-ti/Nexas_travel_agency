// todo_list/static/src/js/components/TodoList.js

odoo.define('owl_demo.components.TodoList', function (require) {
    'use strict';
const { Component } = owl;

class TodoList extends Component {
    static template = 'owl_demo.TodoListTemplate';

    toggleDone(todo) {
        todo.done = !todo.done; // Toggle the done status
        this.render(); // Re-render the component
    }
}

return TodoList;
});