<script lang="ts">
	import { enhance } from '$app/forms';
	import type { SubmitFunction } from '@sveltejs/kit';

	export let data;
	export let form;

	let { session, supabase, profile } = data;
	$: ({ session, supabase, profile } = data);

	let profileForm: HTMLFormElement;
	let loading = false;
	let username: string = profile?.username ?? '';
	let avatarUrl: string = profile?.avatar_url ?? '';

	const handleSubmit: SubmitFunction = () => {
		loading = true;
		return async () => {
			loading = false;
		};
	};

	const handleSignOut: SubmitFunction = () => {
		loading = true;
		return async ({ update }) => {
			loading = false;
			update();
		};
	};
</script>

<div class="max-w-md mx-auto p-4 bg-white rounded shadow-lg lg:max-w-xl xl:max-w-2xl">
	<form
		class="space-y-4"
		method="post"
		action="?/update"
		use:enhance={handleSubmit}
		bind:this={profileForm}
	>
		<div>
			<label for="email" class="block text-gray-600">Email</label>
			<input
				id="email"
				type="text"
				value={session.user.email}
				disabled
				class="mt-1 p-2 w-full border rounded focus:outline-none focus:border-blue-500"
			/>
		</div>

		<div>
			<label for="username" class="block text-gray-600">Username</label>
			<input
				id="username"
				name="username"
				type="text"
				value={form?.username ?? username}
				class="mt-1 p-2 w-full border rounded focus:outline-none focus:border-blue-500"
			/>
		</div>

		<div>
			<input
				type="submit"
				class="w-full py-2 px-4 bg-blue-500 text-white rounded rounded-b-none cursor-pointer"
				value={loading ? 'Loading...' : 'Update'}
				disabled={loading}
			/>
		</div>
	</form>

	<form method="post" action="?/signout" use:enhance={handleSignOut}>
		<div>
			<button
				class="w-full py-2 px-4 bg-gray-300 text-gray-600 rounded rounded-t-none cursor-pointer"
				disabled={loading}
			>
				Sign Out
			</button>
		</div>
	</form>
</div>
