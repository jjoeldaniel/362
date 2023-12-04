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

	// TODO: Load course completion data from Supabase
</script>

<p>hi {username}</p>

{#each Object.entries(divisions) as [key, division]}
	<CourseList {division} jsonFilePath={`/data/${key}.json`} />
{/each}
