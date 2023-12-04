<!-- src/Course.svelte -->
<script lang="ts">
	export let name: string = 'Class';
	export let title: string = 'Title';
	export let description: string = 'Description';
	export let prerequisites: string[] = [];
	export let corequisites: string[] = [];
	export let credits: number = 0;
	export let completions: any = {};
	export let completed = completions[name] || false;
	export let data: any;

	let { session, supabase, profile } = data;
	$: ({ session, supabase, profile } = data);

	async function toggleCompletion() {
		completed = !completed;

		if (!completed) delete completions[name];
		else completions[name] = completed;

		// Update the user's completions in the database
		console.log(completions);
		const { data, error } = await supabase
			.from('profiles')
			.update({
				completions: completions
			})
			.eq('username', profile.username);

		if (error) console.error('Error updating completions:', error);
		else console.log('Updated completions:', data);
	}
</script>

<div class="course border p-4 rounded transition {completed ? 'bg-blue-100' : ''}">
	<h3 class="text-blue-500 cursor-pointer">{name}</h3>
	<p><strong>Title:</strong> {title}</p>
	<p><strong>Description:</strong> {description}</p>
	<p><strong>Prerequisites:</strong> {prerequisites.join(', ')}</p>
	<p><strong>Corequisites:</strong> {corequisites.join(', ')}</p>
	<p><strong>Credits:</strong> {credits}</p>
	<button
		class="py-2 px-4 bg-blue-500 text-white rounded mt-4 cursor-pointer"
		on:click={toggleCompletion}
	>
		{completed ? 'Mark Incomplete' : 'Mark Completed'}
	</button>
</div>
