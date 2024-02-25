<template>
    <section class="main pt-5">
        <div class="container-sm p-5">
            <div class="row justify-content-center">
                <div class="col-4 text  bold m-auto">
                    <p class="fw-bolder fs-2">新北市房價預測系統(111年)</p>
                    <a href="https://data.gov.tw/dataset/161655" class="text-decoration-none icon-link"><p class="fw-medium fs-6 m-0 text-secondary-emphasis">資料來源:歷年不動產實價登錄資訊-買賣案件-111年</p></a>
                    <a href="https://github.com/TIM56887/-scikit-learn/blob/main/trainAndTest.ipynb" class="text-decoration-none"><p class="fs-6 text-secondary-emphasis">訓練及測試資料</p></a>
                    <button @click="startPredict" class="btn btn-secondary btn-sm">Go Try</button>
                </div>
                <div class="col-7 photo-box mt-5 ps-3">
                    <!-- <img class="preview-photo border border-light-subtle rounded-3" src="@/assets/HousePrice/preview1.png" alt="介紹一"> -->
                    <!-- Swiper -->
                    <div class="swiper-container">
                        <div class="swiper-wrapper">
                            <div class="swiper-slide"><a href="https://data.gov.tw/dataset/161655" class="text-decoration-none icon-link"><img class="preview-photo border border-light-subtle rounded-3" src="@/assets/HousePrice/preview1.png" alt="介紹一"></a></div>
                            <div class="swiper-slide"><a href="https://github.com/TIM56887/-scikit-learn/blob/main/trainAndTest.ipynb" class="text-decoration-none"><img class="preview-photo2 border border-light-subtle rounded-3" src="@/assets/HousePrice/preview2.png" alt="介紹二"></a></div>
                            <!-- <div class="swiper-slide"><img class="preview-photo border border-light-subtle rounded-3" src="@/assets/HousePrice/preview1.png" alt="介紹一"></div> -->
                        </div>
                        <!-- 如果需要分页器 -->
                        <!-- <div class="swiper-pagination"></div> -->
                        
                        <!-- 如果需要导航按钮 -->
                        <!-- <div class="swiper-button-prev"></div>
                        <div class="swiper-button-next"></div> -->
                    
                        <!-- 如果需要滚动条 -->
                        <!-- <div class="swiper-scrollbar"></div> -->
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    
</template>
<script>
// 引入Swiper JS
import Swiper from 'swiper';
// 引入Swiper CSS
import 'swiper/swiper-bundle.css';
export default {
    mounted(){
        this.initSwiper();
    },
    methods:{
        initSwiper(){
            new Swiper('.swiper-container', {
            // Swiper选项
            loop: true,
            autoplay: {
            delay: 2500,
            disableOnInteraction: false,
            },
            // 其他配置...
        });
        },
        startPredict(){
            this.$emit('changePage')
        }
    },
    data(){
        return{
           
        }
    }
}
</script>
<style scoped>
    .photo-box {
        height: 600px;
        overflow: hidden;
    }
    .preview-photo{
        width: 100%;
        height: 600px;
        object-fit: cover;
        object-position: 30% 10%;
    }
    .main{
        background-image: url('@/assets/HousePrice/graybackground.jpg');
        background-repeat: no-repeat;
        background-size: cover;
        height: 100vh;
    }
    .preview-photo2{
        width: 100%;
        height: 700px;
        object-fit: cover;
        object-position: 30% 10%;
    }
</style>