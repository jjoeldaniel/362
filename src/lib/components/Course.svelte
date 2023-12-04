<!-- src/Course.svelte -->
<script lang="ts">
	export let name: string = 'Class';
	export let title: string = 'Title';
	export let description: string = 'Description';
	export let prerequisites: string[] = [];
	export let corequisites: string[] = [];
	export let credits: number = 0;
	export let completions: Map<string, boolean> = new Map();
	export let completed = completions.get(name) || false;
	export let data: any;

	let { session, supabase, profile } = data;
	$: ({ session, supabase, profile } = data);

	async function toggleCompletion() {
		completed = !completed;

		if (!completed) completions.delete(name);
		else completions.set(name, completed);

		// Update the user's completions in the database
		console.log(Object.fromEntries(completions));
		const { data, error } = await supabase
			.from('profiles')
			.update({
				completions: Object.fromEntries(completions)
			})
			.eq('username', profile.username);

		if (error) console.error('Error updating completions:', error);
		else console.log('Updated completions:', data);
	}
</script>

<div class="course {completed ? 'completed' : ''}">
	<h3>{name}</h3>
	<p><strong>Title:</strong> {title}</p>
	<p><strong>Description:</strong> {description}</p>
	<p><strong>Prerequisites:</strong> {prerequisites.join(', ')}</p>
	<p><strong>Corequisites:</strong> {corequisites.join(', ')}</p>
	<p><strong>Credits:</strong> {credits}</p>
	<button on:click={toggleCompletion}>
		{completed ? 'Mark Incomplete' : 'Mark Completed'}
	</button>
</div>

<style>
	.course {
		border: 1px solid #ccc;
		padding: 10px;
		margin: 10px;
		border-radius: 5px;
	}

	.completed {
		background-color: #d3f1ff; /* Light blue background for completed courses */
	}
	div {
		border: 1px solid #ccc;
		padding: 10px;
		margin: 10px;
		border-radius: 5px;
	}

	h3 {
		color: #007bff;
		cursor: pointer;
	}

	.completed {
		background-color: #d3f1ff; /* Light blue background for completed courses */
	}

	.course {
		margin-top: 5px;
	}
</style>
