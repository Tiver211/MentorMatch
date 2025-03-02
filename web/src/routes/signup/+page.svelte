<script lang="ts">
	import { watch } from 'runed';

	let isVerificationWindowShown = $state(false);
	let resendTimer = $state(60);

	watch([() => isVerificationWindowShown], () => {
		if (isVerificationWindowShown) {
			window.scrollTo(0, 0);
			setInterval(() => {
				resendTimer--;
			}, 1000);
		}
	});
</script>

<h1>Регистрация пользователя</h1>

{#if !isVerificationWindowShown}
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
				isVerificationWindowShown = true;
			}}>Завершить регистрацию</button
		>
	</form>
{:else}
	<article>
		<h3>Верификация почты</h3>
		<p>
			Перейдите по ссылке в письме, отправленной вам на почту, указанную в форме регистрации. Если
			не можете найти письмо, проверьте папку «Спам».
		</p>
		<input
			type="button"
			value={resendTimer <= 0
				? 'Отправить письмо заново'
				: 'Повторная отправка будет доступна через ' + resendTimer + ' секунд'}
			disabled={resendTimer > 0}
			onclick={() => {
				resendTimer = 60;
			}}
		/>
		<input
			type="button"
			value="Проверить верификацию"
			onclick={() => {
				localStorage.setItem('loggedIn', 'true');
				window.location.href = '/';
			}}
		/>
	</article>
{/if}

<style>
	fieldset {
		margin-bottom: 0;
	}
</style>
