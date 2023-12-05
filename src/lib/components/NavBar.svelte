<script>
	let isMenuOpen = false;

	function toggleMenu() {
		isMenuOpen = !isMenuOpen;
	}

	export let loggedIn = false;

	import Constants from '$lib/constants.js';
</script>

<nav class="flex items-center justify-between flex-wrap bg-gray-800 p-6">
	<div class="flex items-center flex-shrink-0 text-white mr-6">
		<a href="/"><span class="font-semibold text-xl tracking-tight">{Constants.APP_NAME}</span></a>
	</div>
	<div class="block md:hidden">
		<button
			class="flex items-center px-3 py-2 border rounded text-gray-200 border-gray-400 hover:text-white hover:border-white"
			on:click={toggleMenu}
		>
			<svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
				<title>Menu</title>
				<path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
			</svg>
		</button>
	</div>

	{#if isMenuOpen}
		<div class="w-full flex flex-row md:hidden flex-grow">
			<div class="text-lg flex flex-row">
				<a href="/courses" class="block mt-4 text-gray-200 hover:text-white mr-4"> Courses </a>
				<a href="/tutorial" class="block mt-4 text-gray-200 hover:text-white mr-4">
					Tutorial
				</a>
			</div>
			<div class="flex flex-col ml-auto">
				<a
					href="/login"
					class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-gray-800 hover:bg-white mt-4"
				>
					{#if loggedIn}
						Account
					{:else}
						Login
					{/if}
				</a>
			</div>
		</div>
	{/if}

	<div class="w-full hidden md:flex flex-grow md:items-center md:w-auto">
		<div class="text-sm md:flex-grow">
			<a
				href="/courses"
				class="block mt-4 md:inline-block md:mt-0 text-gray-200 hover:text-white mr-4"
			>
				Courses
			</a>
			<a
				href="/tutorial"
				class="block mt-4 md:inline-block md:mt-0 text-gray-200 hover:text-white mr-4"
			>
				Tutorial
			</a>
		</div>
		<div class="space-x-5">
			<a
				href="/login"
				class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-gray-800 hover:bg-white mt-4 md:mt-0"
			>
				{#if loggedIn}
					Account
				{:else}
					Login
				{/if}
			</a>
		</div>
	</div>
</nav>
