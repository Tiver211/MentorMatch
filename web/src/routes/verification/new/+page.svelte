<script lang="ts">
	let resendTimer = $state(60);

	setInterval(() => {
		resendTimer--;
	}, 1000);
</script>

<article>
	<h3>Верификация почты</h3>
	<p>
		Перейдите по ссылке в письме, отправленной вам на почту, указанную в форме регистрации. Если не
		можете найти письмо, проверьте папку «Спам».
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
