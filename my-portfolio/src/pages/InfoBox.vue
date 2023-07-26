<template>
    <div class="card" style="width: 18rem;">
        <img :src=' content.img ' class="card-img-top image" alt="...">
        <div class="card-body">
            <h5 class="card-title fs-4 fw-semibold">{{content.title}}</h5>
            <p class="card-text">{{ content.review }}</p>
            <a :href=" content.url " class="btn btn-primary">前往</a>
        </div>
    </div>
</template>

<script>
export default {
    name:'InfoBox',
    props:['content']
}
</script>
    
<style>
    .card {
        margin-left: 15px;
    }
    .image {
        height: 45%;
    }
    h5{
        height: 10%;
    }
    .card-text {
        height: 60%;
    }
</style>