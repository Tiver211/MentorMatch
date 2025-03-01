<script lang="ts">
	import '@picocss/pico';
	import '../app.css';
	let { children } = $props();
</script>

<div class="container">
	{@render children()}
</div>

<style>
	.container {
		margin-top: 1em;
	}
</style>
