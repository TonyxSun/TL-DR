import { h } from 'preact';

import style from './style.scss';
import InputText from '../../components/input-text';
import Button from '../../components/button';
import { Link } from 'preact-router/match';

const Register = () => (
  <div class={style.login_outer_wrapper}>
    <div class={style.welcome}>Welcome</div>
    <div class={style.login_inner_wrapper}>
      <div class={style.heading}>
        <div class={style.header}>
          <span invisible>Login</span>
          <Link href="/login">Login</Link>
        </div>
        <div class={style.header} selected>
          <span invisible>Sign Up</span>
          <span>Sign Up</span>
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
          <InputText type="password">Confirm Password</InputText>
        </div>
        <div class={style.item}>
          <InputText>Phone Number</InputText>
        </div>
        <div class={style.item}>
          <div class={style.submit}>
            <Button>Register</Button>
          </div>
        </div>
        <div class={style.item}>
          <div class={style.support}>
            <span>Privacy Policy</span>
            <div class={style.divider}></div>
            <span>Terms of Service</span>
          </div>
        </div>
      </div>
    </div>
  </div>
)

export default Register;