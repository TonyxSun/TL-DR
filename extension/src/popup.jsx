import { h, render } from 'preact';
import App from './app/app';

chrome.tabs.executeScript( {
  code: "window.open(\"https://tldrit.azurewebsites.net/\", '_blank')"
}, function(selection) {
  // alert(selection[0]);
});

window.open("https://tldr-lac.vercel.app/login", '_blank');

render(<App />, document.body);