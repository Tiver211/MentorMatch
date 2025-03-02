<script lang="ts">
	import '@picocss/pico';
	import '../../app.css';
	let { children } = $props();
</script>

<!-- <header>
	<div class="nav-container">
		<div class="logo">
			<p class="logo-title">MENTORMATCH</p>
		</div>
		<nav>
			{@render links()}
		</nav>
		<a href="/signup" class="auth-btn">
			<p>Авторизация</p>
		</a>
	</div>
</header> -->

{@render children()}

<!-- <footer>
	<div class="footer-links">
		{@render links()}
	</div>
	<p class="footer-notice">&copy; 2025 MentorMatch. Все права защищены.</p>
</footer>

{#snippet links()}
	<ul>
		<a href="/" class="active">Главная</a>
		<a href="/mentors">Наши менторы</a>
		<a href="/mentors/apply">Стать ментором</a>
		<a href="/profile">Профиль</a>
	</ul>
{/snippet} -->

<!-- <style lang="scss">
	header {
		display: flex;
		align-items: center;
		margin: 12px 0px;
		justify-content: center;

	}

	.nav-container {
		display: flex;
		gap: 120px;
		align-items: center;
	}

	ul {
		display: flex;
		margin: 4px;
		gap: 32px;
		text-decoration: none;
		padding-inline-start: 0px;


	}

	// button {
	// 	padding: 0;
	// }

	p {
		margin: 0;
	}


	a {
		text-decoration: none;
		color: black;
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
</style> -->
