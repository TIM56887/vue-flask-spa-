<template>
    <section class="portfolio" id="section1">
        <div class="vertical-dashed-line"></div>
        <div class="dashed-line-with-circle"></div>
        <div class="dashed-line-with-circle-end"></div>
        <div><h1 class="text-center"></h1></div>
        <div class="container-fluid">            
            <div class="row main-contnet justify-content-center">                                
                <div class=" col-10 col-md-5 col-xxl-4 preview">                    
                    <div class="">
                        <img class="icon" src="../assets/rioticon.png" alt="lolPic">
                    </div>
                    <div class="title fs-1 fw-bolder mt-1 mt-md-3">LOL player search</div>
                    <div class="fs-3 tag fw-bolder mt-1 mt-md-3">Work with APIs</div>
                    <div class="fw-bolder mt-2 main-text"><p>LOL玩家查詢系統，利用RIOT官方api製作玩家資訊查訊系統，包含常用英雄、對戰紀錄...等</p></div>
                    <div class="linkArea">
                        <a href="" class="link">
                            <i class="bi bi-box-arrow-up-right"></i>
                            <div class="linkTxt">Go Try !</div>
                        </a>
                    </div>
                </div>
                <div class="col-10 col-md-5 col-xxl-4 imgArea">
                    <div class="image">
                        <img src="../assets/lolwallpaper1.png" alt="lol" class="lol-wallpaper">
                    </div>
                </div>
            </div>
            <div class="row justify-content-center main-contnet2">
                <div class="col-10 col-md-5 col-xxl-4 imgArea2">
                    <div class="image">
                        <img src="../assets/map.png" alt="lol" class="mapImg">
                    </div>
                </div>
                <div class="col-10 col-md-5 col-xxl-4 preview2">
                    <div class="">
                        <img class="icon-leaf" src="../assets/leaficon.png" alt="lolPic">
                    </div>
                    <div class="title fs-1 fw-bolder mt-1 mt-md-3">LIFF Map</div>
                    <div class="fs-3 tag fw-bolder mt-1 mt-md-3">Work with Map</div>
                    <div class="fw-bolder mt-2 main-text"><p>利用leaflet和line前端框架LIFF製作地圖</p></div>
                    <div class="linkArea">
                        <a href="https://github.com/TIM56887/liff_map" target="_blank" class="link">
                            <i class="bi bi-box-arrow-up-right"></i>
                            <div class="linkTxt">Go Try !</div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
</script>

<style scoped>
@media (min-width: 768px) {
    .portfolio {
       position: relative;
    }

    .main-contnet {
        padding-top: 200px;
        height: 70vh;
    }
    .vertical-dashed-line:after {
        content: '';
        position: absolute;
        left: 50%; /* 将线条放在中间 */
        top: 0;
        bottom: 0;
        border-left: 1px dashed rgb(172, 172, 172); /* 添加虚线 */
        
    }
    .dashed-line-with-circle:after {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 49.75%; /* 根据需要调整位置 */
        top: -10px; /* 圆圈的垂直位置 */
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
    }
    .dashed-line-with-circle:before {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 49.75%; /* 根据需要调整位置 */
        top: 35%; /* 圆圈的垂直位置 */
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
    }
    .dashed-line-with-circle-end:after{
        content: "\30FB";
        line-height: 0.7;
        text-indent: -6px;
        display: inline-block;
        color: #b2b2b2;
        box-sizing: border-box;
        border: 1px solid #b2b2b2;
        width: 20px;
        height: 20px;
        position: absolute;
        left: 49.5%;
        bottom: -10px;
        background-color: #fff;
        border-radius: 50%;
        font-size: 30px;
    }
    
    .preview {
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: white 2%,var(--tw-gradient-from) 15%, var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        position: relative;
        padding-left: 100px;
        padding-right: 50px;
    }

    .preview2 {
        --tw-gradient-from: #07b581;
        --tw-gradient-to: #07b53b;
        --tw-gradient-stops: white 2%,var(--tw-gradient-from) 15%, var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        padding-left: 70px;
        margin-top: 200px;
        margin-bottom: 25%;
    }
    .tag {
        color: transparent;
    }
    .icon {
        width: 80px;
        height: auto;
        border: 1px solid rgb(216, 216, 216);
        border-radius: 10px;
        padding: 10px;
        /* box-shadow: 5px 5px 5px 0px rgba(228, 226, 226, 0.75); */
    }
    .icon-leaf {
        width: 80px;
        height: auto;
        border: 1px solid rgb(216, 216, 216);
        border-radius: 10px;
        padding: 10px;
    }

    .lol-wallpaper {
        height: 500px;
        width: 100%;
        object-fit: cover;
        /* object-position: center; */
    }

    .mapImg {
         
        width: 100%;
    }
    .imgArea {
        padding: 0;
    }
    .imgArea2 {
        padding-left: 100px;
        padding-right: 0;
        text-align: right;
    }
    .link {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 150px;
        height: 50px;
        color: black;
        margin-top: 50px;
        font-size: 20px;
        text-decoration: none;
        border: 1px solid rgb(199, 199, 199);
        border-radius: 4px;
    }

    .link:hover {
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #3e6ff8;
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        color: white;
    }
    .linkTxt {
        margin-left: 10px;
    }

    .main-text {
        color: #777;
        line-height: 1.8;
    }
    .main-contnet2 {
        margin-top: 200px;
    }
}

