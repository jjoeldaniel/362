<!-- src/Course.svelte -->
<script lang="ts">
    export let course: {
      id:number;
      "course code": string;
      title: string;
      description: string;
      prerequisites: string[];
      credits: number;
    };
    let completed = false;
  
    function toggleCompletion() {
      completed = !completed;
    }
  </script>
  
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
  
  <div class="course {completed ? 'completed' : ''}">
    <h3>{course["course code"]}</h3>
    <p><strong>Title:</strong> {course.title}</p>
    <p><strong>Description:</strong> {course.description}</p>
    <p><strong>Prerequisites:</strong> {course.prerequisites.join(", ")}</p>
    <p><strong>Credits:</strong> {course.credits}</p>
    <button on:click={toggleCompletion}>
      {completed ? 'Mark Incomplete' : 'Mark Completed'}
    </button>
  </div>
  