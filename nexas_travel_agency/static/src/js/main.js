import { Component, mount } from 'owl';
import YourComponent from './components/sample';

function start() {
    mount(YourComponent, { target: document.body });
}

start();
