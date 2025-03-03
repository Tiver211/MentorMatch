<h1>Управление аккантом</h1>
<input
	type="button"
	value="Выйти из аккаунта"
	onclick={() => {
		localStorage.removeItem('isAdmin');
		localStorage.removeItem('loggedIn');
		window.location.href = '/';
	}}
/>
<h6 class="red">
	НЕ ДЛЯ ПРОДА! ЕСЛИ ЭТА КНОПКА ОСТАНЕТСЯ ЗДЕСЬ ПОСЛЕ ДД ВСЕМ РУКИ В БАРАНКУ СВЕРНУ!!!!!!!!!!
</h6>
<input
	type="button"
	id="hehehe"
	value="Выдать админку бесплатно, без регистрации и смс"
	onclick={() => {
		localStorage.setItem('isAdmin', 'true');
	}}
/>

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
