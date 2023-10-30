<script>
	import '../app.css';
	import NavBar from '$lib/components/NavBar.svelte';
	import Constants from '$lib/constants.js';
</script>

<div class="h-screen">
	<NavBar />
	<div class="flex mt-24">
		<div class="m-auto max-w-lg">
			<h1 class="pb-4 text-4xl font-semibold">{Constants.APP_NAME}</h1>
			<blockquote class="pb-8 text-xl font-medium italic">What a cool project.</blockquote>
			<slot />
		</div>
	</div>
</div>
