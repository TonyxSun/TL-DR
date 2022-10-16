chrome.contextMenus.create({
  title: "TLDR!",
  contexts:["selection"],
  onclick: (word, tab) => {
    // chrome.tabs.executeScript(tab.id, {file: "getDOM.js"})
    chrome.tabs.executeScript(tab.id, {
      file: '/inject.js'
      // code: "window.getSelection()"
    }, (selection) => {
      console.log(selection);
    });
  }
});