import type { Reroute } from '@sveltejs/kit';

export const reroute: Reroute = ({ url }) => {
	if (url.hostname.startsWith('app.')) {
		return `/app${url.pathname}`;
	}
};
