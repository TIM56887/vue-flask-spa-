<template>
    <section class="aboutMe" id="section3">
        <h1><div class="fs-1 fw-bold text-center mt-5">About Me</div></h1>
        <div class="container-fluid">
            <div class="row justify-content-center mt-5">
                <div class="content col-5 col-xxl-4 text-end">
                    <p class="fs-3">網頁設計| 前後端開發| 網路爬蟲</p>
                    <pre class="fs-3">Python  |C#  |Java  |VUE</pre>
                    <p class="fs-3 ">E-mail：timmy56887@icloud.com</p>
                </div>
                <div class="Picborder col-5 col-xxl-2">
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
    .aboutMe {
        /* min-height: 50vh;     */
    }
    /* .mainArea {
        display: flex;
        justify-content: center;
    } */
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
        /* height: auto; */
        transition: .5s ease;
        position: absolute;
        top: 50%; 
        left: 50%;
        transform: translate(-70%, -50%);
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
        transform: translate(-70%, -50%);
        /* -ms-transform: translate(-50%, -50%); */
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

</style>