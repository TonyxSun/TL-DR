import { h } from 'preact';
import { useState } from 'preact/hooks';

import style from './style.scss';
import InputText from '../../components/input-text';
import Button from '../../components/button';
import { Link } from 'preact-router/match';

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  // const [confirmPassword, setConfirmPassword] = useState("");
  const [phone, setPhone] = useState("");
  const [success, setSuccess] = useState(false);


  const onClick = async () => {

    let { success } = await (await fetch('https://tldrit.azurewebsites.net/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        user_email: email,
        user_password: password,
        user_phone: phone
      })
    })).json();

    console.log(success);

    setSuccess(success);
  };


  return <div class={style.login_outer_wrapper}>
    {
      success ? 
      <div class={style.success}>
        <Button onClick={() => {setSuccess(false)}}>Successful!</Button>
      </div>
      : ''
    }
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
          <InputText value={email} onInput={(e) => setEmail(e.target.value)}>Email</InputText>
        </div>
        <div class={style.item}>
          <InputText type="password" value={password} onInput={(e) => setPassword(e.target.value)}>Password</InputText>
        </div>
        <div class={style.item}>
          <InputText type="password">Confirm Password</InputText>
        </div>
        <div class={style.item}>
          <InputText value={phone} onInput={(e) => setPhone(e.target.value)}>Phone Number</InputText>
        </div>
        <div class={style.item}>
          <div class={style.submit}>
            <Button onClick={onClick}>Register</Button>
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
};

export default Register;