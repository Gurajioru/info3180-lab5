<template>
    <main>
      <h2>Movies</h2>
      <div class="movie-list">
        <div class="movie" v-for="movie in movies" :key="movie.title">
          <img :src="'/api/v1/posters/' + movie.poster" alt="Movie Poster" />
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </main>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  let movies = ref([]);
  
  function fetchMovies() {
    fetch('/api/v1/movies', { method: 'GET' })
      .then((response) => response.json())
      .then((data) => {
        movies.value = data.movies;
      })
      .catch((err) => {
        console.log(err);
      });
  }
  
  onMounted(() => {
    fetchMovies();
  });
  </script>
  
  <style scoped>
    .movie-list {
      margin-left:20px;  
      display: grid;
      grid-template-columns: repeat(auto-fill, 600px);
      grid-gap:15px;
    
    }
  
    .movie {
      /*width: 30%;
      margin-bottom: 30px;*/
      border: 1px solid rgb(221, 217, 217)
    }
  
    .movie img {
      width: 170px;
      height: 256px;
      object-fit:cover;
      float:left;
      padding-right:15px;

    }
  
    .movie h3 {
      margin: 10px 0;
    }
  
    .movie p {
      margin: 0;
      width:50%;
      overflow:hidden;
    }

    h2{
        margin-left:20px;
    }
  </style>