const selection = window.getSelection();

const target = selection.anchorNode.parentElement;

let element = document.createElement("div");

let text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam imperdiet mi tellus, non aliquet tortor porttitor eu. Cras eget tincidunt libero, in aliquam neque. Aliquam a pretium eros. Mauris sit amet mauris sagittis, porttitor orci a, suscipit velit. Nam at dolor lacinia, sodales quam ut, ullamcorper lectus.";

element.innerHTML = `
<style>
  .tldr-outer-wrapper {
    position: fixed;
    right: 5vw;
    z-index: 2;
    width: 30vw;
    display: flex;
    flex-direction: column;
    background-color: white;
    border: 4px solid black;
    box-shadow: 1em 1em 0 black;
    padding: 1em;
  }

  .tldr-wrapper {
    font-size: 1em;
  }
  .tldr-version {
    display: flex;
    justify-content: space-evenly;
  }
  .tldr-dot {
    display: block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background-color: white;
    border: 2px solid black;
    cursor: pointer;
  }
  .tldr-dot[selected] {
    background-color: black;
  }
</style>
<div class="tldr-outer-wrapper">
  <div class="tldr-wrapper">${text}</div>
  <div class="tldr-version">
    <div class="tldr-dot" selected></div>
    <div class="tldr-dot"></div>
    <div class="tldr-dot" style="display: flex; align-items: center; justify-content: center;">+</div>
  </div>
</div>
`;

document.body.appendChild(element);

setInterval(() => {
  element.querySelector('.tldr-outer-wrapper').style.top = `${target.getBoundingClientRect().top}px`;
}, 10);