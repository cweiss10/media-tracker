<script>
  import { onMount } from 'svelte';
  import { Chart } from 'chart.js';

  let chart;
  
  onMount(() => {
    const ctx = document.getElementById('myChart').getContext('2d');
    chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['January', 'February', 'March'],
        datasets: [{
          label: 'Media Completed',
          data: [5, 8, 12],
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      }
    });
  });
</script>

<canvas id="myChart"></canvas>
