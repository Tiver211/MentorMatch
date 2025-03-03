<script lang="ts">
	import '../pico.indigo.min.css';
	import '../app.css';
	import { browser } from '$app/environment';
	let { children } = $props();

	let loggedIn: boolean = $state(false);
	let isAdmin: boolean = $state(false);
	if (browser) {
		loggedIn = localStorage.getItem('loggedIn') ? true : false;
		isAdmin = localStorage.getItem('isAdmin') ? true : false;
	}
</script>

<header>
	<div class="nav-container">
		<div class="logo">
			<p class="logo-title">MENTORMATCH</p>
		</div>
		<nav>
			{@render links()}
		</nav>
		<a href={loggedIn ? '/profile' : '/login'} class="auth-btn">
			<p>{loggedIn ? 'Профиль' : 'Авторизация'}</p>
		</a>
	</div>
</header>

<div class="container">
	{@render children()}
</div>

<footer>
	<div class="footer-links">
		{@render links()}
	</div>
	<p class="footer-notice">&copy; 2025 MentorMatch. Все права защищены.</p>
</footer>

{#snippet links()}
	<ul>
		<li>
			<a href="/" class="active">Главная</a>
		</li>
		<li>
			<a href="/mentors">Наши менторы</a>
		</li>
		<li>
			<a href="/mentors/apply">Стать ментором</a>
		</li>
		{#if isAdmin}
			<li>
				<a href="/admin">Админ-панель</a>
			</li>
		{/if}
	</ul>
{/snippet}

<style>
	.container {
		margin-top: 1em;
	}

	header {
		width: 100%;

		display: flex;
		align-items: center;
		margin: 12px 0px;
		justify-content: center;

		transform: scale(1.2);
	}

	.nav-container {
		width: 75%;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	ul {
		display: flex;
		margin: 4px;
		gap: 1em;
		text-decoration: none;
		padding-inline-start: 0px;
	}

	li {
		list-style: none;
		padding: 0;
	}

	/* // button {
	// 	padding: 0;
	// } */

	p {
		margin: 0;
	}

	a {
		text-decoration: none;
		font-size: 16px;
		font-weight: 400;
	}

	.logo-title {
		font-size: 16px;
		font-weight: 600;
	}

	footer {
		margin-top: 32px;
		display: block;
		justify-content: center;
	}

	.footer-links {
		display: flex;
		gap: 32px;
		justify-content: center;
	}

	.footer-notice {
		margin-top: 20px;
		display: flex;
		color: #707070;
		justify-content: center;
		font-size: 16px;
	}
</style>
