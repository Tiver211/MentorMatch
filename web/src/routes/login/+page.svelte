<script lang="ts">
	import { z } from 'zod';

	let loginParamsSchema = z.object({
		login: z.string(),
		password: z.string()
	});

	type LoginParams = z.infer<typeof loginParamsSchema>;

	let loginParams: LoginParams = $state({
		login: '',
		password: ''
	});

	let invalidCredentialsWarning: HTMLParagraphElement | undefined;

	let promise = $state();
	const onsubmit = (event: Event) => {
		event.preventDefault();
		if (invalidCredentialsWarning) invalidCredentialsWarning.hidden = true;
		promise = undefined;
		promise = fetch('https://prod-team-35-lg7sic6v.final.prodcontest.ru/api/user/auth/sign-in', {
			method: 'POST',
			body: JSON.stringify(loginParams),
			headers: {
				'Content-type': 'application/json; charset=UTF-8'
			}
		}).then((response) => {
			if (!response.ok) {
				if (response.status === 422 && invalidCredentialsWarning) {
					invalidCredentialsWarning.hidden = false;
				}
			}
		});
	};
</script>

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
