<script lang="ts">
	import { z } from 'zod';

	let loginParamsSchema = z.object({
		login: z.string(),
		password: z.string()
	});

	type LoginParams = z.infer<typeof loginParamsSchema>;

	let loginParams: LoginParams = {
		login: '',
		password: ''
	};

	let invalidCredentialsWarning: HTMLParagraphElement | undefined;

	let promise = $state();
	const onsubmit = (event: Event) => {
		event.preventDefault();
		if (invalidCredentialsWarning) invalidCredentialsWarning.hidden = true;
		promise = undefined;
		promise = fetch('/api/admin/secret-url', {
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

<h1>Вход в аккаунт администратора</h1>
<form method="POST" {onsubmit}>
	<label for="email">
		Логин
		<input type="email" name="email" id="email" />
	</label>
	<label for="password">
		Пароль
		<input type="password" name="password" id="password" />
	</label>
	<p id="invalid-credentials" bind:this={invalidCredentialsWarning} hidden>
		Неверный логин или пароль
	</p>
	<button type="submit">Войти в аккаунт</button>
</form>
