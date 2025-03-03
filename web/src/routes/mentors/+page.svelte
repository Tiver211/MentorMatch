<script lang="ts">
	import type { mentorSchema } from '$lib/schemas.js';
	import { onMount } from 'svelte';
	import type { z } from 'zod';

	let mentors: Mentor[] = $state([]);

	// filter fields
	let ageThreshold: number | undefined = $state();

	type Mentor = z.infer<typeof mentorSchema>;

	onMount(() => {
		fetch('https://prod-team-35-lg7sic6v.final.prodcontest.ru/api/mentors').then(
			async (response) => {
				if (!response.ok) {
					throw new Error('fafs');
				}
				mentors = await response.json();
			}
		);
	});
</script>

{#if mentors && mentors.length !== 0}
	<h1>Список доступных менторов</h1>
	<label for="age">
		Возраст от
		<input type="number" name="age" id="age" bind:value={ageThreshold} />
	</label>
{:else}
	<h1>На данный момент отсутствуют доступные менторы</h1>
{/if}

<ul>
	{#each mentors as mentor}
		<li>
			<div class="row">
				<div>
					<b>{mentor.first_name} {mentor.last_name}</b>
					<p>{mentor.age} лет</p>
					<p>
						<b>О себе:</b> <br />
						{mentor.about}
					</p>
				</div>
				<button
					onclick={() => {
						window.location.href = '/mentors/profile?mentor_id=' + mentor.mentor_id;
					}}>Открыть профиль</button
				>
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

	.row {
		display: flex;
		justify-content: space-between;
		align-items: flex-start;
	}
</style>
