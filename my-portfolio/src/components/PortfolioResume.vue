<template>
    <section class="profile">
        
            <div class="container-fluid main-content" >
                <transition name="fade">
                    <h1 class="fw-bolder title" v-if="!isScrolledFromTop">Timmy's Personal Website</h1>
                </transition>
                <transition name="fade">
                    <div class="row justify-content-center align-items-center h-100 preview" v-if="isScrolledFromTop">
                        <div class="col-4">
                            <p class="fs-3 fw-medium">Hi, I'm Tim 
                                currently focusing on 
                                data analysis,
                                data processing, 
                                and front-end development.
                                Here's some of my project...
                            </p>
                            <div class="techStack" v-if="isScrolledFromTop" >
                                <h4>
                                    build with
                                </h4>
                                <ul class="techPICLine">
                                    <li class="techPIC">
                                        <img class="html" src="../assets/html.png" alt="html">
                                    </li>
                                    <li class="techPIC">
                                        <img class="css" src="../assets/css.png" alt="html">
                                    </li>
                                    <li class="techPIC">
                                        <img class="js" src="../assets/JavaScript.png" alt="html">
                                    </li>
                                    <li class="techPIC">
                                        <img class="python" src="../assets/python.png" alt="html">
                                    </li>
                                </ul>
                            </div>    
                        </div>
                        <div class="col-3">
                            <img alt="profile picture" class="profilePc" src="../assets/IMG_2115.jpeg">
                        </div>
                        
                   </div>
                </transition>
                <transition name="fade">
  
 
                </transition>

            </div>
        <span class="scrollNav" v-if="!isScrolledFromTop">scroll</span>

        
        
        <!-- <div class="content">
            <div class="text " :class="{scrolled:!scrolled}">
                <h1>Hi, I'm Tim</h1>
                <p>I am currently focusing on learning data analysis, data processing, and front-end development, I hope to continue improving in the future to expand my professional development field📍</p>
                <p>你好 ! 我叫昌頡，正專注於資料分析、資料處裡、前端開發學習。希望未來能持續進步，以擴展自己的職業發展範疇。 </p>
                
                <a  href="https://github.com/TIM56887" target="_blank">
                    <i class="fab fa-github"></i>
                </a>
            </div>
            
        </div>
        <div class="techStack" :class="{scrolled:!scrolled}">
            <h2>
                Tech
            </h2>
            <ul class="techPICLine">
                <li class="techPIC">
                    <img class="html" src="../assets/html.png" alt="html">
                </li>
                <li class="techPIC">
                    <img class="css" src="../assets/css.png" alt="html">
                </li>
                <li class="techPIC">
                    <img class="js" src="../assets/JavaScript.png" alt="html">
                </li>
                <li class="techPIC">
                    <img class="python" src="../assets/python.png" alt="html">
                </li>
            </ul>
        </div>         -->
    </section>
</template>

<script>
export default {
    name:'PortfolioResume',
    data(){
        return {
            
            isScrolledFromTop: false
        }
    },
    mounted(){
        window.addEventListener('scroll', this.handleScroll);
    },
    methods: {
        handleScroll(){
            this.isScrolledFromTop = window.scrollY > 0;
        }
    }

    

}
</script>
    
<style scoped>
.techStack {
    /* position:absolute;
    top: 90%;
    left: 79%;
    transform: translate(-50%,-50%); */
}
.preview {
    padding-top: 350px;
    padding-left: 200px;
    position: relative;
}
.title {
    position:absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    
}
.main-content {
    height: 100vh;
    
    /* position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0; */
}
@keyframes lineMove {
  0% {
    height: 2px;
    transform: translateY(-120px);
  }
  50% {
    height: 80px;
    transform: translateY(-35px);
  }
    100% {
        height: 1px;
        transform: translateY(-50px);
    }
}
 .scrollNav:after {
    content: "";
    position: absolute;
    display: inline-block;
    width: 1px;
    height: 80px;
    background-color: rgb(190, 190, 190);
    left: 18px;
    bottom: -130px;
    animation: lineMove .9s ease-in-out infinite;
    animation-duration: 0.9s;
    animation-timing-function: ease-in-out;
    animation-delay: 0s;
    animation-iteration-count: infinite;
    animation-direction: normal;
    animation-fill-mode: none;
    animation-play-state: running;
    animation-name: lineMove;
    animation-timeline: auto;
    animation-range-start: normal;
    animation-range-end: normal;
}
@keyframes equallyBound  {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(10px); /* 或者是你想要的移動距離 */
  }
}

