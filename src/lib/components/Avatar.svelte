<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let size: number;
	export let url: string;
	export let data: any;

	let { session, supabase, profile } = data;
	$: ({ session, supabase, profile } = data);

	let avatarUrl: string | null = null;
	let uploading = false;
	let files: FileList;

	const dispatch = createEventDispatcher();

	const downloadImage = async (path: string) => {
		try {
			const { data, error } = await supabase.storage.from('avatars').download(path);

			if (error) {
				throw error;
			}

			const url = URL.createObjectURL(data);
			avatarUrl = url;
		} catch (error) {
			if (error instanceof Error) {
				console.log('Error downloading image: ', error.message);
			}
		}
	};

	$: if (url) downloadImage(url);
</script>

<div style="width: {size}px" aria-live="polite">
	{#if avatarUrl}
		<img
			src={avatarUrl}
			alt={avatarUrl ? 'Avatar' : 'No image'}
			class="avatar image"
			style="height: {size}px, width: {size}px"
		/>
	{:else}
		<div class="avatar no-image" style="height: {size}px, width: {size}px" />
	{/if}
</div>
