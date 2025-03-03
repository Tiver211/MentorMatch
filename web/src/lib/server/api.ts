import { z } from 'zod';

const baseUrl = 'https://prod-team-35-lg7sic6v.final.prodcontest.ru';

export const get = async (
	apiUrl: string,
	schema: z.ZodSchema,
	pathParam?: string,
	urlParams?: {
		key: string;
		value: string;
	}[]
) => {
	const queryString = urlParams
		? '?' + urlParams.map((param) => `${param.key}=${param.value}`).join('&')
		: '';
	const url = [baseUrl, apiUrl, pathParam ? '/' + pathParam : '', queryString].join('');

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
	body: object,
	schema?: z.ZodSchema<T>
): Promise<T | undefined> => {
	const url = baseUrl + apiUrl;
	try {
		const response = await fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(body)
		});

		if (!response.ok) {
			throw new Error('HTTP error! Status: ' + response.status);
		}

		const data = await response.json();
		let dataToReturn = data;
		if (schema) dataToReturn = schema.parse(data);

		return dataToReturn;
	} catch (error) {
		console.error('Error in POST request:', error);
		return undefined;
	}
};
