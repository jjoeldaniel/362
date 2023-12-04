<!-- CourseList.svelte -->
<script lang="ts">
	import { onMount } from 'svelte';
	import Course from './Course.svelte';

	export let division: string;
	export let jsonFilePath: string;
	export let completions: any = {};
	export let data: any;

	let showDetails = false;

	function toggleDetails() {
		showDetails = !showDetails;
	}

	let courses: Array<{
		title: string;
		description: string;
		prerequisites: string[];
		corequisites: string[];
		credits: number;
	}> = [];

	onMount(async () => {
		if (!jsonFilePath) {
			console.error('Please provide a valid JSON file path.');
			return;
		}

		try {
			const response = await fetch(jsonFilePath);

			if (!response.ok) {
				throw new Error(`Failed to fetch data (status ${response.status}).`);
			}

			courses = await response.json();
		} catch (error) {
			console.error('Error fetching data:', error);
		}
	});
</script>

<div class="mt-4">
	<button
		class="bg-blue-500 text-white py-2 px-4 rounded cursor-pointer transition duration-300 focus:outline-none focus:border-blue-700 focus:ring focus:ring-blue-200"
		on:click={toggleDetails}
	>
		{division}
	</button>

	{#if showDetails}
		<div class="mt-4 space-y-4">
			{#each Object.entries(courses) as [name, course]}
				<Course
					{data}
					{name}
					title={course.title}
					description={course.description}
					prerequisites={course.prerequisites}
					corequisites={course.corequisites}
					credits={course.credits}
					completed={completions[name] || false}
					{completions}
				/>
			{/each}
		</div>
	{/if}
</div>
