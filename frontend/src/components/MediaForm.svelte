<script>
  import axios from 'axios';

  let title = "";
  let mediaType = "book";
  let status = "started";

  const addMedia = async () => {
    try {
      await axios.post("http://localhost:8000/media/", {
        title,
        media_type: mediaType,
        status,
      });

      title = "";
      mediaType = "book";
      status = "started";

      alert("Media added successfully!");
    } catch (error) {
      console.error("Error adding media", error);
      alert("Failed to add media.");
    }
  };
</script>

<!-- MediaForm.svelte -->
<form
  class="flex items-center space-x-8 p-6 bg-gray-800 rounded-lg shadow-lg"
  on:submit|preventDefault={addMedia}
>
  <!-- Title Field -->
  <div class="flex flex-col">
    <label for="title" class="text-sm font-semibold text-gray-300">Title</label>
    <input
      type="text"
      id="title"
      bind:value={title}
      class="p-3 w-72 bg-gray-900 text-gray-300 border border-gray-600 rounded-md placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-primary"
      placeholder="Media Title"
      required
    />
  </div>

  <!-- Media Type Field -->
  <div class="flex flex-col">
    <label for="mediaType" class="text-sm font-semibold text-gray-300">Media Type</label>
    <select
      id="mediaType"
      bind:value={mediaType}
      class="p-3 w-56 bg-gray-900 text-gray-300 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
    >
      <option value="book">Book</option>
      <option value="movie">Movie</option>
      <option value="music">Music</option>
      <option value="podcast">Podcast</option>
      <option value="tv_show">TV Show</option>
    </select>
  </div>

  <!-- Status Field -->
  <div class="flex flex-col">
    <label for="status" class="text-sm font-semibold text-gray-300">Status</label>
    <select
      id="status"
      bind:value={status}
      class="p-3 w-56 bg-gray-900 text-gray-300 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
    >
      <option value="started">Started</option>
      <option value="inProgress">In Progress</option>
      <option value="finished">Finished</option>
      <option value="didNotFinish">Did Not Finish</option>
    </select>
  </div>

  <!-- Submit Button -->
  <button
    type="submit"
    class="p-3 w-32 bg-primary text-gray-900 rounded-md hover:bg-secondary focus:outline-none focus:ring-2 focus:ring-primary"
  >
    Add
  </button>
</form>



