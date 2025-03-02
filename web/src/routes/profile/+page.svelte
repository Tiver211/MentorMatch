<h1>Управление аккантом</h1>
<input
	type="button"
	value="Выйти из аккаунта"
	onclick={() => {
		localStorage.removeItem('loggedIn');
	}}
/>
