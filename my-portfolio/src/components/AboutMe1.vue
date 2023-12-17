<template>
    <section class="aboutMe py-5" id="section3">
        <h1><div class="fs-2 fs-md-1 fw-bold text-center mt-5">About Me</div></h1>
        <div class="container-fluid">
            <div class="row justify-content-center mt-3 mt-md-5">
                <div class="content col-10 col-md-4 text-md-end text-center">
                    <p class="fs-4 fs-md-3">網頁設計| 前後端開發| 網路爬蟲</p>
                    <pre class="fs-4 fs-md-3">Python |AWS EC2 |js |VUE</pre>
                    <p class="fs-5 fs-md-3">E-mail：timmy56887@icloud.com</p>
                </div>
                <div class="Picborder col-10 col-md-2 ms-md-3 mt-3 mt-md-0">
                    <div class="picBox">
                        <img class="linePIC" src="../assets/lineimg.jpeg" alt="lineQRcode">
                        <div class="middle">
                            <div class="text">ID:timmy56887</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
</script>

<style scoped>
    .picBox {
        position: relative;
        width: 100%;
        height: 100%;
    }
    .picBox:hover .linePIC {
        opacity: 0.3;
    }
    .picBox:hover .middle {
        opacity: 1;
    }
    .linePIC{
        opacity: 1;
        display: block;
        height: 80%;
        width: auto;
        transition: .5s ease;
        position: absolute;
        top: 50%; 
        left: 50%;
        transform: translate(-50%, -50%);
        display: block;
        backface-visibility: hidden;
    }
    .Picborder {
        text-align: start;
    }
    .middle {
        transition: .5s ease;
        opacity: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: auto;
    }

    .text {
        background-color: #4CAF50;
        color: white;
        font-size: 0.8rem;
        padding: 16px 32px;
    }


    .content{
        margin-top: 2rem;
        color:#1e1e1e;
    }

    @media (max-width: 768px) {
        .picBox {
            height: 150px;
        }
        .linePIC{
            height: 100%;
        }
    }

</style>