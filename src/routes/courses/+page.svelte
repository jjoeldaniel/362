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

	// TODO: Load completedCourses from Supabase
	let completedCourses: Map<string, boolean> = new Map();
</script>

<p>hi {username}</p>

{#each Object.entries(divisions) as [key, division]}
	<CourseList {division} {completedCourses} jsonFilePath={`/data/${key}.json`} />
{/each}
