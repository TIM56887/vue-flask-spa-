<template>
    <section class="portfolio" id="section1">
        <div class="vertical-dashed-line"></div>
        <div class="dashed-line-with-circle"></div>
        <div class="dashed-line-with-circle-end"></div>
        <div class="container-fluid">            
            <div class="row main-contnet justify-content-center position-relative">                                
                <div class=" col-10 col-md-5 col-xxl-4 preview">                    
                    <div class="">
                        <img class="icon" src="../../assets/rioticon.png" alt="lolPic">
                    </div>
                    <div class="title fs-1 fw-bolder mt-1 mt-md-3">LOL player search</div>
                    <div class="fs-3 tag fw-bolder mt-1 mt-md-3">Work with APIs</div>
                    <div class="fw-bolder mt-2 main-text"><p>LOL玩家查詢系統，利用RIOT官方api製作玩家資訊查訊系統，包含常用英雄、對戰紀錄...等</p></div>
                    <div class="linkArea">
                        <a class="link">
                            <!-- <i class="bi bi-box-arrow-up-right"></i> -->
                            <i class="bi bi-cone-striped"></i>
                            <div class="linkTxt"> 開發中...</div>
                        </a>
                    </div>
                </div>
                <div class="col-10 col-md-5 col-xxl-4 imgArea">
                    <div class="image">
                        <img src="../../assets/lolwallpaper1.png" alt="lol" class="lol-wallpaper">
                    </div>
                </div>
            </div>
            <div class="row justify-content-center main-contnet2 align-items-center">
                <div class="col-10 col-md-5 col-xxl-4 imgArea2">
                    <div class="image">
                        <img src="../../assets/map.png" alt="lol" class="mapImg">
                    </div>
                </div>
                <div class="col-10 col-md-5 col-xxl-4 preview2">
                    <div class="">
                        <img class="icon-leaf" src="../../assets/leaficon.png" alt="lolPic">
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
            <div class="row justify-content-center main-content3">
                <div class=" col-10 col-md-5 col-xxl-4 preview3">                    
                    <div class="">
                        <img class="icon" src="../../assets/ntp.png" alt="lolPic">
                    </div>
                    <div class="title fs-1 fw-bolder mt-1 mt-md-3">新北市房價預測系統</div>
                    <div class="fs-3 tag fw-bolder mt-1 mt-md-3">data processing</div>
                    <div class="fw-bolder mt-1 main-text">
                        <p>使用新北市政府提供之房價實價登錄資料。
                        利用python Pandas進行資料清理，經過系列的前處理步驟，處理缺失值、轉換類別資料特徵等，使得原始資料達到了可以進行模型訓練的狀態。使用scikit-learn線性回歸模型進行訓練。
                        訓練及測試資料共29,764筆，特徵共13種(區域、土地坪數、樓層、最高樓層、建物型態、屋齡、建物總面積、房廳衛數、有無管理組織及電梯)
                        
                        </p>
                    </div>
                    <div class="linkArea">
                        <a href="/predict" class="link">
                            <i class="bi bi-box-arrow-up-right"></i>
                            <div class="linkTxt">Go Try !</div>
                        </a>
                    </div>
                </div>
                <div class="col-10 col-md-5 col-xxl-4 imgArea3">
                    <div class="image">
                        <img src="../../assets/houseprice.png" alt="lol" class="housePricePC">
                    </div>
                </div>
            </div>
            <div class="row flex-md-row-reverse flex-column-reverse main-contnet2 justify-content-center align-items-center">                                
                <div class=" col-10 col-md-5 col-xxl-4 preview4">                    
                    <div>
                        <img class="icon" src="../../assets/JavaScript.png" alt="lolPic">
                    </div>
                    <div class="title fs-1 fw-bolder mt-1 mt-md-3">JavaScript Quiz</div>
                    <div class="fs-3 tag fw-bolder mt-1 mt-md-3">Work with data</div>
                    <div class="fw-bolder mt-2 main-text"><p>有關JavaScript的選擇題測驗</p></div>
                    <div class="linkArea">
                        <a class="link" href="/jsquiz">
                            <i class="bi bi-box-arrow-up-right"></i>
                            <div class="linkTxt"> GO Try</div>
                        </a>
                    </div>
                </div>
                <div class="col-10 col-md-5 col-xxl-4 imgArea2">
                    <div class="image">
                        <img src="../../assets/jsquizapp.png" alt="lol" class="lol-wallpaper">
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
        min-height: 70vh;
    }
    .main-contnet::after{
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 50%; /* 根据需要调整位置 */
        top: 100%; /* 圆圈的垂直位置 */
        transform: translate(-50%, -50%);
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
        z-index: 100;
    }
    
    .vertical-dashed-line:after {
        content: '';
        position: absolute;
        left: 50%; /* 将线条放在中间 */
        top: 0;
        bottom: 0;
        border-left: 1px dashed rgb(172, 172, 172); /* 添加虚线 */
        
    }
    .vertical-dashed-line:before {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 49.7%; /* 根据需要调整位置 */
        top: 78%; /* 圆圈的垂直位置 */
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
        z-index: 1000;
    }
    .dashed-line-with-circle:after {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 49.75%; /* 根据需要调整位置 */
        top: 0px; /* 圆圈的垂直位置 */
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
        top: 55%; /* 圆圈的垂直位置 */
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
        /* margin-top: 100px;
        margin-bottom: 14%; */
    }
    .preview3 {
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: white 2%,var(--tw-gradient-from) 15%, var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        position: relative;
        padding-left: 100px;
        padding-right: 50px;
        margin-top: 200px;
    }
    .preview4 {
        --tw-gradient-from: #b56f07;
        --tw-gradient-to: #b54707;
        --tw-gradient-stops: white 2%,var(--tw-gradient-from) 15%, var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        padding-left: 70px;
        /* margin-top: 7%;
        margin-bottom: 14%; */
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
        object-position: top left;
    }
    .housePricePC{
        height: 440px;
        width: 100%;
        object-fit: cover;
        object-position: top left; 
    }
    .mapImg {
         
        width: 100%;
    }
    .imgArea {
        padding: 0;
    }
    .imgArea3 {
        padding: 0;
        margin-top: 320px   ;
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
        margin-top: 100px;
        min-height: 800px
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
    .main-contnet2 {
        margin-top: 150px;
    }
    .main-content3 {
        align-items: center;
        flex-direction: column-reverse;
    }
    .main-contnet::after{
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 5%; /* 根据需要调整位置 */
        top: 110%; /* 圆圈的垂直位置 */
        transform: translate(-50%, -50%);
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
        z-index: 100;
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
        top: 0px; /* 圆圈的垂直位置 */
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
        z-index: 0;
    }
    .vertical-dashed-line:before {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 4%; /* 根据需要调整位置 */
        top: 73%; /* 圆圈的垂直位置 */
        width: 10px; /* 圆圈的宽度 */
        height: 10px; /* 圆圈的高度 */
        background-color: white; /* 圆圈的颜色 */
        border-radius: 50%; /* 圆形 */
        border: 1px solid rgba(30,30,30,.3);
        z-index: 1000;
    }
    .dashed-line-with-circle:before {
        content: ''; /* 伪元素内容为空 */
        position: absolute; /* 绝对定位 */
        left: 4%; /* 根据需要调整位置 */
        top: 51%; /* 圆圈的垂直位置 */
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
    .preview3{
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: white 2%,var(--tw-gradient-from) 15%, var(--tw-gradient-to);
        background-image: linear-gradient(to right bottom, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        position: relative;
        margin-bottom: 50px;
    }
    .preview4 {
        --tw-gradient-from: #b56f07;
        --tw-gradient-to: #b54707;
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
    .housePricePC{
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
    .imgArea3 {
        display: none;
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

}


</style>