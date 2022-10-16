import { h } from 'preact';

import style from './style.scss';

const InputText = ({ children, placeholder, ...props }) => (
  <div class={style.input}>
    <input type="text"></input>
    <span class={style.label}>{children}</span>
  </div>
);

export default InputText;