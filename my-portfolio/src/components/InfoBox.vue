<template>
    <div class="card">
        <img :src=' content.img ' class="card-img-top image" alt="...">
        <div class="card-body">
            <h5 class="card-title fs-4 fw-semibold">{{content.title}}</h5>
            <p class="card-text">{{ content.review }}</p>
        </div>
        <div class="link">
            <a :href=" content.url " class="hover-button" target="_blank" >Go Look!</a>
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
        margin: 30px 0 0 30px;
        width:270px;
        height: 380px !important;
        box-shadow: 5px 5px 5px 0px rgba(228, 226, 226, 0.75);
        position: relative;
    }
    .image {
        height: 45%;
        width: auto;
        object-fit: contain;
    }
    h5{
        height: 10%;
    }
    .card-text {
        height: 60%;
        margin-top: 1rem;
    }
    .card:hover .image ,.card:hover .card-body{
        transition: 0.5s;
        opacity: 0.1;
    }

    .link {
        opacity: 0;
        transition: opacity 0.5s;
        position: absolute;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: 1px solid black;
        border-radius: 10px;
        width:10rem;
        text-align: center;
    }
    .card:hover .link {
        opacity: 1;
    }
    .hover-button {
        font-size: 1.6rem;
        text-decoration: none;
        color: black;
    }
    .link:hover {
        /* background-color: rgba(0, 170, 255, 0.7); */
        --tw-gradient-from: #edf2f8;
        --tw-gradient-to: #4cb7fe;
        --tw-gradient-stops: white 5%,var(--tw-gradient-from) 30%, var(--tw-gradient-to);
        background-image: linear-gradient(to top right, var(--tw-gradient-stops));
    }
    

    @media (min-width: 768px) {
        
    }

    @media (max-width: 768px) {
        .card {
            margin-bottom: 20px;
     
        }
    }

    
</style>