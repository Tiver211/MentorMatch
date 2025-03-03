import { get } from '$lib/server/api';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { mentorSchema } from '$lib/schemas';

export const load: PageServerLoad = async ({ params }) => {
	const mentor = await get('/mentors', mentorSchema, params.mentor_id);
	if (!mentor) {
		error(500, 'Сервер ушел за ментором и не вернулся. Возможно сервер отключен или недоступен.');
	}
	return { mentor };
};
