<script lang="ts">
	import Avatar from '$lib/components/Avatar.svelte';
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

<h1 class="text-3xl font-bold mb-4">Courses</h1>

<div class="bg-gray-800 p-6 rounded-lg flex items-center space-x-4">
	<Avatar {data} bind:url={avatarUrl} size={150} />

	<div>
		<h2 class="text-3xl md:text-4xl text-center pl-5 font-bold text-white">Welcome, {username}!</h2>
	</div>
</div>

<p class="mt-8 mb-4 text-gray-800">
	Welcome to the course catalog! Here you can find all the courses required for a Computer Science
	degree at California State University, Fullerton, as well as your progress towards completing
	them.
</p>

<div class="mb-12">
	{#each Object.entries(divisions) as [key, division]}
		<CourseList {data} {division} {completions} jsonFilePath={`/data/${key}.json`} />
	{/each}
</div>
