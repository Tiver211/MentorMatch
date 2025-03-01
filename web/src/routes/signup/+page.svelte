<script lang="ts">
	let step = $state(0);
	let isStepValid = $state(false);

	let required: Array<HTMLInputElement> = $state([]);
	const oninput = () => {
		for (let i = 0; i < required.length; i++) {
			required[i].ariaInvalid = 'false';
		}
		for (let i = 0; i < required.length; i++) {
			if (!required[i].value || required[i].value === '') {
				required[i].ariaInvalid = 'true';
				isStepValid = false;
				return;
			}
		}

		isStepValid = true;
	};
</script>

<h1>Регистрация пользователя</h1>
{#if step === 0}
	<fieldset class="grid">
		<label for="first-name">
			Ваше имя*
			<input type="text" name="first-name" id="first-name" {oninput} bind:this={required[0]} />
		</label>
		<label for="last-name">
			Фамилия
			<input type="text" name="last-name" id="last-name" {oninput} />
		</label>
	</fieldset>

	<label for="age">
		Возраст*
		<input type="number" min="6" max="192" name="age" id="age" {oninput} bind:this={required[1]} />
	</label>
{:else if step === 1}
	<label for="about"> </label>Напишите немного информации о себе
	<textarea name="about" id="about"> </textarea>
{:else}
	<p>Регистрация окончена</p>
{/if}

<input
	disabled={!isStepValid}
	type="button"
	value={step < 1 ? 'Продолжить' : 'Создать аккаунт'}
	onclick={() => {
		if (step >= 1) {
			window.location.href = '/mentors';
			return;
		}
		step++;
	}}
/>

<style>
	fieldset {
		margin-bottom: 0;
	}
</style>
