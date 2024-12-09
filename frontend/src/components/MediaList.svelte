<script>
  import axios from 'axios';

  let mediaItems = [];
  let searchTerm = '';
  let mediaTypeFilter = "all";
  let statusFilter = "all";

  const fetchMedia = async () => {
    try {
      const response = await axios.get("http://localhost:8000/media/");
      mediaItems = response.data;
    } catch (error) {
      console.error("Error fetching media", error);
      alert("Failed to fetch media.");
    }
  };

  let filteredMediaItems = [];

  $: {
    filteredMediaItems = mediaItems.filter(item => {
      const matchesSearchTerm = item.title.toLowerCase().includes(searchTerm.toLowerCase());
      const matchesMediaType = mediaTypeFilter === "all" || item.media_type === mediaTypeFilter;
      const matchesStatus = statusFilter === "all" || item.status === statusFilter;

      return matchesSearchTerm && matchesMediaType && matchesStatus;
    });
  }

  fetchMedia();
</script>

<!-- MediaList.svelte -->
<div class="p-6 bg-gray-900">
  <div class="max-w-full mx-auto bg-gray-800 p-6 rounded-lg shadow-lg">
    <!-- Search and Filters Section -->
    <h2 class="text-2xl font-semibold text-center mb-4 text-gray-300">Media List</h2>

    <!-- Search Bar -->
    <div class="mb-4">
      <input
        type="text"
        placeholder="Search by title"
        bind:value={searchTerm}
        aria-label="Search media by title"
        class="w-full p-3 bg-gray-900 text-gray-300 border border-gray-600 rounded-md placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-primary"
      />
    </div>

    <!-- Filters Section -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
      <div>
        <label for="mediaTypeFilter" class="block text-lg font-semibold mb-2 text-gray-300">Media Type</label>
        <select
          id="mediaTypeFilter"
          bind:value={mediaTypeFilter}
          class="w-full p-3 bg-gray-900 text-gray-300 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
        >
          <option value="all">All</option>
          <option value="book">Book</option>
          <option value="movie">Movie</option>
          <option value="music">Music</option>
          <option value="podcast">Podcast</option>
          <option value="tv_show">TV Show</option>
        </select>
      </div>

      <div>
        <label for="statusFilter" class="block text-lg font-semibold mb-2 text-gray-300">Status</label>
        <select
          id="statusFilter"
          bind:value={statusFilter}
          class="w-full p-3 bg-gray-900 text-gray-300 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
        >
          <option value="all">All</option>
          <option value="started">Started</option>
          <option value="inProgress">In Progress</option>
          <option value="finished">Finished</option>
          <option value="didNotFinish">Did Not Finish</option>
        </select>
      </div>
    </div>

    <!-- Media Table -->
    <table class="min-w-full table-auto bg-gray-900 rounded-lg shadow-md">
      <thead class="bg-gray-800 text-gray-300">
        <tr>
          <th class="p-4 text-left font-semibold">Title</th>
          <th class="p-4 text-left font-semibold">Media Type</th>
          <th class="p-4 text-left font-semibold">Status</th>
        </tr>
      </thead>
      <tbody>
        {#each filteredMediaItems as item}
        <tr class="border-t border-gray-700 hover:bg-gray-700">
          <td class="p-4 text-gray-300">{item.title}</td>
          <td class="p-4 text-gray-300 capitalize">{item.media_type.replace("_", " ")}</td>
          <td class="p-4 text-gray-300 capitalize">{item.status.replace("_", " ")}</td>
        </tr>
        {:else}
        <tr>
          <td colspan="3" class="p-4 text-center text-gray-500">No media found.</td>
        </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>


