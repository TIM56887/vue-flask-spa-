<template>
    <div class="card" >
        <img :src=' content.img ' class="card-img-top image" alt="...">
        <div class="card-body ">
            <h5 class="card-title fs-4 fw-semibold">{{content.title}}</h5>
            <p class="card-text">{{ content.review }}</p>
        </div>
        <div class="link">
            <a :href=" content.url " class="hover-button" target="_blank" >
                <i class="bi bi-box-arrow-up-right"></i>
                Go Try !
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name:'InfoBox',
    props:['content']
}
</script>
    
<style scoped>

    

    @media (min-width: 768px) {
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
            border-radius: 4px;
            /* width:auto; */
            text-align: center;
            border: 1px solid rgb(199, 199, 199);
            height: 50px;
            width: 150px;
            line-height: 50px;
            
            
        }
        .card:hover .link {
            opacity: 1;
        }
        .hover-button {
            height: 50px;
            font-size: 1.5rem;
            text-decoration: none;
            color: black;
            font-weight: 300 !important;
        }
        .link:hover {
            --tw-gradient-from: #60a5fa;
            --tw-gradient-to: #3e6ff8;
            --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
            
        }
        .link:hover a {
            color: white;
        }
    }

    @media (max-width: 768px) {
        .card {
            display: flex;
            flex-direction: row;
            margin: 0 !important;
            border-radius: 0px;
            height: 120px !important;
            box-shadow: 0px 5px 0px 0px rgba(196, 196, 196, 0.75);
            position: relative;
        }
        .image {
            height: 100%;
            max-width: 100px;
            object-fit: contain;
            padding: 15px;
            border-right: 1px solid rgb(218, 218, 218);
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
            border-radius: 4px;
            width:10rem;
            text-align: center;
            border: 1px solid rgb(199, 199, 199);
        }
        .card:hover .link {
            opacity: 1;
        }
        .hover-button {
            height: 50px;
            font-size: 1.5rem;
            text-decoration: none;
            color: black;
            font-weight: 300 !important;
        }
        .link:hover {
            --tw-gradient-from: #60a5fa;
            --tw-gradient-to: #3e6ff8;
            --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
            
        }
        .link:hover a {
            color: white;
        }
    }

    
</style>