import { h } from 'preact';

import style from './style.scss';

const InputText = ({ type, children, placeholder, ...props }) => {
  type = type || "text";
  return <div class={style.input}>
    <input type={type}></input>
    <span class={style.label}>{children}</span>
  </div>
};

export default InputText;