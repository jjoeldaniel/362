<script>
	import '../app.css';
	import NavBar from '$lib/components/NavBar.svelte';
	import Constants from '$lib/constants.js';
</script>

<title>{Constants.APP_NAME}</title>

<div class="h-screen">
	<NavBar />
	<div class="flex mt-24">
		<div class="m-auto max-w-lg">
			<slot />
		</div>
	</div>
</div>
