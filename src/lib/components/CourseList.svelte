<!-- CourseList.svelte -->
<script lang='ts'>
    import { onMount } from "svelte";
    import Course from "./Course.svelte";

    export let division: string;
    export let jsonFilePath: string; // Add a prop for the JSON file path
    
    let showDetails = false;

    function toggleDetails(){
        showDetails = !showDetails
    }

    let courses: Array<{
        key:number;
        id: number;
        "course code": string;
        title: string;
        description: string;
        prerequisites: string[];
        credits: number;
    }> = [];
  
    onMount(async () => {
        if (!jsonFilePath) {
            console.error("Please provide a valid JSON file path.");
            return;
        }

        try {
            const response = await fetch(jsonFilePath);

            if (!response.ok) {
            throw new Error(`Failed to fetch data (status ${response.status}).`);
            }

            courses = await response.json();
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    });
  </script>
  
  <style>
    /* Styling for the button */
    button {
        background-color: #007bff;
        color: white;
        padding: 10px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #0056b3;
    }

    /* Styling for the container */
    div {
        margin: 20px;
    }

    /* Add focus styling for better accessibility */
    button:focus {
        outline: 2px solid #0056b3;
    }
  </style>
  
  <div>
    <button on:click={toggleDetails} >
        {division}
    </button>
    {#if showDetails}
        {#each Object.entries(courses) as [key, course]}
            <Course {course} />
        {/each}
    {/if}
  </div>
  
  