<template>

    <form @submit.prevent="saveMovie" id="MovieForm">
        <div class="form-group mb-3">
            <h2 class="display-1 mb-3">Add a Movie</h2>
            <div class="sect">
                <label for="title" class="form-label">Movie Title</label>
                <input type="text" name="title" class="formcontrol" />
            </div>
            <div class="sect">
                <label for="description" class="form-label">Movie Description</label>
                <input type="text" name="description" class="formcontrol" />
            </div>
            <div class="sect">
                <label for="poster" class="form-label">Movie Poster</label>
                <input type="file" name="poster" class="formcontrol" />
            </div>
            <input type="hidden" name="csrf_token" :value="csrf_token" />
            <button class="btn btn-primary" type="submit">Add</button>
        </div>
    </form>

</template>

<script setup>
  import { ref, onMounted } from "vue";
  let csrf_token = ref("");  
  let saveMovie = () => {
    const form = document.getElementById('MovieForm');
    let formData = new FormData(form);
   // formData.append('csrf_token', '{{ csrf_token() }}');

    fetch("/api/v1/movies", { method: 'POST', body: formData, headers: {'X-CSRFToken': csrf_token.value } })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        console.log('successful connection');
      })
      .catch((error) => {
        console.log(error);
      });
  };
    onMounted(() => {
        getCsrfToken();
    });

    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
        })
    }
    
</script>