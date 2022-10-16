import { h } from 'preact';
import InputText from '../../components/input-text';
import style from './style.scss';
import Button from '../../components/button'

const Home = () => (
	
	<div class={style.home_outside}>
		<div class={style.background_text}>Hello, everyone! This is the LONGEST TEXT EVER! I was inspired by the various other "longest texts ever" on the internet, and I wanted to make my own. So here it is! This is going to be a WORLD RECORD! This is actually my third attempt at doing this. The first time, I didn't save it. Made with love by Wilson N., Darlnim P., Tony S., Maanuj V. The second time, the Neocities editor crashed. Now I'm writing this in Notepad, then copying it into the Neocities editor instead of typing it directly in the Neocities editor to avoid crashing. It sucks that my past two attempts are gone now. Those actually got pretty long. Not the longest, but still pretty long. I hope this one won't get lost somehow. Anyways, let's talk about WAFFLES! I like waffles. Waffles are cool. Waffles is a funny word. There's a Teen Titans Go episode called "Waffles" where the word "Waffles" is said a hundred-something times. It's pretty annoying. There's also a Teen Titans Go episode about Pig Latin. Don't know what Pig Latin is? It's a language where you take all the consonants before the first vowel, move them to the end, and add '-ay' to the end. If the word begins with a vowel, you just add '-way' to the end. For example, "Waffles" becomes "Afflesway". I've been speaking Pig Latin fluently since the fourth grade, so it surprised me when I saw the episode for the first time. I speak Pig Latin with my sister sometimes. It's pretty fun. I like speaking it in public so that everyone around us gets confused. That's never actually happened before, but if it ever does, 'twill be pretty funny. By the way, "'twill" is a word I invented recently, and it's a contraction of "it will". I really hope it gains popularity in the near future, because "'twill" is WAY more fun than saying "it'll". "It'll" is too boring. Nobody likes boring.</div>
		<div class={style.home_title}>TL;DR</div>
		<div class={style.home_inside}>
			<div class={style.textbox}>
				<textarea placeholder = "Put a link or a text here."></textarea>
			</div>
			<div class={style.buttons}>
				<div class={style.item}>
					<Button>Let's tldr it!</Button>
				</div>
			</div>
		</div>
	</div>
	
);

export default Home;
