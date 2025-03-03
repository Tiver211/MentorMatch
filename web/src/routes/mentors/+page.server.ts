import { get } from '$lib/server/api';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { mentorsArraySchema } from '$lib/schemas';

export const load: PageServerLoad = async () => {
	const mentors = await get('/mentors', mentorsArraySchema);
	if (!mentors) {
		error(500, 'Сервер не вернул список менторов. Возможно сервер отключен или недоступен.');
	}
	return { mentors };
};
