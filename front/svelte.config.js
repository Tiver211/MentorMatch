import adapter from '@sveltejs/adapter-auto';
import { scss } from 'svelte-preprocess';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: [scss(), vitePreprocess()],

	kit: {
		adapter: adapter()
	}
};

export default config;
