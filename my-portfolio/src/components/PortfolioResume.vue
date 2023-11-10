<template>
    <section class="profile">
        <div class="content">
            <div class="text">
                <h1>Hi, I'm Tim</h1>
                <p>I am currently focusing on learning data analysis, data processing, and front-end development, I hope to continue improving in the future to expand my professional development field📍</p>
                <p>你好 ! 我叫昌頡，正專注於資料分析、資料處裡、前端開發學習。希望未來能持續進步，以擴展自己的職業發展範疇。 </p>
                
                <a href="https://github.com/TIM56887" target="_blank">
                    <i class="fab fa-github"></i>
                </a>
            </div>
            <img alt="profile picture" class="profilePc" src="../assets/IMG_2115.jpeg">
        </div>
        <div class="techStack">
            <h2>
                Tech Stack
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
        </div>        
    </section>
</template>

<script>
export default {
    name:'PortfolioResume'
}
</script>

<style scoped>


@media (min-width: 768px){

    .techPIC{
        width: 7rem;
        height: 7rem;
        border-radius: 100%;
        background-color: white;
        list-style-type: none;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        margin: 1rem 1rem 0 0;
    }

    .html{
        object-fit: cover;
        max-width: auto;
        max-height: 5.5rem;
    }
    .css{
        max-width: auto;
        max-height: 6rem;
    }
    .js{
        max-width: auto;
        max-height: 5.5rem;
    }

    .python {
        max-width: auto;
        max-height: 5.5rem;
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
        display: flex;
        justify-content: center;
    }
    
    .profilePc{
        margin-left: 150px;
        width:auto;
        height: 15rem;
        border-radius: 50%;
        background-size: contain;
        animation: morph 8s ease-in-out infinite;
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
    h1 {
        font-size: 50px;
    }
    h2::after {
        content: "|";
        margin-left: 20px;
        line-height: 1.2;
        font-size: 1.5em;
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
        /* width: 75vw; */
        height:100vh;
        padding-left: 25vw;
        min-height: 400px;
        max-height: 1100px;
        
        
    }
    p {
        line-height: 1.7;
        font-size: 1.3rem;
        
    }
    .text{
        width:40%
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
        width:85%
    }
}


</style>