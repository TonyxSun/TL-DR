import { h } from 'preact';

import style from './style.scss';
import InputText from '../../components/input-text';
import Button from '../../components/button';
import { Link } from 'preact-router/match';

const Login = () => (
  <div class={style.login_outer_wrapper}>
    <div class={style.welcome}>Welcome</div>
    <div class={style.login_inner_wrapper}>
      <div class={style.heading}>
        <div class={style.header} selected>
          <span invisible>Login</span>
          <span>Login</span>
        </div>
        <div class={style.header}>
          <span invisible>Sign Up</span>
          <Link href="/register">Sign Up</Link>
        </div>
      </div>
      <div class={style.login}>
        <div class={style.item}>
          <InputText>Email</InputText>
        </div>
        <div class={style.item}>
          <InputText type="password">Password</InputText>
        </div>
        <div class={style.item}>
          <div class={style.submit}>
            <Button>Login</Button>
          </div>
        </div>
        <div class={style.item}>
          <div class={style.support}>
            <span>Forgot Password</span>
            <div class={style.divider}></div>
            <span>Send Request for Help</span>
          </div>
        </div>
      </div>
    </div>
  </div>
)

export default Login;