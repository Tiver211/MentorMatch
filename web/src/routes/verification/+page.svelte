<script lang="ts">
	import { browser } from '$app/environment';
	import { page } from '$app/state';

	let registrationToken: string | null;
	if (browser) {
		registrationToken = page.url.searchParams.get('token');
		if (!registrationToken) window.location.href = '/';
	}
</script>

{#if registrationToken}
	// Проверка токена
{:else}
	<article>
		<h1>Отсутствует токен</h1>
		<p>Возвращаю на главную</p>
	</article>
{/if}
