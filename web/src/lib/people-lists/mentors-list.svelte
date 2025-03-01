<script lang="ts">
	import { watch } from 'runed';

	let { filter }: { filter?: boolean } = $props();

	let mentors = [
		{ name: 'Хто я?', age: 19, about: 'Гейдизайнер и разработчик на Godot' },
		{ name: 'Человек', age: 999, about: 'Профессиональный бездельник' }
	];
	let mentorsFiltered = $state(mentors);

	// filter fields
	let ageThreshold: number | undefined = $state();

	watch([() => ageThreshold], () => {
		mentorsFiltered = mentors;
		if (ageThreshold) mentorsFiltered = mentors.filter((mentor) => mentor.age >= ageThreshold!);
	});
</script>

{#if filter}
	<label for="age">
		Возраст от
		<input type="number" name="age" id="age" bind:value={ageThreshold} />
	</label>
{/if}
<ul>
	{#each mentorsFiltered as { name, age, about }}
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
		border-radius: 0.25em;

		list-style: none;
	}

	p {
		margin-bottom: 0.1em;
	}
</style>
