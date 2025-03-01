import type { Reroute } from '@sveltejs/kit';

export const reroute: Reroute = ({ url }) => {
	if (url.href.endsWith(url.host + '/')) {
		return '/landing';
	}
};
