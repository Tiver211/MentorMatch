<script lang="ts">
	let mentors = [
		{ name: 'Хто я?', age: 19, about: 'Гейдизайнер и разработчик на Godot' },
		{ name: 'Человек', age: 999, about: 'Профессиональный бездельник' }
	];
</script>

<ul>
	{#each mentors as { name, age, about }}
		<li>
			<b>{name}</b>
			<p>{age} лет</p>
			<p>
				<b>О себе:</b> <br />
				{about}
			</p>
		</li>
	{/each}
</ul>

<style>
	ul {
		padding: 1em 0;
	}

	li {
		padding: 0.5em;

		border: 1px solid black;
		border-radius: 0.5em;

		list-style: none;
	}

	p {
		margin-bottom: 0.1em;
	}
</style>
