import { h } from 'preact';
import { Router } from 'preact-router';

import Header from './header';

// Code-splitting is automated for `routes` directory
import Home from '../routes/home';
import Login from '../routes/login';
import Register from '../routes/register';

const App = () => (
	<div id="app">
		<Router>
			<Home path="/" />
			<Login path="/login"></Login>
			<Register path="/register"></Register>
		</Router>
	</div>
)

export default App;
