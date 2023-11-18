<template>
<nav class="navbar">
    <div class="container-fluid">
        <div class="row w-100">
            <div class="col-4 d-flex align-items-center ps-5 ">
                <h1 class="fs-4 lh-lg"><a href="" class="text-decoration-none fw-bold text-secondary">TIM</a></h1>
            </div>
            <div class="col-4 d-flex justify-content-center">
                <ul class="w-100 nav justify-content-center fs-4 lh-lg text-center">
                    <li class="w-25" @click="scrollTo('section1')">Project</li>
                    <li class="w-25" @click="scrollTo('section2')">Resources</li>
                    <li class="w-25" @click="scrollTo('section3')">About me</li>
                </ul>
            </div>
        </div>
    </div>
</nav>
</template>

<script>
    export default {
        methods: {
        scrollTo(sectionId) {
            const el = document.getElementById(sectionId);
                if (el) {
                    el.scrollIntoView({ behavior: 'smooth' });
                }
            }
        }
    }
</script>

<style scoped>
.navbar{
    border-bottom: 0px solid rgb(175, 175, 175);
    box-shadow: 0 1px 0 0 rgba(0,0,0,.1);
    opacity: .95;
    position: fixed;
    width: 100%;
    height: 75px;
    background: #fff;
    z-index: 1000;
}
li:hover {
  cursor: pointer; /* 讓滑鼠指針變成點擊時的手形樣式 */
  
  background-color: #f5f5f5; /* 背景顏色改變 */
  /* 您可以添加其他樣式，如邊框、陰影等 */
}
</style>