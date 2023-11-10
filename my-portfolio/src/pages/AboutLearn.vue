<template>
    <div class="aboutlearn">
        <LearningResource /> 
    </div>
  

</template>

<script>
import LearningResource from './LearningResource.vue';
export default {
    components:{
        LearningResource
    },
    
}
</script>

<style scoped>

    

    @media (min-width:768px){
    
    a {
        margin-top:60px;
    }

    .pic:hover{
        opacity: 0.5;
    }
    
    .aboutlearn {
        width:100%;
        display:flex;
        flex-direction: column;
        /* height: 100%; */
    }

    
    
    .title{
        font-size: 1.8rem;
        font-weight: 400;
        color: #1e1e1e;
    }

    .text {
        font-size: 1.3rem;
        font-weight: 200;
        padding: 0 50px 0 20px;
        line-height: 1.5;
        font-family: Microsoft JhengHei;
        color: #616161
    } 
    }
    @media (max-width:768px){

    
    

    
    
    
    .aboutlearn {
        width:100%;
    }
    .content{
        margin-top: 1rem;
    }
    .title{
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e1e1e;
    }

    .text {
        font-size: 1.3rem;
        font-weight: 200;
        padding: 0 50px 0 20px;
        line-height: 2;
        font-family: Microsoft JhengHei;
        color: #616161
    }
    }
    
</style>