<script lang="ts">
	import { Auth } from '@supabase/auth-ui-svelte';
	import { ThemeSupa } from '@supabase/auth-ui-shared';

	export let data;
</script>

<div class="flex flex-col items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
	<div>
		<h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 mb-8">Login</h2>
	</div>
	<div class="col-6 form-widget">
		<Auth
			supabaseClient={data.supabase}
			view="magic_link"
			redirectTo={`${data.url}/auth/callback`}
			showLinks={false}
			appearance={{ theme: ThemeSupa, style: { input: 'color: #000' } }}
			providers={['github', 'discord']}
			socialLayout="horizontal"
		/>
	</div>
</div>
