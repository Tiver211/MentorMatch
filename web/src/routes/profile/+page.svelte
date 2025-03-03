<script lang="ts">
	import type { userSchema } from '$lib/schemas';
	import type { z } from 'zod';

	type User = z.infer<typeof userSchema>;

	let token: string | null = localStorage.getItem('token');
	let user: User | undefined = $state();

	let promise: any = $state();
	if (token) {
		promise = fetch('https://prod-team-35-lg7sic6v.final.prodcontest.ru/api/user/profile', {
			method: 'GET',
			headers: {
				authorization: token
			}
		}).then(async (response) => {
			user = await response.json();
		});
	}
</script>

{#if promise}
	{#await promise}
		<h1>Проверка авторизации</h1>
	{:then}
		{#if user}
			<h1>Управление аккантом</h1>
			<input
				type="button"
				value="Редактировать аккаунт"
				onclick={() => {
					window.location.href = '/profile/edit';
				}}
			/>
			<input
				type="button"
				value="Выйти из аккаунта"
				onclick={() => {
					localStorage.removeItem('isAdmin');
					localStorage.removeItem('loggedIn');
					window.location.href = '/';
				}}
				class="red"
			/>
		{/if}
	{:catch}
		<h1>Что-то пошло не так</h1>
		<input
			type="button"
			value="Повторить проверку"
			onclick={() => {
				window.location.reload();
			}}
		/>
	{/await}
{:else}
	<h1>Вы не вошли в акканут</h1>
	<input
		type="button"
		value="Авторизация"
		onclick={() => {
			window.location.href = '/login';
		}}
	/>
{/if}

<style>
	.red {
		background-color: #be3144;
		border: none;
	}
</style>
