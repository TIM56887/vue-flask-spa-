<template>
    <section class="learning-resource" id="section2">
        <div class="title">
            Resources
        </div>
        <div class="container-fluid">
            <div class="row justify-content-center p-0">
                <div class="col-md-2 col-xxl-2 side-bar">
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="basic-addon1">
                            <i class="bi bi-search"></i>
                        </span>
                        <input type="text" v-model="searchValue"  class="form-control" placeholder="search..." aria-label="Username" aria-describedby="basic-addon1">
                    </div>
                    <ul>
                        <li class="clickSearch" @click="clickSearch">python</li>
                        <li class="clickSearch" @click="clickSearch">Front-End</li>
                        <li class="clickSearch" @click="clickSearch">sql</li>
                        <li class="clickSearch" @click="clickSearch">css</li>
                        <li class="clickSearch" @click="cleanSearch">
                            <i class="bi bi-stars">clear</i>
                        </li>
                    </ul>
                </div>
                <div class="col-md-9 col-xxl-7 content p-0">
                    <div class="box">
                        <InfoBox v-for="content, index in filterLearningContent" 
                        :content="content" 
                        :key="index"
                        />
                    </div>
                </div>
            </div>
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
            searchValue:"",
            learningcontent:[
                {
                    title:'Mysql',
                    review:'youtube上的免費課程，初學者也能看懂，個人覺得非常實用!',
                    url:'https://www.youtube.com/playlist?list=PLmOn9nNkQxJFi4x7rZ5wpUKts3u7cDx21',
                    img:require('../assets/mysql.png')
                },
                {
                    title:'vue',
                    review:'本套视频教程对Vue3和Vue2的各项核心技术及周边技术进行了详细的讲解',
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
                },
                {
                    title:'Python',
                    review:'完整Python教程',
                    url:'https://www.youtube.com/playlist?list=PLmOn9nNkQxJFGvtKd7PI7AhsYmY-6FrJs',
                    img:require('../assets/python.png')
                },
                {
                    title:'roadmap.sh',
                    review:'軟體開發者的技能樹地圖，提供很多成為特定軟體領域開發者的學習指引',
                    url:'https://roadmap.sh/',
                    img:require('../assets/roadmapPic.png')
                },                
                {
                    title:'100 Days CSS ',
                    review:'100天css挑戰',
                    url:'https://100dayscss.com/',
                    img:require('../assets/css.png')
                },
                {
                    title:'CSS Grid',
                    review:'CSS Grid 小遊戲',
                    url:'https://cssgridgarden.com/',
                    img:require('../assets/cssgrid.png')
                },
                {
                    title:'css-tricks.com',
                    review:'Free website to upskill your css',
                    url:'https://cssgridgarden.com/',
                    img:require('../assets/css-trick.png')
                },
                {
                    title:'Python and AI',
                    review:'Free videos on Python and AI, including tutorials on TensorFlow, NumPy, and Pandas.',
                    url:'https://www.youtube.com/@MorvanZhou/playlists',
                    img:require('../assets/mofan.png')
                },
                {
                    title:' NLP spaCy',
                    review:'spaCy tutorial,natural language processing.',
                    url:'https://www.youtube.com/watch?v=dIUTsFT2MeQ',
                    img:require('../assets/spacy.png')
                },
                {
                    title:' SQL ZOO',
                    review:'Learn SQL step by step',
                    url:'https://sqlzoo.net/wiki/SQL_Tutorial',
                    img:require('../assets/sqlzoo.png')
                },
                
            ],
        }
    },
    computed:{
        filterLearningContent(){
            return this.learningcontent.filter( item=>{
                return item.title.toLowerCase().includes(this.searchValue.toLowerCase())
                }
            )
        }
    },
    methods:{
        clickSearch(e){
            this.searchValue = e.target.innerText
        },
        cleanSearch(){
            this.searchValue = ""
        },
    }
}
</script>

<style scoped>


@media (min-width: 768px) {
    .content {
    
        padding-left: 5rem;
        margin-bottom: 5rem;
    }
    .input-group {
        max-width:300px;
    }
    .box {
        display: flex;
        flex-direction: row;
        margin-top: 50px;
        flex-wrap: wrap;
    }
    .title {
        text-align: center;
        color:#1e1e1e;
        font-size: 3rem;
        font-weight: 900;
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
        background-image: linear-gradient(to right, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
        padding-top: 150px;
    }

    .learning-resource {
        min-height: 150vh;
        background-color: #f6f7f8;
    }
    .side-bar {
        margin-top: 120px;
        position: sticky;
        top: 200px;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 800;
    }
    .input-group{
        width: 200px;
    }

    li {
        border:1px solid #b7b5b5;
        color: #3c3c3c;
        border-radius: 10px;
        display: block;
        width: 100px;
        text-align: center;
        margin-bottom: 15px;
        --tw-gradient-from: #60a5fa;
        --tw-gradient-to: #1d4ed8;
        --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
        background-image: linear-gradient(to right, var(--tw-gradient-stops));
        -webkit-background-clip: text;
        background-clip: text;
    }
    li:hover {
        opacity: 1;
        color: transparent;
        border:1px solid #b6b7b7;;
    }

}


    @media (max-width: 768px) {
        .box {
            display: flex;
            flex-direction: column;
            
            
        }
        .content {
            
            padding-left: 5rem;
            margin-bottom: 5rem;
        }
        .input-group {
            max-width:90%;
        }

        .title {
            text-align: center;
            color:#1e1e1e;
            font-size: 2rem;
            font-weight: 600;
            --tw-gradient-from: #60a5fa;
            --tw-gradient-to: #1d4ed8;
            --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            background-image: linear-gradient(to right, var(--tw-gradient-stops));
            -webkit-background-clip: text;
            background-clip: text;
            padding-top: 20px;
        }

        .learning-resource {
            min-height: 150vh;
            background-color: #f6f7f8;
        }
        .side-bar {
            margin-top: 10px; 
            height: 150px;
            display: flex;
            flex-direction: column;
            z-index: 800;
        }

        ul {
            display: flex;
            flex-wrap: wrap;
            margin: 0;
        }
        li {
            border:1px solid #b7b5b5;
            color: #3c3c3c;
            border-radius: 10px;
            display: block;
            width: 100px;
            text-align: center;
            margin-bottom: 15px;
            --tw-gradient-from: #60a5fa;
            --tw-gradient-to: #1d4ed8;
            --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to);
            background-image: linear-gradient(to right, var(--tw-gradient-stops));
            -webkit-background-clip: text;
            background-clip: text;
        }
        li:hover {
            opacity: 1;
            color: transparent;
            border:1px solid #b6b7b7;;
        }

    }
    
</style>