<template>
  <section class="aboutme">
    <div class="background animate__animated animate__bounce animate__fadeInLeftBig" v-show="showAboutMe">
        <h1>
            <div class="aboutmetitle" ref="scrollElement">ABOUT ME </div>
        </h1>
        <div class="aboutMetitle">
            <router-link active-class="active" to="/aboutlearn">學習資源</router-link>
            <router-link active-class="active" to="/aboutwork">經歷</router-link>
            <router-link active-class="active" to="/aboutlife">基本資料</router-link>
        </div>
        <div class="content">
            <transition name="about">
                <keep-alive>
                    <router-view></router-view>
                </keep-alive>
            </transition>
        </div>
    </div>
  </section>
</template>

<script>
import 'animate.css';
export default {
    data(){
        return{
            showAboutMe:false
        }
    },
    name:'AboutMe',
    mounted(){
        window.addEventListener('scroll', this.checkScroll);
    },
    beforeDestroy(){
        window.removeEventListener('scroll', this.checkScroll);
    },
    methods:{
        checkScroll() {
            // 滾輪滑到的位置
            let scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
             // 跟上一次滑到的位置比較，如果滑到一個特定位置，則觸發路由
            // if (scrollPosition > this.lastScrollPosition) {
            // 判斷是否已經滑到特定位置
                if (scrollPosition > this.$refs.scrollElement.scrollTop) {
                    this.showAboutMe = true
                    if(this.$route.path == '/' ){
                        this.$router.push('/aboutlearn');
                        
                    }
                }
            // }
            // 更新最後滾輪的位置
            // this.lastScrollPosition = scrollPosition;
        },

    
    
    }
}
</script>

<style scoped>



@media (min-width: 768px) {

    



    .background {
        width:100%;
        min-height: 700px;
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 1rem;
        /* color: #1d70d6; */
        margin-right: 10rem;
        border: 2px solid transparent;
        box-shadow: inset 0 0 10px rgba(8, 8, 8,0.1); 
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
        background-image: linear-gradient(to right, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
    }
    h1{
        text-align: center;
        
        
    }
    .aboutmetitle{
        font-size: 1.5rem;
        font-weight: 700;
        font-family: inherit;
        line-height: 1.1;
        margin-top: 2rem;
        display: inline-block;
        color:transparent;
    }
    .aboutme {
        width:100%;
        min-height: 80vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #ffffff;
    }

    .aboutMetitle{
        display: flex;
        justify-content: space-around;
        width:50%;
        margin-top: 5rem;
        /* height:clamp(1.3rem, 2rem ,3rem) */
        height: 4rem;
    }
    a {
        font-size: 2rem;
        background-color: #ffffff;
        color: #ccc;
        border:none;
        text-decoration: none;
        font-weight: 400;
        transition: color 0.7s 0.1s, font-size 0.2s 0.2s;
    }

    .active {
        color: #1e1e1e;
        border-bottom: 5px solid #1e1e1e;
        font-size: 2.5rem  ;
    }

    .content {
        width: 100%;
        padding-left: 13%;
    }
    .about-enter-active {
        transition: opacity 0.1s;
    }
    .about-enter, .about-leave-to {
        opacity: 0;
    }
    .about-enter-to {
        opacity: 1;
    }
}
@media (max-width: 768px) {

    .background {
        width:100%;
        /* height: 110vh; */
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 1rem;
        /* color: #60a5fa; */
        /* margin-right: 10rem; */
        border: 2px solid transparent;
        box-shadow: inset 0 0 10px rgba(8, 8, 8,0.1);
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
        background-image: linear-gradient(to right, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text; 
    }


    h1{
        text-align: center;
    }
    .aboutmetitle{
        font-size: 1rem;
        font-weight: 700;
        font-family: inherit;
        line-height: 1.1;
        margin-top: 2rem;
        display: inline-block;
        color:transparent;
    }
    .aboutme {
        width:100vw;
        /* height: 120vh; */
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #ffffff;
    }

    .aboutMetitle{
        display: flex;
        justify-content: space-around;
        width:100%;
        margin: 2rem 0;
        /* height:clamp(1.3rem, 2rem ,3rem) */
        height: 3rem;
    }
    a {
        font-size: 1rem;
        background-color: #ffffff;
        color: #ccc;
        border:none;
        text-decoration: none;
        font-weight: 700;
        transition: color 0.3s 0.1s, font-size 0.1s 0.2s;
    }

    .active {
        color: #1e1e1e;
        border-bottom: 4px solid #1e1e1e;
        font-size: 2rem  ;
    }

    .content {
        width: 80%;
    }
    .about-enter-active {
    transition: opacity 0.8s;
    }
    .about-enter, .about-leave-to {
    opacity: 0;
    }
}
</style>