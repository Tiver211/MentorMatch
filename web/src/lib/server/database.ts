import { z } from 'zod';

export const mentorSchema = z.object({
	mentor_id: z.string().uuid().optional(),
	first_name: z.string().optional(),
	last_name: z.string().optional(),
	age: z.number().int().min(0).max(125).optional(),
	direction: z.string().optional(),
	about: z.string().optional(),
	contact: z.string().optional()
});

export const mentorsArraySchema = z.array(mentorSchema);

const baseUrl = 'https://prod-team-35-lg7sic6v.final.prodcontest.ru';

export const get = async (apiUrl: string, schema: z.ZodSchema) => {
	const url = baseUrl + apiUrl;
	try {
		const response = await fetch(url);
		if (!response.ok) {
			throw new Error('HTTP error! Status: ' + response.status);
		}

		const data = await response.json();

		const dataToReturn = schema.parse(data);

		return dataToReturn;
	} catch (error) {
		console.log(error);
		return undefined;
	}
};

export const post = async <T>(
	apiUrl: string,
	payload: unknown,
	schema: z.ZodSchema<T>
): Promise<T | undefined> => {
	const url = baseUrl + apiUrl;
	try {
		const response = await fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(payload)
		});

		if (!response.ok) {
			throw new Error('HTTP error! Status: ' + response.status);
		}

		const data = await response.json();
		const dataToReturn = schema.parse(data);

		return dataToReturn;
	} catch (error) {
		console.error('Error in POST request:', error);
		return undefined;
	}
};
