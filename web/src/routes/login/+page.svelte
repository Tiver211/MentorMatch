<hgroup>
	<h1>Вход в аккаунт</h1>
	<p>Нет аккаунта? <a href="/signup">Зарегистрируйтесь</a>.</p>
</hgroup>
<form method="POST">
	<label for="email">
		Электронная почта
		<input type="email" name="email" id="email" />
	</label>
	<label for="password">
		Пароль
		<input type="password" name="password" id="password" />
	</label>
	<button type="submit">Войти в аккаунт</button>
	<label for="hehehe">
		<h6 class="red">
			НЕ ДЛЯ ПРОДА! ЕСЛИ ЭТА КНОПКА ОСТАНЕТСЯ ЗДЕСЬ ПОСЛЕ ДД ВСЕМ РУКИ В БАРАНКУ СВЕРНУ!!!!!!!!!!
		</h6>
		<input
			type="button"
			id="hehehe"
			value="Взломать пентагон и войти без пароля"
			onclick={() => {
				localStorage.setItem('loggedIn', 'true');
				window.location.href = '/';
			}}
		/>
	</label>
</form>

<style>
	.red {
		padding: 0.25em;
		border-radius: 0.25em;

		color: white;
		background-color: red;
	}

	#hehehe {
		background-color: green;
	}
</style>
