<script lang="ts">
	import type { z } from 'zod';
	import type { userSchema } from '$lib/schemas';
	import { watch } from 'runed';

	type User = z.infer<typeof userSchema>;

	let token: string | null = localStorage.getItem('token');
	let isAdmin = $state(false);

	let promise: any = $state();
	if (token) {
		promise = fetch('https://prod-team-35-lg7sic6v.final.prodcontest.ru/api/check', {
			method: 'POST',
			headers: {
				authorization: 'Bearer ' + token
			}
		}).then(async (response) => {
			if (response.ok) isAdmin = await response.json();
		});
	}
</script>

{#await promise}
	<h1>Проверка прав доступа</h1>
{:then}
	{#if isAdmin}
		<h1>Панель администратора</h1>
	{:else}
		<h1>Этот дом запривачен, разворачивайся.</h1>
	{/if}
{/await}
