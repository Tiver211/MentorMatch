<script lang="ts">
	import { browser } from '$app/environment';

	let loggedIn: boolean = $state(false);
	let isAdmin: boolean = $state(false);
	if (browser) {
		loggedIn = localStorage.getItem('loggedIn') ? true : false;
		isAdmin = localStorage.getItem('isAdmin') ? true : false;
	}
</script>

{#if loggedIn && isAdmin}
	<h1>Велкам ту зе клаб, бади</h1>
{:else}
	<h1>Этот дом запривачен, разворачивайся.</h1>
{/if}