.scrollNav {
    animation: equallyBound 1.4s ease infinite;
    transform: (50%,50%);
    position: absolute;
    left: 49%;
    bottom: 100px;
}

.fade-transition {
  position: relative;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 1s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

@media (min-width: 768px){

    .techPIC{
        width: 3rem;
        height: auto;
        border-radius: 100%;
        background-color: white;
        list-style-type: none;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        margin: 0.5rem 1rem 0 0;
        /* padding: 0; */
    }

    .html{
        /* object-fit: cover; */
        max-width: auto;
        max-height: 3rem;
    }
    .css{
        max-width: auto;
        max-height: 3rem;
    }
    .js{
        max-width: auto;
        max-height: 3rem;
    }

    .python {
        max-width: auto;
        max-height: 3rem;
        padding-top: 8px;
    }

    .techStack{
        display:flex;
        justify-content: flex-start;
        align-items: center;
        
    }
    i.fab.fa-github:hover {
        color: blue;
    }
    ul {
        padding: 0 !important;
        display: flex;
        justify-content: center;
    }
    
    .profilePc{
        margin-left: 150px;
        width:auto;
        height: 15rem;
        border-radius: 50%;
        background-size: contain;
        animation: morph 6s ease-in-out infinite;
        border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
        transition: all 2s ease-in-out;
        border: 3px solid black;
        }
    .content {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        padding: 10% 0 3% 0;
    }
    .fab {
        margin-top: 50px;
       font-size: 30px;
        color: black;   
    }
    h4 {
        font-size: 20px;
        width: 150px;
    }
    h4::after {
        content: "|";
        margin-left: 1px;
        line-height: 1.2;
        font-size: 1.2em;
    }

    p {
        font-size: 20px
    }

    @keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
    }
    @keyframes morph {
            0% {
            border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                }

            50% {
            border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
                }

            100% {
            border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                }
        }

    .profile{
        background-color: #ffffff;
        /* width: 75vw;
        /* height:93vh; */
        /* padding-left: 25vw; */
        /* min-height: 400px; */
        /* max-height: 1100px; */
        font-family: Menlo, Monaco, Consolas
        
        
    }
    p {
        line-height: 1.7;
        font-size: 1.3rem;
        
    }
    .text{
        width:40%;
        transition: all 1s;

    }
}


@media (max-width: 768px){

    .techPIC{
        width: 5rem;
        height: 5rem;
        border-radius: 100%;
        background-color: white;
        list-style-type: none;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: flex-start;
        margin: 0.5rem 0 0 0;

    }

    .html{
        
        max-width: auto;
        max-height: 5rem;
    }
    .css{
        max-width: auto;
        max-height: 5.4rem;
    }
    .js{
        max-width: auto;
        max-height: 5rem;
    }

    .python {
        max-width: auto;
        max-height: 4.5rem;
        padding-top: 8px;
    }

    .techStack{
        display:flex;
        justify-content: flex-start;
        align-items: center;
        flex-direction: column;
    }
    .techPICLine {
        display: flex;
        flex-direction: row;
        margin-top: 0.5rem;
        padding:0;
    }
    



    i.fab.fa-github:hover {
        color: rgb(60, 60, 235);
    }
    
    .profilePc{
        margin-left: 50px;
        width:auto;
        height: 10rem;
        border-radius: 50%;
        background-size: cover;
        animation: morph 8s ease-in-out infinite;
        border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
        transition: all 2s ease-in-out;
        border: 3px solid black;
        }
    .content {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        padding: 10% 0 3% 0;
    }
    .fab {
        margin-top: 25px;
        font-size: 30px;
        color: black;   
    }
    h1 {
        font-size: 30px;
    }
    h2::after {
        content: "-";
        margin-left: 10px;
        line-height: 1.2;
        font-size: 1.2em;
        
    }

    h2 {
        font-size:2rem;
        font-weight: 600;
        
    }

    p {
        font-size: 20px
    }

    @keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
    }
    @keyframes morph {
            0% {
            border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                }

            50% {
            border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
                }

            100% {
            border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
                }
        }

    .profile{
        background-color: #ffffff;
        width: 100vw;
        /* height:100vh; */
        padding-left: 2vw;
        min-height: 400px;
    }
    p {
        line-height: 1.7;
        font-size: 1.3rem;
        
    }
    .text{
        width:85%;
        
    }
}


</style>