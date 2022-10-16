import { h } from 'preact';

import style from './style.scss';

const Button = ({ onClick, children, ...props }) => (
  <div class={style.button} onClick={onClick}>{children}</div>
);

export default Button;