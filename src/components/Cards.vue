<script setup>
const props = defineProps(['movie'])
</script>

<template>
    <div class="col col-md-4">
        <div class="card">
            <img :src="article.photo" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">{{ article.title }}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary">{{ article.created_on }}</h6>
                <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
                <RouterLink :to="'/articles/' + article.id" class="card-link">Read more</RouterLink>
            </div>
        </div>
    </div>
</template>