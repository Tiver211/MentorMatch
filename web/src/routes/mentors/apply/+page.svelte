<script lang="ts">
	let loggedIn = localStorage.getItem('loggedIn') ? true : false;
</script>

<h1>Заявка на становление ментором</h1>

{#if loggedIn}
	<form action="" method="POST">
		<h3>В чем специализируютесь?</h3>
		<textarea name="direction" id="direction"></textarea>
		<button type="submit">Подать заявку</button>
	</form>
{:else}
	<h3>Для становления ментором необходимо <a href="/signup">зарегистрироваться</a>.</h3>
{/if}
