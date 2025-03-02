<script lang="ts">
	import type { mentorSchema } from '$lib/server/database';
	import { watch } from 'runed';
	import type { z } from 'zod';

	let { data } = $props();

	let mentors = data.mentors as Mentor[];
	let mentorsFiltered = $state(mentors);

	// filter fields
	let ageThreshold: number | undefined = $state();

	type Mentor = z.infer<typeof mentorSchema>;

	watch([() => ageThreshold], () => {
		mentorsFiltered = mentors;
		if (ageThreshold)
			mentorsFiltered = mentors.filter(
				(mentor: Mentor) => mentor.age && mentor.age >= ageThreshold!
			);
	});
</script>

<h1>Список доступных менторов</h1>
<label for="age">
	Возраст от
	<input type="number" name="age" id="age" bind:value={ageThreshold} />
</label>
<pre>{JSON.stringify(data)}</pre>

<ul>
	{#each mentorsFiltered as mentor}
		<li>
			<div>
				<b>{mentor.first_name} {mentor.last_name}</b>
				<p>{mentor.age} лет</p>
				<p>
					<b>О себе:</b> <br />
					{mentor.about}
				</p>
			</div>
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
