<script lang="ts">
	let loggedIn = localStorage.getItem('loggedIn') ? true : false;
</script>

{#if loggedIn}
	<h1>Заявка на становление ментором</h1>
	<form action="" method="POST">
		<h3>В чем специализируютесь?</h3>
		<textarea name="direction" id="direction"></textarea>
		<button type="submit">Подать заявку</button>
	</form>
{:else}
	<h1>Необходима регистрация</h1>
	<h3>
		Для отправки заявки на становление ментором необходимо <a href="/signup">зарегистрироваться</a>.
	</h3>
{/if}
