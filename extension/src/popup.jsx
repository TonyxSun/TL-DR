import { h, render } from 'preact';
import App from './app/app';

chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
  alert(selection[0]);
});

render(<App />, document.body);