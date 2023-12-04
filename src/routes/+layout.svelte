<script>
	import '../app.css';
	import NavBar from '$lib/components/NavBar.svelte';
	import Constants from '$lib/constants.js';
	import { invalidate } from '$app/navigation';
	import { onMount } from 'svelte';

	export let data;

	let { supabase, session } = data;
	$: ({ supabase, session } = data);

	onMount(() => {
		const { data } = supabase.auth.onAuthStateChange((event, _session) => {
			if (_session?.expires_at !== session?.expires_at) {
				invalidate('supabase:auth');
			}
		});

		return () => data.subscription.unsubscribe();
	});

	let loggedIn = false;

	if (session) {
		loggedIn = true;
	}
</script>

<title>{Constants.APP_NAME}</title>

<div class="h-screen">
	<NavBar loggedIn />
	<div class="flex mt-24">
		<div class="m-auto max-w-lg px-3 md:px-0">
			<slot />
		</div>
	</div>
</div>
