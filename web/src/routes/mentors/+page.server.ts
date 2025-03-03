import { get, mentorsArraySchema } from '$lib/server/database';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const mentors = await get('/mentors', mentorsArraySchema);
	if (!mentors) {
		error(500, 'Сервер не вернул список менторов. Возможно сервер отключен или недоступен.');
	}
	return { mentors };
};
