import { get, mentorSchema } from '$lib/server/database';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const mentor = await get('/mentors', mentorSchema, params.mentor_id);
	if (!mentor) {
		error(500, 'Сервер ушел за ментором и не вернулся. Возможно сервер отключен или недоступен.');
	}
	return { mentor };
};
