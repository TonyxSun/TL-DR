(async function(){
  const selection = window.getSelection();

  const target = selection.anchorNode.parentElement;

  let element = document.createElement("div");

  let { response, sentiment_obj, tldr } = await (await fetch('https://tldrit.azurewebsites.net/analyze', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user_id: null,
      input_data: selection.toString()
    })
  })).json();

  if (!response.success) return console.log("FAIL");
  
  const text = tldr;
  
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
      margin-bottom: 1em;
    }

    .tldr-wrapper-custom textarea {
      outline: none;
      border: none;
      background-color: transparent;
      font-size: 1em;
      resize: none;
      height: 30vh;
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
      color: white;
    }

    .tldr-button {
      padding: 0.5em 0;
      font-size: 1em;
      border: 4px solid black;
      box-shadow: 0.5em 0.5em 0 black;
      color: black;
      letter-spacing: 0.2em;
      width: 80%;
      text-align: center;
      cursor: pointer;
      user-select: none;
      transition: 0.2s ease all;
      margin: auto;
      margin-bottom: 2em;
    }

    .tldr-button:hover {
      box-shadow: 0.25em 0.25em 0 black;
    }

    .tldr-button:active {
      transition: 0.1s ease all;
      background-color: black;
      color: white;
      box-shadow: 0 0 0 black;
    }

    .tldr-pi {
      height: 2em;
      margin-bottom: 1em;
    }

  </style>
  <div class="tldr-outer-wrapper">
    <svg class="tldr-pi" viewBox="-1 -1 2 2" style="transform: rotate(-90deg)"></svg>
    <div class="tldr-wrapper">${text}</div>
    <div class="tldr-wrapper-custom" hidden>
      <textarea placeholder="Your Own TLDR"></textarea>
      <div class="tldr-button">Submit!</div>
    </div>
    <div class="tldr-version">
      <div class="tldr-dot" selected></div>
      <div class="tldr-dot"></div>
      <div id="tldr-custom" class="tldr-dot" style="display: flex; align-items: center; justify-content: center;">+</div>
    </div>
  </div>
  `;
  
  document.body.appendChild(element);


  const svgEl = document.querySelector('svg');
  const slices = [
    { percent: sentiment_obj['positive'], color: '#00A86B' },
    { percent: sentiment_obj['neutral'], color: '#CCCDC6' },
    { percent: sentiment_obj['negative'], color: '#ff7272' },
  ];
  let cumulativePercent = 0;

  function getCoordinatesForPercent(percent) {
    const x = Math.cos(2 * Math.PI * percent);
    const y = Math.sin(2 * Math.PI * percent);
    return [x, y];
  }

  slices.forEach(slice => {
    // destructuring assignment sets the two variables at once
    const [startX, startY] = getCoordinatesForPercent(cumulativePercent);
    
    // each slice starts where the last slice ended, so keep a cumulative percent
    cumulativePercent += slice.percent;
    
    const [endX, endY] = getCoordinatesForPercent(cumulativePercent);

    // if the slice is more than 50%, take the large arc (the long way around)
    const largeArcFlag = slice.percent > .5 ? 1 : 0;

    // create an array and join it just for code readability
    const pathData = [
      `M ${startX} ${startY}`, // Move
      `A 1 1 0 ${largeArcFlag} 1 ${endX} ${endY}`, // Arc
      `L 0 0`, // Line
    ].join(' ');

    // create a <path> and append it to the <svg> element
    const pathEl = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    pathEl.setAttribute('d', pathData);
    pathEl.setAttribute('fill', slice.color);
    svgEl.appendChild(pathEl);
  });


  const wrapper = element.querySelector('.tldr-wrapper');
  const custom = element.querySelector('.tldr-wrapper-custom');

  element.querySelector('.tldr-button').onclick = () => {
    element.querySelector('[selected]').removeAttribute('selected')
    custom.setAttribute('hidden', '');
    wrapper.removeAttribute('hidden');
    element.querySelectorAll('.tldr-dot')[1].setAttribute('selected', '');
    wrapper.innerText = custom.querySelector('textarea').value;
  };

  element.querySelector('#tldr-custom').onclick = () => {
    element.querySelector('[selected]').removeAttribute('selected')
    element.querySelector('#tldr-custom').setAttribute('selected', '');
    wrapper.setAttribute('hidden', '');
    custom.removeAttribute('hidden');
  };
  
  setInterval(() => {
    element.querySelector('.tldr-outer-wrapper').style.top = `${target.getBoundingClientRect().top}px`;
  }, 10);
})();