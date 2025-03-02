<hgroup>
	<h1>Регистрация пользователя</h1>
	<p>Уже есть аккаунт? <a href="/login">Войдите</a> в него.</p>
</hgroup>

<form action="/signup" method="POST">
	<h3>Личная информация</h3>
	<fieldset class="grid">
		<label for="first-name">
			Имя*
			<input type="text" name="first-name" id="first-name" required />
		</label>
		<label for="last-name">
			Фамилия
			<input type="text" name="last-name" id="last-name" />
		</label>
		<label for="age">
			Возраст
			<input type="number" name="age" id="age" pattern="^(0?[0-9]?[0-9]|1[01][0-9]|120)$" />
		</label>
	</fieldset>
	<label for="about">
		<h3>Напишите немного информации о себе</h3>
		<textarea name="about" id="about"></textarea>
	</label>
	<label for="contact">
		<h3>Как с вами можно связаться?</h3>
		<textarea name="contact" id="contact"></textarea>
	</label>
	<h3>Данные авторизации</h3>
	<fieldset class="grid">
		<label for="email">
			Электронная почта*
			<input type="email" name="email" id="email" required />
		</label>
		<label for="password">
			Пароль*
			<input type="password" name="password" id="password" required />
		</label>
	</fieldset>
	<button
		type="submit"
		onclick={() => {
			window.location.href = '/verification/new';
		}}>Завершить регистрацию</button
	>
</form>

<style>
	fieldset {
		margin-bottom: 0;
	}
</style>
