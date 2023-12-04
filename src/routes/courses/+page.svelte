<script lang="ts">
	import CourseList from '$lib/components/CourseList.svelte';

	export let data;

	let { session, supabase, profile } = data;
	$: ({ session, supabase, profile } = data);

	let username: string = profile?.username ?? '';
	let avatarUrl: string = profile?.avatar_url ?? '';

	const divisions = {
		lower_div: 'Lower Division',
		sci_math: 'Science and Math',
		electives: 'Electives',
		upper_div: 'Upper Division',
		grad_reqs: 'Graduation Requirements'
	};

	// TODO: Load completions from Supabase
	let completions: any = profile?.completions ?? '{}';
</script>

<h1 class="text-3xl font-bold">Courses</h1>

<p class="mt-4 mb-8">
	Welcome to the course catalog! Here you can find all the courses required for a Comptute Science
	degree at California State University, Fullerton, as well as your progress towards completing
	them.
</p>

<div class="mb-12">
	{#each Object.entries(divisions) as [key, division]}
		<CourseList {data} {division} {completions} jsonFilePath={`/data/${key}.json`} />
	{/each}
</div>
