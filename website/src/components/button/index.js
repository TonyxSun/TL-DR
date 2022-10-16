import { h } from 'preact';

import style from './style.scss';

const Button = ({ children, ...props }) => (
  <div class={style.button}>{children}</div>
);

export default Button;