@media (max-width: 768px) {
    .portfolio {
       position: relative;
    }

    .main-contnet {
        align-items: center;
        flex-direction: column-reverse;
        
    }
    .vertical-dashed-line:after {
        content: '';
        position: absolute;
        left: 5%; /* 将线条放在中间 */
        top: 0;
        bottom: 0;
        border-left: 1px dashed rgb(172, 172, 172); /* 添加虚线 */
        z-index: -10;
    }
    .dashed-line-with-circle:after {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 4%; /* 根据需要调整位置 */
        top: -10px; /* 圆圈的垂直位置 */
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
        z-index: 0;
    }
    .dashed-line-with-circle:before {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 4%; /* 根据需要调整位置 */
        top: 40%; /* 圆圈的垂直位置 */
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
    }
    .dashed-line-with-circle-end:after{
        content: "\30FB";
        line-height: 0.7;
        text-indent: -6px;
        display: inline-block;
        color: #b2b2b2;
        box-sizing: border-box;
        border: 1px solid #b2b2b2;
        width: 20px;
        height: 20px;
        position: absolute;
        left: 3%;
        bottom: -10px;
        background-color: #fff;
        border-radius: 50%;
        font-size: 30px;
    }
    
    .preview {
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: white 2%,var(--tw-gradient-from) 15%, var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        position: relative;
        /* padding-left: 10px; */
        
    }

    .preview2 {
        --tw-gradient-from: #07b581;
        --tw-gradient-to: #07b53b;
        --tw-gradient-stops: white 2%,var(--tw-gradient-from) 15%, var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        margin-top: 15px;
        margin-bottom: 25%;
    }
    .tag {
        color: transparent;
    }
    .icon {
        width: 60px;
        height: auto;
        border: 1px solid rgb(216, 216, 216);
        border-radius: 10px;
        padding: 10px;
        /* box-shadow: 5px 5px 5px 0px rgba(228, 226, 226, 0.75); */
    }
    .icon-leaf {
        width: 60px;
        height: auto;
        border: 1px solid rgb(216, 216, 216);
        border-radius: 10px;
        padding: 10px;
    }

    .lol-wallpaper {
        border-radius: 40px;
        width: 100%;
        height: 280px;
        object-fit: cover;
        object-position: top left;
    }

    .mapImg { 
        width: 100%;
        height: 400px;
        object-fit: cover;
        object-position: top left;
        border-radius: 20px;
    }
    .imgArea {
        margin-top: 40px;
        margin-bottom: 10px;
    }
    .imgArea2 {
        /* padding-left: 100px; */
        padding-right: 0;
        text-align: right;
    }
    .link {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 150px;
        height: 50px;
        color: black;
        margin-top: 10px;
        font-size: 20px;
        text-decoration: none;
        border: 1px solid rgb(199, 199, 199);
        border-radius: 4px;
    }

    .link:hover {
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #3e6ff8;
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        color: white;
    }
    .linkTxt {
        margin-left: 10px;
    }

    .main-text {
        color: #777;
        line-height: 1.8;
    }
    .main-contnet2 {
        margin-top: 150px;
    }
}


</style>