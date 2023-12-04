<!-- CourseList.svelte -->
<script lang="ts">
	import { onMount } from 'svelte';
	import Course from './Course.svelte';

	export let division: string;
	export let jsonFilePath: string;
	export let completions: Map<string, boolean> = new Map();
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

<div>
	<button on:click={toggleDetails}>
		{division}
	</button>
	{#if showDetails}
		{#each Object.entries(courses) as [name, course]}
			<Course
				{data}
				{name}
				title={course.title}
				description={course.description}
				prerequisites={course.prerequisites}
				corequisites={course.corequisites}
				credits={course.credits}
				completed={completions.get(name) || false}
				{completions}
			/>
		{/each}
	{/if}
</div>

<style>
	/* Styling for the button */
	button {
		background-color: #007bff;
		color: white;
		padding: 10px;
		border: none;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	button:hover {
		background-color: #0056b3;
	}

	/* Styling for the container */
	div {
		margin: 20px;
	}

	/* Add focus styling for better accessibility */
	button:focus {
		outline: 2px solid #0056b3;
	}
</style>
