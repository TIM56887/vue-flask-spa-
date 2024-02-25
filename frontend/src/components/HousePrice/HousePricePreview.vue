<template>
    <section class="main pt-5">
        <div class="container-sm p-5">
            <div class="row justify-content-center">
                <div class="col-4 text  bold m-auto">
                    <p class="fw-bold fs-2">新北市房價預測系統</p>
                    <a href="https://data.gov.tw/dataset/161655"><p class="fw-medium fs-5">資料來源:政府公開資訊網站</p></a>
                </div>
                <div class="col-7 photo-box">
                    <img class="preview-photo border border-light-subtle rounded-3" src="@/assets/HousePrice/preview1.png" alt="介紹一">
                </div>
            </div>
        </div>
    </section>
    
    
</template>
<script>
export default {
    methods:{
    },
    data(){
        return{
           
        }
    }
}
</script>
<style scoped>
    .photo-box {
        height: 700px;
        overflow: hidden;
    }
    .preview-photo{
        width: 100%;
        height: 700px;
        object-fit: cover;
        object-position: top left;
    }
    .main{
        background-image: url('@/assets/HousePrice/graybackground.jpg');
        background-repeat: no-repeat;
        background-size: cover;
        height: 100vh;
    }
</style>