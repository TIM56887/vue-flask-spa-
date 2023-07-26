<template>
    <section class="learning-resource mb-5">
        <h1 class="title">我的學習資源</h1>
        <div class="box">
            <InfoBox v-for="content, index in learningcontent" :content="content" :key="index"/>
        </div>
    </section>
</template>

<script>
import InfoBox from './InfoBox.vue'
export default {
    components:{
        InfoBox
    },
    data(){
        return{
            learningcontent:[
                {
                    title:'Mysql',
                    review:'youtube上的免費課程，初學者也能看懂，個人覺得非常實用!',
                    url:'https://www.youtube.com/playlist?list=PLmOn9nNkQxJFi4x7rZ5wpUKts3u7cDx21',
                    img:require('../assets/mysql.png')
                },
                {
                    title:'vue',
                    review:'本套视频教程对Vue3和Vue2的各项核心技术及周边技术进行了详细的讲解，所有知识点都以案例为驱动，生活化举例，讲解细致，幽默风趣。',
                    url:'https://www.youtube.com/playlist?list=PLmOn9nNkQxJEARHuEpVayY6ppiNlkvrnb',
                    img:require('../assets/logo.png')
                },
                {
                    title:'html&css',
                    review:'youtube上的免費課程，初學者也能看懂，個人覺得非常實用!',
                    url:'https://www.youtube.com/playlist?list=PLmOn9nNkQxJGGuwYhQzTmRGFwF9cHYS-x',
                    img:require('../assets/html.png')

                },
                {
                    title:'freecodecamp',
                    review:'一個能在網頁上練習撰寫程式的網站',
                    url:'https://www.freecodecamp.org/',
                    img:require('../assets/freecodecamp.jpg')
                }
            ]
        }
    }
}
</script>

<style>
 .title {
    color:transparent;
    
    font-size: 1.8rem;
    font-weight: 600;
 }
    .box {
        display: flex;
        flex-direction: row;
        /* justify-content: ; */
        margin-top: 50px;
        
    }
    .learning-resource {
        margin-top: 100px;
        
    }
    
</style>